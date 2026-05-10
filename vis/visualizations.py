import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import plot_tree

os.makedirs("data/visualizations",exist_ok=True)
def read_model_outputs():
    """ 
    Reads the logistic regression model output dataframes
    
        Returns:
            crash_model_results:
                dataframe for the logistic regression model results
            crash_predictor_results:
                dataframe for the logistic regression predictor results       
<<<<<<< HEAD
    """   
    crash_model_results=pd.read_csv("data/model_outputs/crash_model_prediction_results.csv")
    crash_predictor_results=pd.read_csv("data/model_outputs/predictor_impact_results.csv")
    return crash_model_results, crash_predictor_results
=======
    """
    try:   
        crash_model_results=pd.read_csv("data/model_outputs/crash_model_prediction_results.csv")
        crash_predictor_results=pd.read_csv("data/model_outputs/predictor_impact_results.csv")
        return crash_model_results, crash_predictor_results
    except:
        print("An exception has occured")
>>>>>>> test

def static_viz_LR(crash_model_results, crash_predictor_results):
    """ 
    Creates the visualizations of the model results for the logistic regression
    
        Parameters:
            crash__model_results: dataframe
                dataframe for the logistic regression model results
            crash_predictor_results: dataframe
                dataframe for the logistic regression predictor results       
    """ 
<<<<<<< HEAD
    
    plt.figure(figsize=(10,8))
    sns.pairplot(data=crash_model_results[["actual_crash_data","predicted_crash_data"]])
    plt.savefig("data/visualizations/model_pairplot.png")
    plt.show()
    
    
    plt.figure(figsize=(10,8))
    sns.barplot(data=crash_predictor_results, x="predictor", y="coefficient_impact")
    plt.savefig("data/visualizations/model_barplot.png")
    plt.show()
    
    print("Summary of model results:")
    print("light seems to negatively impact crash realted injuries at a coefficient of about -0.25")
    print("day of the week shows a low impact on crash related injury at a coefficeint of about 0.10")

=======
    try:
        plt.figure(figsize=(10,8))
        sns.pairplot(data=crash_model_results[["actual_crash_data","predicted_crash_data"]])
        plt.savefig("data/visualizations/model_pairplot.png")
        plt.show()
        
        
        plt.figure(figsize=(10,8))
        sns.barplot(data=crash_predictor_results, x="predictor", y="coefficient_impact")
        plt.savefig("data/visualizations/model_barplot.png")
        plt.show()
        
        print("Summary of model results:")
        print("light seems to negatively impact crash realted injuries at a coefficient of about -0.25")
        print("day of the week shows a low impact on crash related injury at a coefficeint of about 0.10")
    except:
        print("An exception has occured")
>>>>>>> test
def static_viz_RF(rand_forest_model, feature_names):
    """ 
    Creates the tree plot for the random forest model 
    
        Parameters:
            rand_forest_model: model
                The crash data random forest model 
            feature_names: series
                A series of feature names used in the random forest model
<<<<<<< HEAD
    """ 
    for tree in range(3):
        plt.figure(figsize=(15,20))
        plot_tree(rand_forest_model.estimators_[tree], feature_names=feature_names, filled= True, max_depth=2)
        plt.savefig(f"data/visualizations/random_forest_tree_{tree+1}.png")
        plt.close()

=======
    """
    try: 
        for tree in range(3):
            plt.figure(figsize=(15,20))
            plot_tree(rand_forest_model.estimators_[tree], feature_names=feature_names, filled= True, max_depth=2)
            plt.savefig(f"data/visualizations/random_forest_tree_{tree+1}.png")
            plt.close()

    except:
        print("An exception has occured")
>>>>>>> test
