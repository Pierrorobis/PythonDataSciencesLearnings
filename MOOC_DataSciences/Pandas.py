'''
Created on 26 août 2017

@author: pierrerobisson
'''
import numpy as np
import pandas as pd

if __name__ == '__main__':
    #===========================================================================
    # #Series
    # ser1 = pd.Series(data = np.arange(9), index = np.arange(9,0,-1))
    # ser2 = pd.Series(data = np.arange(9), index = np.arange(9,0,-1))
    # 
    # #DataFrames
    # np.random.seed(101)
    # df = pd.DataFrame(data=np.random.randn(3,3), columns=['a','b','c'], index=['X','Y','Z'])
    # print(df)
    # print(df['a'])
    # print(df[['a','b']])
    # df['new'] = df['c']/0.
    # print(df)
    # df.drop('b',axis=1,inplace=True)#remebebr axis = 0 refers to the index (rows) and axis = 1 refers to the columns
    # df2 = df.drop('X',inplace=False)
    # print(df)
    # print(df2)
    # print(df.loc['X'])
    # print(df.iloc[0])
    # print('-------------------------')
    # print(df.loc[['Y','Z'],['a','c']])
    # print(df[df>0])
    # print(df[(df['c']<0) & (df['a']>0)])
    # print('-------------------------')
    # print('')
    # # Index Levels
    # outside = ['G1','G1','G1','G2','G2','G2']
    # inside = [1,2,3,1,2,3]
    # hier_index = list(zip(outside,inside))
    # print (hier_index)
    # hier_index = pd.MultiIndex.from_tuples(hier_index)
    # print (hier_index)
    # df = pd.DataFrame(data = np.random.randn(6,2), index = hier_index, columns = ['A','B'])
    # df.index.names = ['Groups','Num']
    # print (df)
    # print(df.loc['G1'].loc[3]['A'])
    # print(df.xs(2,level = 'Num'))
    # df.loc['G1'].loc[2]['A'] = np.nan
    # print(df)
    # print(df.dropna(axis = 1))
    # print(df.fillna(df.mean()))
    #===========================================================================
    
    df = pd.read_excel('/Users/pierrerobisson/Desktop/test.xlsx', header=[0,1,2],skiprows=[6,7])
    print(df['A'][1].loc['Outdoor'])
    print('\n')
    print(df)
    df1 = df.iloc[:3].copy()
    print('\n')
    print(dict(df1))
    df2 = df.iloc[5:].copy()
    df2.columns = df2.columns.droplevel(0)
    df2.columns = df2.columns.droplevel(1)
    df2.drop(labels=[3,4],axis=1,inplace=True)
    df2.drop(labels=np.nan,inplace=True)
    print('df2')
    print(df2)