'''
Created on 27 août 2017

@author: pierrerobisson
'''
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import seaborn as sns
from scipy import signal
import cufflinks as cf
import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

def matplotlibFunc():
    x = np.linspace(0, 5, 11)
    y = x**2
    '''
    #plt.subplot(1,2,1)
    plt.plot(x,y,'r')
    plt.xlabel('YOLO')
    plt.ylabel('BITE')
    #plt.subplot(1,2,2)
    plt.plot(y,x,'b')
    plt.show()'''
    
    ''''
    fig = plt.figure()
    axes1 = fig.add_axes([0.1,0.1,0.8,0.8])
    axes2 = fig.add_axes([0.15,0.5,0.4,0.4])
    axes1.plot(x,y)
    axes2.plot(y,x)
    plt.show()'''
    
    fig,axes = plt.subplots(nrows=1,ncols=2,figsize=(8,4),dpi = 100)
    for current_axes in axes:
        current_axes.plot(x,y,label='Squared', color='purple')
        current_axes.set_xlabel('YOLO')
        current_axes.set_ylabel('BITE')
        current_axes.set_title('MDr')
        current_axes.set_xlim([0,10])
        current_axes.xaxis.set_major_locator(matplotlib.ticker.MultipleLocator(2))
        current_axes.xaxis.set_minor_locator(matplotlib.ticker.MultipleLocator(0.5))
    axes[1].plot(x,x**3,label='Cubed',linewidth=3,alpha = 0.5, linestyle='--',marker='o')#linewidth = lw, linestyle = ls
    axes[1].legend(loc = 0)
    
    plt.tight_layout() #Eviter les recouvrements
    fig.savefig('picture.pdf')
    plt.show()
    
def seabornFunc():
    tips = sns.load_dataset('tips')
    print(tips.head())
    print(type(tips['total_bill']))
    flights = sns.load_dataset('flights')
    print(flights.head())
    flights = flights.pivot_table(index='month',columns='year',values='passengers')
    print(flights)
    '''Distribution Plot'''
    #sns.distplot(tips['total_bill'],kde=False,bins=30)
    #sns.jointplot(x='total_bill',y='tip',data=tips,kind='resid')
    #sns.pairplot(tips,hue='sex')
    #sns.rugplot(tips['total_bill'])
    
    '''Distribution Plot'''
    #sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.mean)
    #sns.countplot(x='sex', data=tips)
    #sns.boxplot(x='day', y='total_bill',data=tips)
    #sns.violinplot(x='day', y='total_bill',data=tips, hue='sex', split=True)
    #sns.stripplot(x='day', y='total_bill',data=tips, jitter=True, hue='sex', split=True)
    
    #ces deux vont bien ensemble
    #sns.violinplot(x='day',y='total_bill',data=tips)
    #sns.swarmplot(x='day', y='total_bill',data=tips, color='black')
    #sns.factorplot(x='day',y='total_bill',data=tips,kind='violin')
    
    '''Matrix plot'''
    #On a besoin d'une matrice
    tc = tips.corr()
    tc.rename(columns={'size':"yolo"},index={'size':"yolo"},inplace=True)
    print(tc)
    sns.heatmap(data=tc, annot=True, cmap='coolwarm',vmin=0)
    sns.heatmap(data=flights, linewidths=2, yticklabels='auto',annot=True,fmt="d")
    sns.clustermap(data=flights,cmap='coolwarm')
    
    '''Regression plot'''
    #sns.lmplot(x='total_bill',y='tip',data=tips,col='sex',row='time',scatter_kws={'s':50})
    
    '''Grids'''
    #iris = sns.load_dataset('iris')
    #g = sns.PairGrid(iris)
    #g.map_diag(sns.distplot)
    #g.map_lower(sns.kdeplot)
    #g.map_upper(plt.scatter)
    
    #Ca c'est vraiùent cool
    g = sns.FacetGrid(data=tips,col='time',row='sex')
    g.map(sns.distplot, 'total_bill')
    
    sns.despine()
    sns.set_style('darkgrid')
    
    plt.show()

def kdeFunc(sForSeries):
    gaussCourbe = signal.gaussian(51,std=1)
    fig = plt.figure()
    axes1 = fig.add_axes([0.1,0.1,0.9,0.9])
    axes1.plot(gaussCourbe)
    
    plt.show()

def plotlyFunc():
    plotly.tools.set_credentials_file(username='pierrorobis', api_key='Pyr7OYrcBRfGAgH2KwNt')
    cf.go_online()
    
#===============================================================================
#     df = pd.DataFrame(data=np.random.randn(100,4),columns='A B C D'.split())
#     print(df.head())
#     df2 = pd.DataFrame(data={'Category':['A','B','C'],'Value':[32,57,87]})
#     print(df2)
#     df = cf.datagen.lines()
# 
#     df2.iplot(filename='test')
#     
#     df4 = pd.DataFrame({'A':np.arange(100),'B':np.arange(100,0,-1)})
#     df4[['A','B']].iplot(kind='spread',fill=True,opacity=0.8,colorscale='blues',filename='BITCH')
#     
#     df.iplot(kind='hist',opacity=0.7,subplots=True,xTitle='X BIIITCH',yTitle='Y Biiitch',filename='histograms')
#===============================================================================
    
    '''Choropleth'''
    data = dict(type = 'choropleth',
                locations = ['France','Germany','United Kingdom'], #See https://fr.wikipedia.org/wiki/Liste_des_codes_pays_du_CIO, si tu veux utiliser les code de pays style FRA etc...
                locationmode = 'country names',
                colorscale ='Greens',
                text = ['FRANCE', 'ALLEMAGNE', 'ANGLETERRE'],
                marker = dict(line = dict(color = 'rgb(0,220,0', width = 2)),
                z = [1.,2.,3.],
                colorbar = {'title':'titre biitch'})
    layout = dict(geo={'scope':'europe', 'showlakes':True, 'lakecolor':'rgb(20,80,240)'},
                  title='BITE')
    choromap = go.Figure(data = [data],layout = layout)
    py.iplot(choromap)
    
if __name__ == '__main__':
  
    matplotlibFunc()
    seabornFunc()
    #kdeFunc(tips['total_bill'])
    #plotlyFunc()
    
    pass