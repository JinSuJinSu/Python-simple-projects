import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv(r'C:\Users\Administrator\OneDrive\바탕 화면\fcc-forum-pageviews.txt')
condition1 = df['value'] >= df['value'].quantile(0.025)
condition2 = df['value'] <= df['value'].quantile(0.975)

# Clean data

total_condition = (condition1) & (condition2)
df = df[total_condition].copy()



def draw_line_plot():
    # Draw line plot
    plt.plot(df.index,df.value,color='red')
    date_array=['2016-07','2017-01','2017-07','2018-01','2018-07','2019-01','2019-07','2020-01']

    plt.xticks(np.arange(160, 1300, 160), labels=date_array)
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    plt.figure(figsize=(10,0.7))



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_dates = [2016,2017,2018,2019]
    df_legends = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

    df_bar = None

    # Draw bar plot





    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
