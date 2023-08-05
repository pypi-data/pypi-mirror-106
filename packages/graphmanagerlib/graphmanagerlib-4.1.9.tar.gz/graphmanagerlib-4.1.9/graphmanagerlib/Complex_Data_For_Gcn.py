import random
import torch
import torch_geometric
import numpy as np
from torch_geometric.utils.convert import from_networkx
from bpemb import BPEmb
from sentence_transformers import SentenceTransformer
from graphmanagerlib.Complex_Graph import Grapher
from graphmanagerlib.JsonManager import ConvertJsonToDocumentsObjects

bpemb_en = BPEmb(lang="fra", dim=100)
sent_model = SentenceTransformer('distilbert-base-nli-stsb-mean-tokens')


def make_bert_features_if_required(text):
    if (text == 'NaN'):
        return nan_features
    else:
        return make_sent_bert_features(text)


def make_sent_bert_features(text):
    emb = sent_model.encode([text])[0]
    return emb


nan_features = make_sent_bert_features('NaN')


def get_data(documents, tags):
    """
    returns one big graph with unconnected graphs with the following:
    - x (Tensor, optional) – Node feature matrix with shape [num_nodes, num_node_features]. (default: None)
    - edge_index (LongTensor, optional) – Graph connectivity in COO format with shape [2, num_edges]. (default: None)
    - edge_attr (Tensor, optional) – Edge feature matrix with shape [num_edges, num_edge_features]. (default: None)
    - y (Tensor, optional) – Graph or node targets with arbitrary shape. (default: None)
    - validation mask, training mask and testing mask
    """
    all_files = documents.copy()
    random.shuffle(all_files)

    train_list_of_graphs, test_list_of_graphs = [], []

    trainingProportion = round(((len(all_files) / 100) * 80))

    training, testing = all_files[:trainingProportion], all_files[trainingProportion:]

    for idx, file in enumerate(all_files):
        _, individual_data = makeIndividualData(file, tags)
        print(f'File {idx + 1}/{len(all_files)} --> Success', flush=True)
        if file in training:
            train_list_of_graphs.append(individual_data)
        elif file in testing:
            test_list_of_graphs.append(individual_data)

    train_data = torch_geometric.data.Batch.from_data_list(train_list_of_graphs)
    train_data.edge_attr = None
    test_data = torch_geometric.data.Batch.from_data_list(test_list_of_graphs)
    test_data.edge_attr = None
    return train_data, test_data


def makeIndividualData(file, tags):
    connect = Grapher(file)
    individual_data = from_networkx(connect.G)

    feature_cols = ['rd_b', 'rd_r', 'rd_t', 'rd_l', 'line_number', 'n_upper', 'n_alpha', 'n_spaces', 'n_numeric',
                    'n_special']

    df = connect.df

    text_features = np.array(df["Object"].map(make_sent_bert_features).tolist()).astype(np.float32)
    numeric_features = df[feature_cols].values.astype(np.float32)
    features = np.concatenate((numeric_features, text_features), axis=1)

    for val in ['right_text', 'left_text', 'top_text', 'bottom_text']:
        text_features = np.array(df[val].map(make_bert_features_if_required).tolist()).astype(np.float32)
        features = np.concatenate((features, text_features), axis=1)

    features = torch.tensor(features)

    """
    dfObjectNew = []
    tagsArray = np.array(df['Tag']).tolist()

    for idx, value in enumerate(df["Object"]):
        if (tagsArray[idx] != 'undefined'):
            dfObjectNew.append(make_bert_features_if_required(value))
        else:
            dfObjectNew.append(nan_features)

    text_features = np.array(dfObjectNew).astype(np.float32)
    numeric_features = df[feature_cols].values.astype(np.float32)
    features = np.concatenate((numeric_features, text_features), axis=1)

    for val in ['right_text', 'left_text', 'top_text', 'bottom_text']:
        dfNeighboorText = []
        for idx, value in enumerate(df[val]):
            if (tagsArray[idx] != 'undefined'):
                dfNeighboorText.append(make_bert_features_if_required(value))
            else:
                dfNeighboorText.append(nan_features)
        text_features = np.array(dfNeighboorText).astype(np.float32)
        features = np.concatenate((features, text_features), axis=1)

    features = torch.tensor(features)
    """
    for col in df.columns:
        try:
            df[col] = df[col].str.strip()
        except AttributeError as e:
            pass

    df['Tag'] = df['Tag'].fillna('undefined')
    for i, tagValue in enumerate(tags):
        df.loc[df['Tag'] == tagValue, 'num_labels'] = i + 1

    assert df[
               'num_labels'].isnull().values.any() == False, f'labeling error! Invalid label(s) present in {file}.csv, df:{df}'
    labels = torch.tensor(df['num_labels'].values.astype(int))
    text = df['Object'].values

    individual_data.x = features
    individual_data.y = labels
    individual_data.text = text

    return connect, individual_data


def getDataForUniquePrediction(json, tags):
    test_list_of_graphs = []
    documents = ConvertJsonToDocumentsObjects(json)[0]
    grapher, individual_data = makeIndividualData(documents, tags)
    test_list_of_graphs.append(individual_data)
    test_data = torch_geometric.data.Batch.from_data_list(test_list_of_graphs)
    test_data.edge_attr = None
    return grapher, test_data
