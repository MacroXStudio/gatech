# MacroX
---
## Introduction

The repository contains information and code for Air_Quality - Economic Progress project   

Packages included in the repository:- 
1. Fetch_gases_official_IN  
    The notebook contains code to download data from the official government website for India. More details in the notebook
2. India_Cities.csv  
    The Excel Sheet contains information about the State - City relationship, and the number of  air-pollution stations in each city.
3. India_City_Coordinates.csv  
    Contains the coordinates for India Cities
4. Fetch_Data_API  
    The notebook contains code to fetch data from OpenweatherMap, average the data daywise and store it in csv format
5. Accessing_VM.pdf  
    Contains instruction to create/start/stop a VM in gs
6. Air_Quality_Comparison.pptx  
    Plot of initial findigs of gases for some Indian Cities
7. GaTech_Practicum_2022_EconVsClimate.pdf    

## Resources  

1. OpenWeatherMap  
    To access the data from OpenWeatherMap, you need to create a token.  
    The data is free for students for 6 months. (Make sure to use your student email-ID to register) [OpenWeatherMap](https://openweathermap.org/our-initiatives/student-initiative)
2. GCS Bucket Link - [GCS](https://console.cloud.google.com/storage/browser/air_quality_macrox;tab=objects?project=macrox01&prefix=&forceOnObjectsSortingFiltering=false)   
    The GCS bucket contains data downloaded for all the above cities.  
    * satellite_data  
        * CO_India.csv -  Satellite Data for CO2 emission for Indian Cities  
        * NO2_India.csv - Satellite Data for NO2 emission for Indian Cities  
        * SO2_India.csv - Satellite Data for SO2 emission for Indian Cities  
        * blackCarbon_India.csv - Satellite Data for PM emission for Indian Cities  
    * Unemployment_Rate_M_Total.csv - Economic Data of Indian States Month wise  
    * api_data_IN - Folder contains Air Pollution data fetched from the API    
    * official_air_pollution_IN - Folder contains Air Pollution data fetched from the official Indian Govt. website  
3. WHO Air Pollution Article - [WHO](https://www.who.int/health-topics/air-pollution#tab=tab_1)
4. Research_Paper.pdf [Optional] - Reference on how to use Satellite Data

## Accessing Files in GCS

Python code snippet to access any file as a Pandas dataframe from GCS bucket
>import pandas as pd  
>df = pd.read_csv('https://storage.googleapis.com/air_quality_macrox/api_data_IN/Agartala_raw.csv', index_col = 0)  
>df.head()

## Data

The pollutants present in the files under **api_data_IN**:  

- SO2 (ug/m3)
- NO2 (ug/m3)
- PM2.5 (ug/m3)
- CO (ug/m3)

The pollutants present in the files under **official_air_pollution_IN**: 

- SO2 (ug/m3)
- NO2 (ug/m3)
- PM2.5 (ug/m3)
- CO (mg/m3)

## Data Cleanup (Official Air Pollution Data)

The data in the GCS bucket is in the form of an Excel Workbook. For each city, the data can be of two forms
1. One single file containing all the available gases for that station.   
    For Example, the file Delhi/site_11420220824052136.xlsx contains all the labels

2. Two files for the same station - One file containing the NO2 and a second file containing SO2 and PM2.5 data.  
    For Example, the file Agra/site_30720220823002242.xlsx and Agra/site_30720220824231117.xlsx contain NO2 and {PM2.5, SO2} respectively in two different files for the same station
    > Hint: the 6th to 8th character in the file_name contains the station ID. For Example, Agra/site_30720220823002242.xlsx station ID is 307

3. A lot of stations don't have all the gases available.   
    For Example, CO is missing in a lot of stations. Check the official website to fetch CO if it exists
	
## Data Notes

1. NO2 and SO2 satellite data has -1.270000e+30 as the filler value which is used to fill missed or bad measurements. This value should be treated as missing value. Similarly CO satellite data has -9999 as filler value.
2. Below is the graph for CO and NO2 data <b>without</b> replacing filler values.

```
import pandas as pd
import plotly.express as px

df = pd.read_csv('https://storage.googleapis.com/air_quality_macrox/satellite_data/CO_India.csv', index_col = 0, parse_dates = ['date'])
df = df.sort_values(['date'])
fig = px.line(df, x="date", y="Mumbai", title='CO India')
fig.show()

```


![co_india](https://user-images.githubusercontent.com/32074154/191332514-b27438ae-6e91-48b4-82f1-028870530a91.PNG)


 ![no2_india](https://user-images.githubusercontent.com/32074154/191332706-7554254b-fb8a-4c94-af2e-b85a89b576d7.PNG)


After <b>replacing</b> the filler values with None:

```
import pandas as pd
import plotly.express as px

df = pd.read_csv('https://storage.googleapis.com/air_quality_macrox/satellite_data/CO_India.csv', index_col = 0, parse_dates = ['date'])
df = df.replace(-9999.0, 0)
df = df.sort_values(['date'])
fig = px.line(df, x="date", y="Mumbai", title='CO India')
fig.show()
```

![co_none](https://user-images.githubusercontent.com/32074154/191332804-3abff951-3e74-4295-bcf5-b73786dba568.PNG)

![no2_none](https://user-images.githubusercontent.com/32074154/191332851-c5efdc7a-e84d-4ae1-83b9-17109c1f9ef5.PNG)

