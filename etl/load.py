import pandas as pd
from sklearn.preprocessing import LabelEncoder
import os

os.makedirs("data/load",exist_ok=True)

def read_combined_df():
    """Read the combined csv file and saves into new dataframe with model predictors

    Returns:
    crash_data_encode:
        A filtered crash dataframe that will be used for preprocess
    """    
    combined_crash_data=pd.read_csv("data/transform/Combined_Moco_Crash_Driver_Incident.csv")
    crash_data_encode=combined_crash_data[["injury_severity", "weather", "light", "hour_of_day", "day_of_week"]]
    return crash_data_encode

def prepare_crash_df(crash_data_encode):
    """ 
    Encodes the filtered crash data to prepare for models
        Parameters:
            crash_data_encode: dataframe
            The encoded crash dataframe

        Returns:
            crash_data_encode:
            A encoded crash dataframe of the model predictors that will then be used to train and test and split
    """    
    label_encoders={}
    for column in ["injury_severity", "weather", "light", "hour_of_day", "day_of_week"]:
        le=LabelEncoder()
        crash_data_encode[column]=le.fit_transform(crash_data_encode[column])
        label_encoders[column]= le
    crash_data_encode.to_csv("data/load/Combined_Moco_Crash_Data_Load.csv", index=False)
    return crash_data_encode