import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

os.makedirs("data/model_outputs",exist_ok=True)
  

def train_test_split_RF_df():
    """ Trains, tests and splits the loaded data to prepare for random forest classification model
        Returns:
            X_train_RF: 
                dataframe for crash model training data 
            X_test_RF: 
                data frame for crash model testing data
            y_train_RF: 
                A series of the injury severity crash model target training data
            y_test_RF: 
                A series of the injury severity crash model target testing data
    """
<<<<<<< HEAD
    crash_data_encode=pd.read_csv("data/load/Combined_Moco_Crash_Data_Load.csv")
    crash_training=crash_data_encode.copy()
    X=crash_training.drop(columns="injury_severity")
    y=crash_training["injury_severity"]
    X_train_RF, X_test_RF, y_train_RF, y_test_RF= train_test_split(X,y, test_size=0.2, random_state=42)
    return X_train_RF, X_test_RF, y_train_RF, y_test_RF
=======
    try:
        crash_data_encode=pd.read_csv("data/load/Combined_Moco_Crash_Data_Load.csv")
        crash_training=crash_data_encode.copy()
        X=crash_training.drop(columns="injury_severity")
        y=crash_training["injury_severity"]
        X_train_RF, X_test_RF, y_train_RF, y_test_RF= train_test_split(X,y, test_size=0.2, random_state=42)
        return X_train_RF, X_test_RF, y_train_RF, y_test_RF
    except:
        print("An exception has occured")
>>>>>>> test

def classfication_model_RF(X_train_RF, X_test_RF, y_train_RF, y_test_RF):
    """ Creates the random forest classification model 
        Parameters:
            X_train_RF: dataframe
                dataframe for crash model training data 
            X_test_RF: dataframe
                data frame for crash model testing data
            y_train_RF: series
                A series of the injury severity crash model target training data
            y_test_RF: series
                A series of the injury severity crash model target testing data
        Returns:
            rand_forest_model:
                The random forest model
            
    """
    try:
        rand_forest_model=RandomForestClassifier()
        rand_forest_model.fit(X_train_RF, y_train_RF)
        fatal_crash_predictions=rand_forest_model.predict(X_test_RF)
<<<<<<< HEAD
        print("Accuracy:",accuracy_score(y_test_RF, fatal_crash_predictions))
        print("Precision:", precision_score(y_test_RF, fatal_crash_predictions, average="weighted"))
        print("Recall Score:", recall_score(y_test_RF, fatal_crash_predictions, average="weighted"))
=======
        print("Random Forest Accuracy:",accuracy_score(y_test_RF, fatal_crash_predictions))
        print("Random Forest Precision:", precision_score(y_test_RF, fatal_crash_predictions, average="weighted"))
        print("Random Forest Recall Score:", recall_score(y_test_RF, fatal_crash_predictions, average="weighted"))
>>>>>>> test
        return rand_forest_model
    except:
        print("An exception has occured")