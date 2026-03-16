import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

os.makedirs("data/visualizations",exist_ok=True)
def read_model_outputs():
    crash_model_results=pd.read_csv("data/model_outputs/crash_model_prediction_results.csv")
    crash_predictor_results=pd.read_csv("data/model_outputs/predictor_impact_results.csv")
    return crash_model_results, crash_predictor_results

def static_viz(crash_model_results, crash_predictor_results):
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

    

crash_model_results, crash_predictor_results=read_model_outputs()
static_viz(crash_model_results, crash_predictor_results)


# In the future I would like to create some other static visuals, will need to work on other options after
# I will also try to create the respective chaneg log and additional missing parts for part 2 in part 3 due to time contstraints


