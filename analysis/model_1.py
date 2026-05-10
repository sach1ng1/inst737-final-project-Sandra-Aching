import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score

os.makedirs("data/model_outputs",exist_ok=True)
  

def train_test_split_LR_df():
    """ Trains, tests and splits the loaded data to prepare for logistic regression classification model
        Returns:
            X_train_LR: 
                dataframe for crash model training data 
            X_test_LR: 
                data frame for crash model testing data
            y_train_LR: 
                A series of the injury severity crash model target training data
            y_test_LR: 
                A series of the injury severity crash model target testing data
    """
    try:
        crash_data_encode=pd.read_csv("data/load/Combined_Moco_Crash_Data_Load.csv")
        crash_training=crash_data_encode.copy()
        X=crash_training.drop(columns="injury_severity")
        y=crash_training["injury_severity"]
        X_train_LR, X_test_LR, y_train_LR, y_test_LR= train_test_split(X,y, test_size=0.2, random_state=42)
        return X_train_LR, X_test_LR, y_train_LR, y_test_LR
    except:
        print("An exception has occured")

def classfication_model_LR(X_train_LR, X_test_LR, y_train_LR, y_test_LR):
    """ Creates the logistic regression classification model 
        Parameters:
            X_train_LR: dataframe
                dataframe for crash model training data 
            X_test_LR: dataframe
                data frame for crash model testing data
            y_train_LR: series
                A series of the injury severity crash model target training data
            y_test_LR: series
                A series of the injury severity crash model target testing data
    """
    try:
        log_model=LogisticRegression()
        log_model.fit(X_train_LR, y_train_LR)
        fatal_injury_predictions=log_model.predict(X_test_LR)
        print("Logistic Accuracy:",accuracy_score(y_test_LR, fatal_injury_predictions))
        print("Logistic Precision:", precision_score(y_test_LR, fatal_injury_predictions, average="weighted"))
        print("Logistic Recall Score:", recall_score(y_test_LR, fatal_injury_predictions, average="weighted"))
        # I wanted to create a sid by side dataframe that compares the crash data I fed into the model and then what the results were
        crash_data_results=pd.DataFrame({
            "actual_crash_data":y_test_LR,
            "predicted_crash_data":fatal_injury_predictions
        })
        crash_data_results.to_csv("data/model_outputs/crash_model_prediction_results.csv")
        #I wanted to creatr another dataframe to show how much a predictor like weather or light impacts fatal injury crahses
        predictor_impact=pd.DataFrame({
            "predictor":X_train_LR.columns,
            "coefficient_impact": log_model.coef_[0]
        })
        predictor_impact.to_csv("data/model_outputs/predictor_impact_results.csv")
    except:
        print("An exception has occured")


