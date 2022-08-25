from nbformat import write
import requests
import json
from datetime import datetime
import pandas as pd

def fetch():
    data=pd.read_csv('India.csv', header=0)
    api_key="Insert api key here"
    # df=pd.DataFrame(columns=['City','Lat','Lng','Date','CO','NO','NO2','O3','SO2','PM2_5','PM10','NH3'])
    data_csv=[]
    for index, rows in data.iterrows():
        # cooridnates=i['BoundingBox Coordinates'].split(',')
        # lat=str(((float(cooridnates[1]))+float((cooridnates[3])))/2)
        # lng=str(((float(cooridnates[0]))+(float(cooridnates[2])))/2)
        lat=str(rows['center1'])
        lng=str(rows['center2'])
        api="https://api.openweathermap.org/data/2.5/air_pollution/history?lat="+lat+"&lon="+lng+"&start=1388636865&end=1658857185&appid="+api_key
        response = requests.get(api)
        output=response.json()
        list=output['list']
        for row in list:
            timestamp=row['dt']
            dt_object = datetime.fromtimestamp(timestamp)
            obj = row['components']
            temp={'City':'Seattle','Lat':lat,'Lng':lng,'Date':dt_object,
            'CO':obj['co'],'NO':obj['no'],'NO2':obj['no2'],'O3':obj['o3'],'SO2':obj['so2'],'PM2_5':obj['pm2_5'],'PM10':obj['pm10'],'NH3':obj['nh3']}
            data_csv.append(temp)
        df=pd.DataFrame(data_csv,columns=['City','Lat','Lng','Date','CO','NO','NO2','O3','SO2','PM2_5','PM10','NH3'])
        df.to_csv(rows['Capital'] + '_raw.csv')
    
def convert():
    data=pd.read_csv('C:/Users/chiku/Desktop/Macro/air_pollution/NY_6_raw.csv',header=0)
    avg_no2=0
    avg_pm=0
    avg_o3=0
    count=1
    df=[]
    data['P']=data.Date.shift(1).fillna(0)
    data['N']=data.Date.shift(-1).fillna(0)
    for index,i in data.iterrows():
        if(i['Date']==i['N']):
            avg_no2=avg_no2+i['NO2']
            avg_o3=avg_o3+i['O3']
            avg_pm=avg_pm+i['PM2_5']
            count=count+1
        else:
            avg_no2=avg_no2+i['NO2']
            print(count)
            temp={'City':i['City'],'Lat':i['Lat'],'Lng':i['Lng'],'Date':i['Date'],
        'NO2':(avg_no2/count),'O3':(avg_o3/count),'PM2_5':(avg_pm/count)}
            df.append(temp)
            avg_no2=0
            avg_pm=0
            avg_o3=0
            count=1
    df=pd.DataFrame(df,columns=['City','Lat','Lng','Date','NO2','O3','PM2_5'])
    df.to_csv('NY_QC.csv')
    
if __name__ == '__main__':
    fetch()
    #convert()