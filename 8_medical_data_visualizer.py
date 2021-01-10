import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = df = pd.read_csv(r"C:\Users\Administrator\Desktop\medical.txt")

pd.set_option('display.max_row', 100)
pd.set_option('display.max_columns', 15)

# Add 'overweight' column

df['overweight'] = df['weight']/(df['height']/100)**2

# 1. overweight check
over_weight_check = df['overweight']>25
normal_weight_check = df['overweight']<=25

over_weight_df = df[over_weight_check].copy()
normal_weight_df = df[normal_weight_check].copy()

over_weight_df['overweight'] = 1
normal_weight_df['overweight'] = 0

result_weight_df = pd.concat([over_weight_df,normal_weight_df])
weight_df = result_weight_df[['id','overweight']]

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.


# 2. cholesterol check
over_cholesterol_check = df['cholesterol']>1
normal_cholesterol_check = df['cholesterol']<=1

over_cholesterol_df = df[over_cholesterol_check].copy()
normal_cholesterol_df = df[normal_cholesterol_check].copy()

over_cholesterol_df['cholesterol'] = 1
normal_cholesterol_df['cholesterol'] = 0

result_cholesterol_df = pd.concat([over_cholesterol_df,normal_cholesterol_df])
cholesterol_df = result_cholesterol_df['cholesterol']



# 3. gluc check
over_gluc_check = df['gluc']>1
normal_gluc_check = df['gluc']<=1

over_gluc_df = df[over_gluc_check].copy()
normal_gluc_df = df[normal_gluc_check].copy()

over_gluc_df['gluc'] = 1
normal_gluc_df['gluc'] = 0

result_gluc_df = pd.concat([over_gluc_df,normal_gluc_df])
gluc_df = result_gluc_df['gluc']


# active, alco, smoke and cardio results
# It is just for data merge
active_df = df['active']
alco_df = df['alco']
smoke_df = df['smoke']
cardio_df = df['cardio']


# create a data frame to draw plot
final_df = pd.concat([active_df,alco_df,cholesterol_df,gluc_df,weight_df,smoke_df,cardio_df], axis=1)





# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
   
    df_cat = pd.melt(final_df, id_vars=['id', 'cardio'])
    
    # Draw the catplot with 'sns.catplot()'

    fig = sns.catplot(x="variable", hue="value", col="cardio", data=df_cat, kind="count")

    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = None

    # Calculate the correlation matrix
    corr = None

    # Generate a mask for the upper triangle
    mask = None



    # Set up the matplotlib figure
    fig, ax = None

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig


