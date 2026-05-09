# inst737-final-project-Sandra-Aching
# Project Overview
## Business Problem 
There lacks insight into what factors like age, road condition or weather contribute to severe fatal crash incidents which can help to support the Montgomery County Vision Zero plan to help eliminate severe to fatal crash incidents in the county roads.

## Data
In order to conduct this predictive analysis, I will use crash incident and crash driver data from Montgomery County, Maryland. Montgomery County has a public open data portal that gives access to different types of data available from the county.
## Crash Reporting Incidents Data
This dataset contains crash incident data from Montgomery County, Maryland:
https://data.montgomerycountymd.gov/Public-Safety/Crash-Reporting-Incidents-Data/bhju-22kf/about_data
## Crash Reporting Drivers Data
This dataset contains driver data from crash incidents in Montgomery County, Maryland
https://data.montgomerycountymd.gov/Public-Safety/Crash-Reporting-Drivers-Data/mmzv-x632/about_data 

# Techniques Employed
Using Python with libraries like pandas, sci-kit learn, matplotlib among other libraries to perform EDA, transformation and model training for my final project analysis.

# Project Setup Instructions
First please clone the project repository and the directory:
```
   git clone https://github.com/sach1ng1/inst737-final-project-Sandra-Aching.git
   cd inst737-final-project-Sandra-Aching
```
Then, please activate the virtual environment:

```python -m venv crvenv
   source crvenv/bin/activate
```

Finally, please also setup the corresponding dependencies:

```pip install -r requirements.txt 
```

Now you are able to run the project code package from the main.py:

```python main.py 
```

# Code Structure

The following is the project code package structure:

```
inst737-final-project-Sandra-Aching/
├── data/
│   ├── extracted/   -> contains the raw csv files extracted from the moco open data portal 
│   ├── transformed/ -> contains the transformed and combined crash data csv file
│   ├── load/        -> contains the csv file with crash feature encoded for analysis
│   ├── model_outputs/ -> contains the results from the model analysis
│   ├── visualizations/ -> contains the visualizations from model
│   ├── reference-tables/ -> contains data dictionaries and encoding reference file
├── etl/
│   ├── extract.py   -> extracts the raw data from moco open data portal 
│   ├── transform.py -> cleans and transforms the crash data
│   ├── load.py      -> prepares the data for loading to analysis
├── analysis/
│   ├── model_1.py   -> performs the logistic regression model
│   ├── model_2.py   -> performs the random forest model
├── vis/
│   ├── visualizations.py -> creates visualizations from the models
├── final_SA_project.log  -> stores the pipeline log
├── main.py               -> runs the pipeline  
├── README.md             -> contains project overview and information
├── requirements.txt.     -> contains the dependencies
```



