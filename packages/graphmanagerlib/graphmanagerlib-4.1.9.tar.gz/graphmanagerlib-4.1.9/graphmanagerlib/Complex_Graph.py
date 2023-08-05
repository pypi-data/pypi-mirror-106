import numpy as np
import pandas as pd
import itertools
import networkx as nx


class Grapher:
    """
    Description:
            This class is used to generate:
                    1) the graph (in dictionary form) { source_node: [destination_node1, destination_node2]}
                    2) the dataframe with relative_distances
    Inputs: The class consists of a pandas dataframe consisting of cordinates for bounding boxe and the image of the invoice/receipt.
    """

    def __init__(self, document):
        self.nodes = document.nodes
        self.G, self.df = self.graph_formation()
        self.relative_distance(document.width, document.height)

    def graph_formation(self):

        """
        Description:
        ===========
        Line formation:
        1) Sort words based on Top coordinate:
        2) Form lines as group of words which obeys the following:
            Two words (W_a and W_b) are in same line if:
                Top(W_a) <= Bottom(W_b) and Bottom(W_a) >= Top(W_b)
        3) Sort words in each line based on Left coordinate
        This ensures that words are read from top left corner of the image first,
        going line by line from left to right and at last the final bottom right word of the page is read.

        Args:
            df with words and cordinates (xmin,xmax,ymin,ymax)
            image read into cv2
        returns:
            df with words arranged in orientation top to bottom and left to right, the line number for each word, index of the node connected to
            on all directions top, bottom, right and left (if they exist and satisfy the parameters provided)
        _____________________y axis______________________
        |
        |                       top
        x axis               ___________________
        |              left | bounding box      |  right
        |                   |___________________|
        |                       bottom
        |
        |
        iterate through the rows twice to compare them.
        remember that the axes are inverted.

        """

        """
        preprocessing the raw nodes list to favorable df 
        """
        df = pd.DataFrame([node.getInfo() for node in self.nodes])

        temp = df.copy()
        temp.fillna('', inplace=True)
        temp.columns = ['xmin', 'ymin', 'xmax', 'ymax', 'Object', 'Tag']
        df = temp

        assert type(df) == pd.DataFrame, f'object_map should be of type \
                    {pd.DataFrame}. Received {type(df)}'

        assert 'xmin' in df.columns, '"xmin" not in object map'
        assert 'xmax' in df.columns, '"xmax" not in object map'
        assert 'ymin' in df.columns, '"ymin" not in object map'
        assert 'ymax' in df.columns, '"ymax" not in object map'
        assert 'Object' in df.columns, '"Object" column not in object map'
        assert 'Tag' in df.columns, '"Tag" column not in object map'

        # remove empty spaces both in front and behind
        for col in df.columns:
            try:
                df[col] = df[col].str.strip()
            except AttributeError:
                pass

        # further cleaning
        df.dropna(inplace=True)
        # sort from top to bottom
        df.sort_values(by=['ymin'], inplace=True)
        df.reset_index(drop=True, inplace=True)

        # subtracting ymax by 1 to eliminate ambiguity of boxes being in both left and right
        df["ymax"] = df["ymax"].apply(lambda x: x - 1)

        master = []
        for idx, row in df.iterrows():
            # flatten the nested list
            flat_master = list(itertools.chain(*master))
            # check to see if idx is in flat_master
            if idx not in flat_master:
                top_a = row['ymin']
                bottom_a = row['ymax']
                # every line will atleast have the word in it
                line = [idx]
                for idx_2, row_2 in df.iterrows():
                    # check to see if idx_2 is in flat_master removes ambiguity
                    # picks higher cordinate one.
                    if idx_2 not in flat_master:
                        # if not the same words
                        if not idx == idx_2:
                            top_b = row_2['ymin']
                            bottom_b = row_2['ymax']
                            if (top_a <= bottom_b) and (bottom_a >= top_b):
                                line.append(idx_2)
                master.append(line)

        df2 = pd.DataFrame({'words_indices': master, 'line_number': [x for x in range(1, len(master) + 1)]})
        # explode the list columns eg : [1,2,3]
        df2 = df2.set_index('line_number').words_indices.apply(pd.Series).stack() \
            .reset_index(level=0).rename(columns={0: 'words_indices'})
        df2['words_indices'] = df2['words_indices'].astype('int')
        # put the line numbers back to the list
        final = df.merge(df2, left_on=df.index, right_on='words_indices')
        final.drop('words_indices', axis=1, inplace=True)

        """
        3) Sort words in each line based on Left coordinate
        """
        final2 = final.sort_values(by=['line_number', 'xmin'], ascending=True) \
            .groupby('line_number') \
            .head(len(final)) \
            .reset_index(drop=True)

        df = final2
        """
        Pseudocode:
        1) Read words from each line starting from topmost line going towards bottommost line
        2) For each word, perform the following:
            - Check words which are in vertical projection with it.
            - Calculate RD_l and RD_r for each of them 
            - Select nearest neighbour words in horizontal direction which have least magnitude of RD_l and RD_r, 
            provided that those words do not have an edge in that direciton.
                    - In case, two words have same RD_l or RD_r, the word having higher top coordinate is chosen.
            - Repeat steps from 2.1 to 2.3 similarly for retrieving nearest neighbour words in vertical direction by 
            taking horizontal projection, calculating RD_t and RD_b and choosing words having higher left co-ordinate
            incase of ambiguity
            - Draw edges between word and its 4 nearest neighbours if they are available.
        Args: 
            df after lines properly aligned

        returns: 
            graph in the form of a dictionary, networkX graph, dataframe with 
        """

        # horizontal edges formation
        # print(df)
        df.reset_index(inplace=True)
        grouped = df.groupby('line_number')
        # for undirected graph construction
        horizontal_connections = {}
        # left
        left_connections = {}
        # right
        right_connections = {}

        for _, group in grouped:
            a = group['index'].tolist()
            b = group['index'].tolist()
            horizontal_connection = {a[i]: a[i + 1] for i in range(len(a) - 1)}
            # storing directional connections
            right_dict_temp = {a[i]: {'right': a[i + 1]} for i in range(len(a) - 1)}
            left_dict_temp = {b[i + 1]: {'left': b[i]} for i in range(len(b) - 1)}

            # add the indices in the dataframes
            for i in range(len(a) - 1):
                df.loc[df['index'] == a[i], 'right'] = int(a[i + 1])
                df.loc[df['index'] == a[i + 1], 'left'] = int(a[i])

            left_connections.update(right_dict_temp)
            right_connections.update(left_dict_temp)
            horizontal_connections.update(horizontal_connection)

        dic1, dic2 = left_connections, right_connections

        # verticle connections formation
        bottom_connections = {}
        top_connections = {}

        for idx, row in df.iterrows():
            if idx not in bottom_connections.keys():
                right_a = row['xmax']
                left_a = row['xmin']

                for idx_2, row_2 in df.iterrows():
                    # check for higher idx values

                    if idx_2 not in bottom_connections.values() and idx < idx_2:
                        right_b = row_2['xmax']
                        left_b = row_2['xmin']
                        if (left_b <= right_a) and (right_b >= left_a):
                            bottom_connections[idx] = idx_2
                            top_connections[idx_2] = idx

                            # add it to the dataframe
                            df.loc[df['index'] == idx, 'bottom'] = idx_2
                            df.loc[df['index'] == idx_2, 'top'] = idx
                            # print(bottom_connections)
                            # once the condition is met, break the loop to reduce redundant time complexity
                            break

                            # combining both
        result = {}
        dic1 = horizontal_connections
        dic2 = bottom_connections

        for key in (dic1.keys() | dic2.keys()):
            if key in dic1: result.setdefault(key, []).append(dic1[key])
            if key in dic2: result.setdefault(key, []).append(dic2[key])
        # print(result)

        G = nx.from_dict_of_lists(result)

        return G, df

        # features calculation

    def get_text_features(self, df):
        """
        gets text features
        Args: df
        Returns: n_lower, n_upper, n_spaces, n_alpha, n_numeric,n_special
        """
        data = df['Object'].tolist()

        '''
            Args:
                df

            Returns: 
                character and word features

        '''
        special_chars = ['&', '@', '#', '(', ')', '-', '+',
                         '=', '*', '%', '.', ',', '\\', '/',
                         '|', ':']

        # character wise
        n_lower, n_upper, n_spaces, n_alpha, n_numeric, n_special = [], [], [], [], [], []

        for words in data:
            lower, upper, alpha, spaces, numeric, special = 0, 0, 0, 0, 0, 0
            for char in words:
                if char.islower():
                    lower += 1
                # for upper letters
                if char.isupper():
                    upper += 1
                # for white spaces
                if char.isspace():
                    spaces += 1
                    # for alphabetic chars
                if char.isalpha():
                    alpha += 1
                    # for numeric chars
                if char.isnumeric():
                    numeric += 1
                if char in special_chars:
                    special += 1

            n_lower.append(lower)
            n_upper.append(upper)
            n_spaces.append(spaces)
            n_alpha.append(alpha)
            n_numeric.append(numeric)
            n_special.append(special)

        df['n_upper'], df['n_alpha'], df['n_spaces'], \
        df['n_numeric'], df['n_special'] = n_upper, n_alpha, n_spaces, n_numeric, n_special

    def relative_distance(self, image_width, image_height):
        """
        1) Calculates relative distances for each node in left, right, top  and bottom directions if they exist.
        rd_l, rd_r = relative distances left , relative distances right. The distances are divided by image width
        rd_t, rd_b = relative distances top , relative distances bottom. The distances are divided by image length
        2) Exports the complete document graph for visualization
        Args:
            result dataframe from graph_formation()

        returns:
            dataframe with features and exports document graph if prompted
        """

        df = self.df

        for index in df['index'].to_list():
            right_index = df.loc[df['index'] == index, 'right'].values[0]
            left_index = df.loc[df['index'] == index, 'left'].values[0]
            bottom_index = df.loc[df['index'] == index, 'bottom'].values[0]
            top_index = df.loc[df['index'] == index, 'top'].values[0]

            # check if it is nan value
            if np.isnan(right_index) == False:
                right_text = df.loc[df['index'] == right_index, 'Object'].values[0]
                right_word_left = df.loc[df['index'] == right_index, 'xmin'].values[0]
                source_word_right = df.loc[df['index'] == index, 'xmax'].values[0]
                df.loc[df['index'] == index, 'rd_r'] = (right_word_left - source_word_right) / image_width
                df.loc[df['index'] == index, 'right_text'] = right_text
                """
                for plotting purposes
                getting the mid point of the values to draw the lines for the graph
                mid points of source and destination for the bounding boxes
                """
                right_word_x_max = df.loc[df['index'] == right_index, 'xmax'].values[0]
                right_word_y_max = df.loc[df['index'] == right_index, 'ymax'].values[0]
                right_word_y_min = df.loc[df['index'] == right_index, 'ymin'].values[0]

                df.loc[df['index'] == index, 'destination_x_hori'] = (right_word_x_max + right_word_left) / 2
                df.loc[df['index'] == index, 'destination_y_hori'] = (right_word_y_max + right_word_y_min) / 2

            if np.isnan(left_index) == False:
                left_text = df.loc[df['index'] == left_index, 'Object'].values[0]
                left_word_right = df.loc[df['index'] == left_index, 'xmax'].values[0]
                source_word_left = df.loc[df['index'] == index, 'xmin'].values[0]
                df.loc[df['index'] == index, 'rd_l'] = (left_word_right - source_word_left) / image_width
                df.loc[df['index'] == index, 'left_text'] = left_text

            if np.isnan(bottom_index) == False:
                bottom_text = df.loc[df['index'] == bottom_index, 'Object'].values[0]
                bottom_word_top = df.loc[df['index'] == bottom_index, 'ymin'].values[0]
                source_word_bottom = df.loc[df['index'] == index, 'ymax'].values[0]
                df.loc[df['index'] == index, 'rd_b'] = (bottom_word_top - source_word_bottom) / image_height
                df.loc[df['index'] == index, 'bottom_text'] = bottom_text

                """for plotting purposes"""
                bottom_word_top_max = df.loc[df['index'] == bottom_index, 'ymax'].values[0]
                bottom_word_x_max = df.loc[df['index'] == bottom_index, 'xmax'].values[0]
                bottom_word_x_min = df.loc[df['index'] == bottom_index, 'xmin'].values[0]
                df.loc[df['index'] == index, 'destination_y_vert'] = (bottom_word_top_max + bottom_word_top) / 2
                df.loc[df['index'] == index, 'destination_x_vert'] = (bottom_word_x_max + bottom_word_x_min) / 2

            if np.isnan(top_index) == False:
                top_text = df.loc[df['index'] == top_index, 'Object'].values[0]
                top_word_bottom = df.loc[df['index'] == top_index, 'ymax'].values[0]
                source_word_top = df.loc[df['index'] == index, 'ymin'].values[0]
                df.loc[df['index'] == index, 'rd_t'] = (top_word_bottom - source_word_top) / image_height
                df.loc[df['index'] == index, 'top_text'] = top_text

        # replace all tne NaN values with '0' meaning there is nothing in that direction
        df[['rd_r', 'rd_b', 'rd_l', 'rd_t']] = df[['rd_r', 'rd_b', 'rd_l', 'rd_t']].fillna(0)
        df[['right_text', 'left_text', 'top_text', 'bottom_text']] = df[
            ['right_text', 'left_text', 'top_text', 'bottom_text']].fillna('NaN')

        # drop the unnecessary columns
        df.drop(['destination_x_hori', 'destination_y_hori', 'destination_y_vert', 'destination_x_vert'], axis=1,
                inplace=True)
        self.get_text_features(df)


