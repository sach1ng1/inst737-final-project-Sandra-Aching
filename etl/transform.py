import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("data/transform",exist_ok=True)

def read_crash_df():
    """Read the extracted csv files and saves into new dataframes for preprocessing

    Returns:
        crash_driver_df:
            The extracted dataframe for MOCO crash driver data
        crash_incident_df:
            The extracted dataframe for MOCO crash incident data
    """
    try:    
        crash_driver_df=pd.read_csv("data/extracted/Moco_CrashReporting_Driver_data.csv")
        crash_incident_df=pd.read_csv("data/extracted/Moco_CrashReporting_Incident_data.csv")
        print(crash_driver_df.head())
        print(crash_driver_df.info())
        print(crash_driver_df.describe())
        print(crash_incident_df.head())
        print(crash_incident_df.info())
        print(crash_incident_df.describe())
        return crash_driver_df,crash_incident_df
    except:
        print("An exception has occured")

def clean_crash_dfs(crash_driver_df, crash_incident_df):
    """Cleans the crash dataframes converting data types, and standardizing categories for crash features
    Parameters:
        crash_driver_df:dataframe
            The crash driver dataframe
        crash_incident_df: dataframe
            The crash incident dataframe
        
    Returns:
        new_crash_driver_df: dataframe
            The cleaned crash driver dataframe
        new_crash_incident_df: dataframe
            The cleaned crash incident dataframe
    """
    try:      
        crash_driver_df.columns= [column.strip().lower() for column in crash_driver_df.columns]
        crash_incident_df.columns= [ column.strip().lower() for column in crash_incident_df.columns]
        new_crash_driver_df=crash_driver_df[["report_number", "driver_at_fault", "injury_severity"]]
        new_crash_incident_df=crash_incident_df[["report_number", "acrs_report_type", "crash_date_time", "road_name", "at_fault", "weather", "light", "latitude", "longitude"]]
        new_crash_incident_df["light"]=new_crash_incident_df["light"].str.strip().str.lower()
        new_crash_incident_df["weather"]=new_crash_incident_df["weather"].str.strip().str.lower()
        new_crash_driver_df["injury_severity"]=new_crash_driver_df["injury_severity"].str.strip().str.lower()
        
        new_crash_incident_df["crash_date_time"] = pd.to_datetime(new_crash_incident_df["crash_date_time"])
        new_crash_incident_df["hour_of_day"]=new_crash_incident_df["crash_date_time"].dt.hour
        new_crash_incident_df["day_of_week"]=new_crash_incident_df["crash_date_time"].dt.dayofweek
        
        
        light_categories={
            "dusk": "dusk",
            "daylight":"daylight",
            "dark - lighted": "dark",
            "dawn": "dawn",
            "dark - not lighted": "dark",
            "dark - unknown lighting": "dark",
            "dark no lights": "dark",
            "dark lights on": "dark",
            "dark -- unknown lighting": "dark",
            "unknown": "unknown",
            "other": "other",
            "N/A": "unknown"     
        }
        
        weather_categories={
            "clear": "clear",
            "cloudy": "cloudy",
            "fog, smog, smoke": "foggy",
            "rain": "rainy",
            "freezing rain or freezing drizzle": "winter precip",
            "snow": "winter precip",
            "blowing snow": "winter precip",
            "sleet or hail": "winter precip",
            "severe crosswinds": "windy",
            "blowing sand, soil, dirt": "windy",
            "raining": "rainy",
            "foggy": "foggy",
            "sleet": "winter precip",
            "wintry mix": "winter precip",
            "severe winds": "windy",
            "other": "other",
            "unknown": "unknown",
            "N/A": "unknown"      
        }
        injury_categories={
            "no apparent injury":"nonfatal",
            "possible injury":"nonfatal",
            "suspected serious injury": "nonfatal",
            "fatal injury": "fatal",
            "suspected minor injury": "nonfatal"
            }
        
        new_crash_incident_df["light"]=new_crash_incident_df["light"].replace(light_categories)
        new_crash_incident_df["weather"]=new_crash_incident_df["weather"].replace(weather_categories)
        new_crash_driver_df["injury_severity"]=new_crash_driver_df["injury_severity"].replace(injury_categories)
        return new_crash_driver_df,new_crash_incident_df
    except:
        print("An exception has occured")

def merge_crash_data(new_crash_driver_df, new_crash_incident_df):
    """ Merges the cleaned crash driver dataframe and cleaned crash incident dataframe
    Parameters:
        new_crash_driver_df:dataframe
            The cleaned crash driver dataframe
        new_crash_incident_df: dataframe
            The cleaned crash incident dataframe
        
    Returns:
        crash_driver_incident: dataframe
            The merged dataframe
    """ 
    try:
        crash_driver_incident=pd.merge(new_crash_driver_df,new_crash_incident_df, on="report_number", how="left")
        crash_driver_incident=crash_driver_incident.reset_index(drop=True)
        print(crash_driver_incident.head())
        print(crash_driver_incident.info())
        print(crash_driver_incident["injury_severity"].value_counts(dropna=False))
        print(crash_driver_incident["light"].value_counts(dropna=False))
        print(crash_driver_incident["weather"].value_counts(dropna=False))
        return crash_driver_incident
    except:
        print("An exception has occured")

def create_eda(crash_driver_incident):
    """ Performs EDA plots to understand counts and distribution of crash data
        Parameters:
            crash_driver_incident:dataframe
                The merged crash incident dataframe
    """
    try: 
        plt.figure(figsize=(10,8))
        sns.countplot(data=crash_driver_incident, x="light")
        plt.savefig("data/transform/light_countplot.png")
        plt.show()
        
        plt.figure(figsize=(10,8))
        sns.countplot(data=crash_driver_incident, x="weather")
        plt.savefig("data/transform/weather_countplot.png")
        plt.show()
        
        plt.figure(figsize=(10,8))
        sns.countplot(data=crash_driver_incident, x="hour_of_day")
        plt.savefig("data/transform/hour_of_day_countplot.png")
        plt.show()
        
        plt.figure(figsize=(10,8))
        sns.countplot(data=crash_driver_incident, x="day_of_week")
        plt.savefig("data/transform/day_of_week_countplot.png")
        plt.show()
        
        plt.figure(figsize=(10,8))
        sns.countplot(data=crash_driver_incident, x="injury_severity")
        plt.savefig("data/transform/injury_severity_countplot.png")
        plt.show()
        
        crash_driver_incident.to_csv("data/transform/Combined_Moco_Crash_Driver_Incident.csv",index=False)
        
        
        print("Summary of what I see for merged crash reporting data:")
        print("It seems most crahses have happened during the daylight.")
        print("Crashes have occured it seems mostly in clear weather conditions.")
        print("Crahses have mostly occured between 3pm and 6pm (15:00 and 18:00), decreasing towards the night. There is another peak time range for crashes occuring between 7am and 9am.")
        print("The most crahses during the weekdays have been on Friday (4) with crashes seemingly decreasing in the weekends (5-6).")
    except:
        print("An exception has occured")




    
    
    


    