# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 09:33:20 2015

@author: akommajesula
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import train_test_split
from sklearn import metrics
import statsmodels.formula.api as smf

# visualization
import seaborn as sns
import matplotlib.pyplot as plt

# importing the metro ridership date
rider = pd.read_csv('ridership.csv')
rider.columns.values
rider.head()
rider.describe()

#importing weather data. This data only comes in a year so each year has to be downloaded by 
weather2005 = pd.read_csv('http://www.wunderground.com/history/airport/KDCA/2005/1/1/CustomHistory.html?dayend=31&monthend=12&yearend=2005&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1')
weather2005=weather2005.rename(columns={'EST':'Date'})

weather2006 = pd.read_csv('http://www.wunderground.com/history/airport/KDCA/2006/1/1/CustomHistory.html?dayend=31&monthend=12&yearend=2006&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1')
weather2006 = weather2006.rename(columns={'EST':'Date'})

weather2007 = pd.read_csv('http://www.wunderground.com/history/airport/KDCA/2007/1/1/CustomHistory.html?dayend=31&monthend=12&yearend=2007&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1')
weather2007 = weather2007.rename(columns={'EST':'Date'})

weather2008 = pd.read_csv('http://www.wunderground.com/history/airport/KDCA/2008/1/1/CustomHistory.html?dayend=31&monthend=12&yearend=2008&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1')
weather2008 = weather2008.rename(columns={'EST':'Date'})

weather2009 = pd.read_csv('http://www.wunderground.com/history/airport/KDCA/2009/1/1/CustomHistory.html?dayend=31&monthend=12&yearend=2009&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1')
weather2009 = weather2009.rename(columns={'EST':'Date'})

weather2010 = pd.read_csv('http://www.wunderground.com/history/airport/KDCA/2010/1/1/CustomHistory.html?dayend=31&monthend=12&yearend=2010&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1')
weather2010 = weather2010.rename(columns={'EST':'Date'})

weather2011 = pd.read_csv('http://www.wunderground.com/history/airport/KDCA/2011/1/1/CustomHistory.html?dayend=31&monthend=12&yearend=2011&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1')
weather2011 = weather2011.rename(columns={'EST':'Date'})

weather2012 = pd.read_csv('http://www.wunderground.com/history/airport/KDCA/2012/1/1/CustomHistory.html?dayend=31&monthend=12&yearend=2012&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1')
weather2012 = weather2012.rename(columns={'EST':'Date'})

weather2013 = pd.read_csv('http://www.wunderground.com/history/airport/KDCA/2013/1/1/CustomHistory.html?dayend=31&monthend=12&yearend=2013&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1')
weather2013 = weather2013.rename(columns={'EST':'Date'})

weather2014 = pd.read_csv('http://www.wunderground.com/history/airport/KDCA/2014/1/1/CustomHistory.html?dayend=31&monthend=12&yearend=2014&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1')
weather2014 = weather2014.rename(columns={'EST':'Date'})

frames = [weather2005, weather2006, weather2007, weather2008, weather2009, weather2010, weather2011, weather2012, weather2013, weather2014]
#Concatenating all weather data. 
weather = pd.concat(frames)

weather.to_csv('weather.csv')
# Gas prices were available for download as a csv file. 

gas = pd.read_csv('gas.csv')
gas.columns.values
gas.head()
gas.describe()

# Merging all the data together
data=pd.read_csv('data.csv')
data = data.rename(columns={'Mean TemperatureF':'Temp','PrecipitationIn':'Rain'})
data.Rain.fillna(value=0) 
data.Rain.isnull().sum()
data['Weekday']=data.Day.map({'Saturday':0,'Sunday':0,'Monday':1,'Tuesday':1,'Wednesday':1,'Thursday':1,'Friday':1})

#scatter plot using several of the features

sns.pairplot(data, x_vars=['gasprice','Temp','Rain','Weekday','Smartrip'], y_vars='Ridership')

# correlation matrix
data.corr()

# display correlation matrix in Seaborn using a heatmap
sns.heatmap(data.corr())

feature_cols=['gasprice','Temp','Rain','Weekday','Smartrip']
X=data[feature_cols]
y = data.Ridership

linreg = LinearRegression()
linreg.fit(X, y)