# predict v0.3:
# Much code commented for test purposes

import pickle
import pandas as pd


def load_model(path):
    with open(path, 'rb') as file:
        model = pickle.load(file)
    return model

def load_data(path, dates):
#     data_df = pd.read_csv('data/REE_data_aggregated_by_10mn.csv')
#     data = data_df.loc[data_df["datetime_utc"]==input_values[0], "demanda"].values[0]
    data = 15000
    return data

def get_prediction(model, cust_input, input_ids):
    # input_df = pd.DataFrame(cust_input).transpose()
    # input_df.columns = input_ids[0:]
    print("Modèle en entrée de get_prediction :", model)
    # return model.predict(input_df)[0]
    return 15000


def load_model_and_predict(path, cust_input, input_ids):
    """
    Args:
        path: path and name of selected model file
        cust_input: values of selected dates
        input_ids: names of selected dates
    
    Returns:
        get_prediction: prediction built from Args.
    """
    # model = load_model(path)
    print("Chemin du modèle en entrée de load_model_and_predict :", path)
    print("Données en entrée de load_model_and_predict :", cust_input)
    model = "fake model"
    return get_prediction(model, cust_input, input_ids)