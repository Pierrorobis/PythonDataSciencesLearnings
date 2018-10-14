'''
Created on 2 nov. 2017

@author: pierrerobisson
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas_datareader import data, wb
from datetime import datetime, date, time
import os

def project911():
    df = pd.read_csv("/Users/pierrerobisson/Desktop/Python-Data-Science-and-Machine-Learning-Bootcamp/Data-Capstone-Projects/911.csv")
    print(df.info())
    print(df.head())
    
    #===========================================================================
    # What are the top 5 zipcodes for 911 calls?
    #===========================================================================
    print("--------------Top 5 used zip code--------------")
    print(df["zip"].value_counts().head())
    
    #===========================================================================
    # What are the top 5 townships (twp) for 911 calls?
    #===========================================================================
    print("--------------Top 5 used city--------------")
    print (df["twp"].value_counts().head())
    
    #===========================================================================
    # Take a look at the 'title' column, how many unique title codes are there?
    #===========================================================================
    print("--------------Number of unique title code :--------------")
    #print(df["title"].value_counts().count()) # --> Pas beau !!!
    print(df["title"].nunique())
    #===============================================================================
    # In the titles column there are "Reasons/Departments" specified before the title code. These are EMS, Fire, and Traffic. Use .apply() with a custom lambda expression to create a new column called "Reason" that contains this string value.
    # For example, if the title column value is EMS: BACK PAINS/INJURY , the Reason column value would be EMS.
    #===============================================================================
    df["reason"] = df["title"].apply(lambda title: title.split(":")[0])
    
    #===========================================================================
    # What is the most common Reason for a 911 call based off of this new column?
    #===========================================================================
    print("--------------Number of reasons :--------------")
    print(df["reason"].value_counts())
    
    #===========================================================================
    # Now use seaborn to create a countplot of 911 calls by Reason.
    #===========================================================================
    #===========================================================================
    # sns.countplot(data = df, x="reason")
    # plt.show()
    #===========================================================================
    
    #===============================================================================
    # Now let us begin to focus on time information. What is the data type of the objects in the timeStamp column?
    #===============================================================================
    print("--------------Time data type :--------------")
    print(type(df["timeStamp"].iloc[0]))
    
    #===========================================================================
    # You should have seen that these timestamps are still strings. Use pd.to_datetime 
    # to convert the column from strings to DateTime objects.
    #===========================================================================
    df["timeStamp"] = pd.to_datetime(df["timeStamp"], format="%Y-%m-%d %H:%M:%S", errors="coerce")
    print(list(map(lambda x: x.hour, df["timeStamp"].head())))
    
    #===========================================================================
    # Now that the timestamp column are actually DateTime objects, use .apply() to create 
    # 3 new columns called Hour, Month, and Day of Week. You will create these columns based 
    # off of the timeStamp column, reference the solutions if you get stuck on this step.
    #===========================================================================
    
    import time
    start_time = time.time()

    #---- Cette première solution est beeeaucoup plus lente (2x) que la deuxième, il faut utiliser . apply dès que possible
    print("solution1")
    dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
    df["Hours"] = pd.Series(map(lambda x: x.hour, df["timeStamp"]))
    df["Month"] = pd.Series(map(lambda x: x.month, df["timeStamp"]))
    df["Day of Week"] = pd.Series(map(lambda x: dmap[x.dayofweek], df["timeStamp"]))
    
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    
    print("solution2")
    df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
    df['Month'] = df['timeStamp'].apply(lambda time: time.month)
    df['Day of Week'] = df['timeStamp'].apply(lambda time: dmap[time.dayofweek])
    
    print("--- %s seconds ---" % (time.time() - start_time))
    
    print(df["Day of Week"].head())
    
    #===========================================================================
    # Now use seaborn to create a countplot of the Day of Week column with the hue based off of the Reason column.
    #===========================================================================
    #===========================================================================
    # plt.subplot(1,2,1)
    # sns.countplot(data=df, x="Day of Week", hue="reason")
    #===========================================================================
    
    #===========================================================================
    # Now do the same for Month:
    #===========================================================================
    #===========================================================================
    # plt.subplot(1,2,2)
    # sns.countplot(data=df, x="Month", hue="reason")
    #===========================================================================
    #===========================================================================
    # plt.show()
    #===========================================================================
    
    #===============================================================================
    #     Did you notice something strange about the Plot?
    # You should have noticed it was missing some Months, let's see if we can maybe fill in this 
    # information by plotting the information in another way, possibly a simple line plot that fills 
    # in the missing months, in order to do this, we'll need to do some work with pandas...
    # Now create a groupby object called byMonth, where you group the DataFrame by the month 
    # column and use the count() method for aggregation. Use the head() method on this returned DataFrame.
    #===============================================================================
    print("--------------Group by month :--------------")
    byMonth = df.groupby(by = "Month").count()
    print(byMonth)
    
    #===========================================================================
    # Now create a simple plot off of the dataframe indicating the count of calls per month.
    #===========================================================================
    #===========================================================================
    # plt.plot(byMonth["twp"])
    # sns.lmplot(x="Month",y="twp", data=byMonth.reset_index())#reset index necessaire pour que l'index ne soit plus les mois, mais un index 0, 1, 3...
    # #print(byMonth.reset_index())
    # plt.show()
    #===========================================================================
    
    #===========================================================================
    # Create a new column called 'Date' that contains the date from the timeStamp column. You'll need to use apply along with the .date() method.
    #===========================================================================
    df["Date"] = df["timeStamp"].apply(lambda x: x.date())
    print(df["Date"].head())
    #===========================================================================
    # Now groupby this Date column with the count() aggregate and create a plot of counts of 911 calls
    #===========================================================================
    #===========================================================================
    byDate = df.groupby("Date").count()
    # plt.plot(byDate["twp"])
    # plt.show()
    #===========================================================================
    
    #===========================================================================
    # Now recreate this plot but create 3 separate plots with each plot representing a Reason for the 911 call
    #===========================================================================
    #===========================================================================
    # for reason in df["reason"].value_counts().keys():
    #     byDate2 = df[(df["reason"]==reason)].groupby("Date").count()
    #     plt.plot(byDate2["twp"], label=reason)
    #     print (reason)
    # plt.legend()
    #===========================================================================
    #===========================================================================
    # plt.show()
    #===========================================================================
    
    byDay = df.groupby("Day of Week").count()
    byHours = df.groupby("Hours").count()
    
    df["count"] = 1
    dfDayHours = df.pivot_table(index="Day of Week", columns="Hours", values="count",aggfunc='sum')
    dayHour = df.groupby(by=['Day of Week','Hours']).count()['reason'].unstack()#autre façon de faire équivalente
    print(dayHour-dfDayHours)
    
    #===========================================================================
    # Now create a HeatMap using this new DataFrame.
    #===========================================================================
    #sns.heatmap(dayHour)
    
    #===========================================================================
    # Now create a ClusterMap using this DataFrame.
    #===========================================================================
    #===========================================================================
    # sns.clustermap(dayHour)
    # plt.show()
    #===========================================================================
    
    dayMonth = df.groupby(by=['Day of Week','Month']).count()['reason'].unstack()
    sns.heatmap(dayMonth)
    sns.clustermap(dayMonth)
    plt.show()
def financeLoadData():
    if os.path.exists("/Users/pierrerobisson/Desktop/Python-Data-Science-and-Machine-Learning-Bootcamp/Data-Capstone-Projects/all_banksPR"):
        bank_stocks = pd.read_pickle("/Users/pierrerobisson/Desktop/Python-Data-Science-and-Machine-Learning-Bootcamp/Data-Capstone-Projects/all_banksPR")
        print("Loaded from pickle.")
    else:
        startTime = date(2006,1,1)
        endTime = date(2017,1,1)
    
        tickers = ["BAC","C","GS","JPM","MS","WFC"]
        listBank = []
        for tick in tickers:
            try:
                listBank.append(data.get_data_yahoo(tick, start=startTime, end=endTime))
            except:
                print("Erreur de connection pour la clé : {}".format(tick))
                raise
        
        bank_stocks = pd.concat(listBank,keys=tickers,axis=1)
        bank_stocks.columns.names = ['Bank Ticker','Stock Info']
        bank_stocks.to_pickle("/Users/pierrerobisson/Desktop/Python-Data-Science-and-Machine-Learning-Bootcamp/Data-Capstone-Projects/all_banksPR")
    return bank_stocks

def financeProject():
    bank_stocks = financeLoadData()
    print(bank_stocks.head(1))
    
if __name__ == '__main__':
    #project911()
    financeProject()
    pass