import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Step 1: Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Step 2: Create scatter plot of Year vs Sea Level
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Data Points', color='blue')

    # Step 3: Perform linear regression on all data
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create x-values from 1880 to 2050
    years_extended = pd.Series(range(1880, 2051))
    
    # Calculate predicted y-values
    sea_level_pred = res.slope * years_extended + res.intercept
    
    # Plot best fit line for all data
    plt.plot(years_extended, sea_level_pred, 'r', label='Best Fit Line (1880-2050)')

    # Step 4: Perform linear regression on data from year 2000 onwards
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    
    # Create x-values from 2000 to 2050
    years_recent = pd.Series(range(2000, 2051))
    
    # Calculate predicted y-values for recent data
    sea_level_pred_recent = res_recent.slope * years_recent + res_recent.intercept
    
    # Plot best fit line for recent data
    plt.plot(years_recent, sea_level_pred_recent, 'green', label='Best Fit Line (2000-2050)')

    # Step 5: Customize plot
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()