import os
import numpy as np
import torch

from graphmanagerlib.Complex_Graph import Grapher
from graphmanagerlib.Complex_Data_For_Gcn import getDataForUniquePrediction
from graphmanagerlib.JsonManager import ConvertJsonToDocumentsObjects,ConvertPredictionToJson


def make_info(document):
    connect = Grapher(document)
    return connect.df

def predictionsUnique(saved_model_folder,json,labels_tab):
    grapher, predictions_data = getDataForUniquePrediction(json, labels_tab)

    torchMode = "cuda" if torch.cuda.is_available() else "cpu"

    model = torch.load(os.path.join(saved_model_folder, "saved_model.pt"), torchMode)

    y_preds = model(predictions_data.to(device=torchMode)).max(dim=1)[1]
    y_preds = y_preds.cpu()
    y_preds = y_preds.numpy()
    # y_preds = model(predictions_data).max(dim=1)[1].cpu().numpy()

    test_batch = predictions_data.batch.cpu().numpy()
    sample_indexes = np.where(test_batch == 0)[0]
    y_pred = y_preds[sample_indexes]

    print("Beginning of the prediction", flush=True)

    df = grapher.df

    assert len(y_pred) == df.shape[0]

    predictions = []
    for row_index, row in df.iterrows():
        _y_pred = y_pred[row_index]
        _label = labels_tab[_y_pred]
        if _label != 'undefined':
            _text = row['Object']
            xmin, ymin, xmax, ymax = row[['xmin', 'ymin', 'xmax', 'ymax']]
            predictions.append({'Text': _text,
                                'Label': _label,
                                'XMin': xmin,
                                'YMin': ymin,
                                'XMax': xmax,
                                'YMax': ymax
                                })

    return ConvertPredictionToJson(predictions)

if __name__ == "__main__":
    predictionsUnique()