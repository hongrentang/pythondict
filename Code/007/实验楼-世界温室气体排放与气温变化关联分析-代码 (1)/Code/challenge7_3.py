# _*_ coding:utf-8 _*_

import pandas as pd
import matplotlib.pyplot as plt

def category_data(df_data,category):
    df_data = df_data[df_data['Series code']==category]
    df_data = df_data.drop(['Country code', 'Country name', 'Series code', 'Series name', 'SCALE', 'Decimals'],axis=1)
    df_data = df_data.replace({'..':pd.NaT})
    df_data = df_data.fillna(method='ffill',axis=1).fillna(method='bfill',axis=1)
    result = df_data.mean()
    return result
    

def climate_plot():
    df_data = pd.read_excel("ClimateChange.xlsx",sheetname='Data')
    co2e = category_data(df_data,'EN.ATM.CO2E.KT')
    meth = category_data(df_data,'EN.ATM.METH.KT.CE')
    noxe = category_data(df_data,'EN.ATM.NOXE.KT.CE')
    ghgo = category_data(df_data,'EN.ATM.GHGO.KT.CE')
    ghgr = category_data(df_data,'EN.CLC.GHGR.MT.CE')

    total_ghg = pd.concat([co2e,meth,noxe,ghgo,ghgr],axis=1).mean(axis=1)
    total_ghg = pd.DataFrame(total_ghg)
    total_ghg.columns = ['Total GHG']


    df_globals = pd.read_excel("GlobalTemperature.xlsx",sheetname='GlobalTemperatures')
    df_globals.index = pd.to_datetime(df_globals['Date'])
    df_globals = df_globals.drop(['Land Max Temperature','Land Min Temperature'],axis=1)
    year_data = df_globals.resample('A').mean()
    year_data = year_data.loc['1990-12-31 00:00:00':'2011-12-31 00:00:00'].set_index(total_ghg.index)
    data = pd.concat([total_ghg,year_data],axis=1)
    data = (data - data.min()) / (data.max() - data.min())
    quarter_data = df_globals.resample('Q').mean()

    fig = plt.figure()
    ax1 = fig.add_subplot(2,2,1)
    ax2 = fig.add_subplot(2,2,2)
    ax3 = fig.add_subplot(2,2,3)
    ax4 = fig.add_subplot(2,2,4)
    a = data.plot(kind='line',ax=ax1)
    b = data.plot(kind='bar',ax=ax2)
    c = quarter_data.plot(kind='area',ax=ax3)
    d = quarter_data.plot(kind='kde',ax=ax4)
    a.set_xlabel('Years')
    a.set_ylabel('Values')
    b.set_xlabel('Years')
    b.set_ylabel('Values')
    c.set_xlabel('Quarters')
    c.set_ylabel('Temperature')
    d.set_xlabel('Values')
    d.set_ylabel('Values')
    plt.show()
    return fig

if __name__ == '__main__':
    print(climate_plot())







