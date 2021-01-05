import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = df = pd.read_csv(r"C:\Users\Administrator\Desktop\medical.txt")



# Add 'overweight' column

df['overweight'] = df['weight']/(df['height']/100)**2


# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.
# 1.actice check
over_active_check = df['active']==1
normal_active_check = df['active']==0

over_active_df = df[over_active_check]
normal_active_df = df[normal_active_check]


# 2.alco check
over_alco_check = df['alco']==1
normal_alco_check = df['alco']==0

over_alco_df = df[over_alco_check]
normal_alco_df = df[normal_alco_check]


# 3. cholesterol check
over_cholesterol_check = df['cholesterol']>1
normal_cholesterol_check = df['cholesterol']<=1

over_cholesterol_df = df[over_cholesterol_check]
normal_cholesterol_df = df[normal_cholesterol_check]

over_cholesterol_df['cholesterol'] = 1
normal_cholesterol_df['cholesterol'] = 0


# 4. gluc check
over_gluc_check = df['gluc']>1
normal_gluc_check = df['gluc']<=1

over_gluc_df = df[over_gluc_check]
normal_gluc_df = df[normal_gluc_check]

over_gluc_df['gluc'] = 1
normal_gluc_df['gluc'] = 0



# 5. overweight check
over_weight_check = df['overweight']>25
normal_weight_check = df['overweight']<=25

over_weight_df = df[over_weight_check]
normal_weight_df = df[normal_weight_check]

over_weight_df['overweight'] = 1
normal_weight_df['overweight'] = 0


# 6. smoke check
over_smoke_check = df['smoke']==1
normal_smoke_check = df['smoke']==0

over_smoke_df = df[over_smoke_check]
normal_smoke_df = df[normal_smoke_check]




# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = None


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the collumns for the catplot to work correctly.
    df_cat = None

    # Draw the catplot with 'sns.catplot()'



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
