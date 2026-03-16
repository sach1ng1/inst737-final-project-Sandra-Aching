from etl.extract import extract_driver_data,extract_incident_data
from etl.transform_load import read_crash_df, clean_crash_dfs, merge_crash_data, create_eda
from analysis.model_1 import read_combined_df, preprocess_crash_df, train_test_split_df, classfication_model
from vis.visualizations import read_model_outputs, static_viz


def main():
    # calling the raw extracted data from montgomery county gov website using apis
    extract_driver_data()
    extract_incident_data()
    
    #transforming the csv files for analysis
    crash_driver_df, crash_incident_df=read_crash_df()
    new_crash_driver_df, new_crash_incident_df= clean_crash_dfs(crash_driver_df, crash_incident_df)
    crash_driver_incident=merge_crash_data(new_crash_driver_df, new_crash_incident_df)
    create_eda(crash_driver_incident)
    
    # calling in the preprocessing and model for data
    crash_data=read_combined_df()
    crash_data=preprocess_crash_df(crash_data)
    X_train, X_test, y_train, y_test=train_test_split_df(crash_data)
    classfication_model(X_train, X_test, y_train, y_test)
    
    #calling in the visualizations made from the results of model
    crash_model_results, crash_predictor_results=read_model_outputs()
    static_viz(crash_model_results, crash_predictor_results)
    
if __name__=="__main__":
    main()
    

