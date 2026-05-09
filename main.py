from etl.extract import extract_driver_data,extract_incident_data
from etl.transform import read_crash_df, clean_crash_dfs, merge_crash_data, create_eda
from etl.load import read_combined_df, prepare_crash_df
from analysis.model_1 import train_test_split_LR_df, classfication_model_LR
from analysis.model_2 import train_test_split_RF_df, classfication_model_RF
from vis.visualizations import read_model_outputs, static_viz_LR, static_viz_RF
import logging

logger=logging.getLogger(__name__)
def main():
    """
    main calls functions from the extract, transform, load, model_1, model_2, and visualization files
    """
    logging.basicConfig(filename="final_SA_project.log", level=logging.INFO)
    try:
        logger.info("The start of the final project pipeline")
    # calling the raw extracted data from montgomery county gov website using apis
        extract_driver_data()
        extract_incident_data()
        
        #transforming the csv files for analysis
        crash_driver_df, crash_incident_df=read_crash_df()
        new_crash_driver_df, new_crash_incident_df= clean_crash_dfs(crash_driver_df, crash_incident_df)
        crash_driver_incident=merge_crash_data(new_crash_driver_df, new_crash_incident_df)
        create_eda(crash_driver_incident)
        
        # calling in the preprocessing and model for data to be loaded for analysis
        crash_data=read_combined_df()
        crash_data=prepare_crash_df(crash_data)
        
        # performing the logistic regression model
        X_train_LR, X_test_LR, y_train_LR, y_test_LR= train_test_split_LR_df()
        classfication_model_LR(X_train_LR, X_test_LR, y_train_LR, y_test_LR)
        
        #performing the random forest model
        X_train_RF, X_test_RF, y_train_RF, y_test_RF=train_test_split_RF_df()
        rand_forest_model=classfication_model_RF(X_train_RF, X_test_RF, y_train_RF, y_test_RF)
        
        #calling in the visualizations made from the results of Logistic Regresssion Model
        crash_model_results, crash_predictor_results=read_model_outputs()
        static_viz_LR(crash_model_results, crash_predictor_results)
        static_viz_RF(rand_forest_model, X_train_RF.columns)
        logger.info("The end of the final project pipeleine")
    except:
        print("An exception has occured")
    
    
if __name__=="__main__":
    main()
    

