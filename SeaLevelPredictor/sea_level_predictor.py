import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import matplotlib.lines as mlines
def draw_plot():
    # Read data from file
    df=pd.read_csv('epa-sea-level.csv')
    # Create scatter plot
    plt.scatter(x='Year',y='CSIRO Adjusted Sea Level', data=df,s=[1 for _ in range(len(df['Year']))])
    
    # Create first line of best fit
    res=linregress(df['Year'],df['CSIRO Adjusted Sea Level'])
    x=np.arange(1850.0,2100.0,25)
    y=np.arange(0,res.intercept + res.slope*2100,2)
    plt.plot(x, res.intercept + res.slope*x, 'r')  
    # Create second line of best fit
    df_new=df[df['Year']>2000]
    x_new=np.arange(2000.0,2100.0,25)
    res_new=linregress(df_new['Year'],df_new['CSIRO Adjusted Sea Level'])
    plt.plot(x_new, res_new.intercept + res_new.slope*x_new, '--b')
    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.xticks(x)
    plt.yticks(np.arange(0,res.intercept + res.slope*2200,2))
    line1=mlines.Line2D([], [], color='red', marker='_', markersize=15, label='Line 1')
    line2=mlines.Line2D([], [], color='blue', marker='_', markersize=15, label='Line 2')
    plt.legend(handles=[line1,line2],loc='upper left')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()