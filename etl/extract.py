import pandas as pd
import os
from sodapy import Socrata

os.makedirs("data/extracted",exist_ok=True)

def extract_driver_data():
    """ Extracts crash driver data from Moco government open data portal using an api, documentation can be dfound here: https://dev.socrata.com/foundry/data.montgomerycountymd.gov/mmzv-x632

    Returns:
    crash_driver_data:
    crash driver dataframe that will be used in transform_load 
    """
    try:    
        client = Socrata("data.montgomerycountymd.gov","7Vi9xLbfFtp2Z7lg0Mzs6WMsv",timeout=60)

        results=client.get_all("mmzv-x632")

        crash_driver_data=pd.DataFrame.from_records(results)
        
        crash_driver_data.to_csv("data/extracted/Moco_CrashReporting_Driver_data.csv", index=False)
        
        return crash_driver_data
    except:
        print("An exception has occured")

def extract_incident_data():
    """Extracts crash incident data from moco government open data portal using an api, documentation can be found here:https://dev.socrata.com/foundry/data.montgomerycountymd.gov/bhju-22kf

    Returns:
    crash_incident_data:
    crash incident data that will be used in tansform_load
    
    """
    try:    
        client= Socrata("data.montgomerycountymd.gov","7Vi9xLbfFtp2Z7lg0Mzs6WMsv", timeout=60)
        
        results=client.get_all("bhju-22kf")
        
        crash_incident_data=pd.DataFrame.from_records(results)
        
        crash_incident_data.to_csv("data/extracted/Moco_CrashReporting_Incident_data.csv",index=False)
        
        return crash_incident_data
    except:
        print("An exception has occured")



