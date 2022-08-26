# MacroX
---
## Introduction

The repository contains information and codes for Air_Quality - Economic Progress project

Packages included:- 
1. Fetch_gases_official_IN  
    The notebook contains codes to download data from the official government website for India. More details in the notebook
2. India_Cities.csv  
    The Excel Sheet contains information about the State - City relationship, and the number of stations in each city.
3. India_City_Coordinates.csv  
    Contains the coordinates for India Cities
4. Fetch_Data_API  
    The notebook contains codes to fetch data from OpenweatherMap, average the data daywise and store it in csv format
5. GCS Bucket Link - [GCS](https://console.cloud.google.com/storage/browser/air_quality_macrox?project=macrox01).
    The GCS bucket contains data downloaded for all the above cities in India_Cities.csv. Each folder (City_Name) contains data for all the stations in that city

## Data CleanUp

The pollutants present in the files: 

- SO2 (ug/m3)
- NO2 (ug/m3)
- PM2.5 (ug/m3)
- CO (mg/m3)


The data in the GCS bucket is in the form of an Excel Workbook. For each city, the data can be of two forms
1. One single file containing all the available gases for that station.   
    For Example, the file Delhi/site_11420220824052136.xlsx contains all the labels

2. Two files for the same station - One file containing the NO2 and a second file containing SO2 and PM2.5 data.  
    For Example, the file Agra/site_30720220823002242.xlsx and Agra/site_30720220824231117.xlsx contain NO2 and {PM2.5, SO2} respectively in two different files for the same station
    > Hint: the 6th to 8th character in the file_name contains the station ID. For Example, Agra/site_30720220823002242.xlsx station ID is 307

## Note

- A lot of stations don't have all the gases available.   
 For Example, CO is missing in a lot of stations. Check the official website to fetch CO if it exists
