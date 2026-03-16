import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

os.makedirs("data/model_outputs",exist_ok=True)

def read_combined_df():
    combined_crash_data=pd.read_csv("data/transformed_loaded/Combined_Moco_Crash_Driver_Incident.csv")
    crash_data_encode=combined_crash_data[["injury_severity", "weather", "light", "hour_of_day", "day_of_week"]]
    return crash_data_encode



def preprocess_crash_df(crash_data_encode):
    label_encoders={}
    for column in ["injury_severity", "weather", "light", "hour_of_day", "day_of_week"]:
        le=LabelEncoder()
        crash_data_encode[column]=le.fit_transform(crash_data_encode[column])
        label_encoders[column]= le
    return crash_data_encode

def train_test_split_df(crash_data_encode):
    crash_training=crash_data_encode.copy()
    X=crash_training.drop(columns="injury_severity")
    y=crash_training["injury_severity"]
    X_train, X_test, y_train, y_test= train_test_split(X,y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def classfication_model(X_train, X_test, y_train, y_test):
    log_model=LogisticRegression()
    log_model.fit(X_train, y_train)
    fatal_injury_predictions=log_model.predict(X_test)
    print("Accuracy:",accuracy_score(y_test, fatal_injury_predictions))
    # I wanted to create a sid by side dataframe that compares the crash data I fed into the model and then what the results were
    crash_data_results=pd.DataFrame({
        "actual_crash_data":y_test,
        "predicted_crash_data":fatal_injury_predictions
    })
    crash_data_results.to_csv("data/model_outputs/crash_model_prediction_results.csv")
    #I wanted to creatr another dataframe to show how much a predictor like weather or light impacts fatal injury crahses
    predictor_impact=pd.DataFrame({
        "predictor":X_train.columns,
        "coefficient_impact": log_model.coef_[0]
    })
    predictor_impact.to_csv("data/model_outputs/predictor_impact_results.csv")
    


# crash_data=read_combined_df()
# crash_data=preprocess_crash_df(crash_data)
# X_train, X_test, y_train, y_test=train_test_split_df(crash_data)
# classfication_model(X_train, X_test, y_train, y_test)

