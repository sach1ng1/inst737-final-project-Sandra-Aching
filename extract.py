import pandas as pd
from sodapy import Socrata

def extract_driver_data():
    client = Socrata("data.montgomerycountymd.gov","7Vi9xLbfFtp2Z7lg0Mzs6WMsv")

    results=client.get_all("mmzv-x632")

    crash_driver_data=pd.DataFrame.from_records(results)
    
    crash_driver_data.to_csv("data/Moco_CrashReporting_Driver_data.csv", index=False)
    
    return crash_driver_data

#print(driver_data.head())
#print(driver_data.info())
def extract_incident_data():
    client= Socrata("data.montgomerycountymd.gov","7Vi9xLbfFtp2Z7lg0Mzs6WMsv")
    
    results=client.get_all("bhju-22kf")
    
    crash_incident_data=pd.DataFrame.from_records(results)
    
    crash_incident_data.to_csv("data/Moco_CrashReporting_Incident_data.csv",index=False)
    
    return crash_incident_data





