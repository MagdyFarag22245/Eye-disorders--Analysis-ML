# Import Libraries
import numpy as np 
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Importing the dataset
df = pd.read_csv('sources/Eye-disorders-prevalence.csv')

# Analysis:-

# Tab_1  (OverView)

# num.of rows & columns
Total_records = len(df)
num_columns = len(df.columns)

# function using Scatter plot for latitude and longitude using Plotly
def plot_distribution():
    fig = px.scatter(df, x='longitude', y='latitude', color_discrete_sequence=px.colors.qualitative.Set3,
                 title='Spatial Distribution of eye disorders prevalence', labels={'long': 'Longitude', 'lat': 'Latitude'})
    return fig

# function to visualize a map of data
def cluster_map():
    # Combine latitude and longitude into a single array
    coordinates = df[['latitude', 'longitude']].values

    # Perform K-means clustering
    kmeans = KMeans(n_clusters=5, random_state=42)
    cluster_labels = kmeans.fit_predict(coordinates)

    # Visualize the clusters
    fig = px.scatter_mapbox(df, lat='latitude', lon='longitude', color=cluster_labels,
                            color_continuous_scale='Viridis',
                            title='Cluster Analysis of eye disorders prevalence',
                            hover_name='locationdesc',
                            mapbox_style='carto-positron', zoom=2)
    fig.update_layout(margin={'r':0,'t':0,'l':0,'b':0})
    return fig


def plot_correlation_heatmap(figsize=(8, 5), cmap='viridis'):
    """
    Plots a heatmap of the correlation matrix for numeric columns in a DataFrame.

    Parameters:
    - df: pandas DataFrame containing the data.
    - figsize: tuple, size of the figure (default is (10, 8)).
    - cmap: str, colormap for the heatmap (default is 'viridis').

    Returns:
    - None. Displays the heatmap plot.
    """
    # Select numeric columns
    numeric_cols = df.select_dtypes(include=['float64', 'int64'])
    
    # Calculate the correlation matrix
    corr_matrix = numeric_cols.corr()
    
    # Create a heatmap
    plt.figure(figsize=figsize)
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap=cmap, vmin=-1, vmax=1)
    plt.title('Correlation Matrix')
    return plt


# Tab_2  (prevalence)

def plot_data_value_distribution():
    """
    Visualizes the distribution of a specified column using a histogram.

    Parameters:
    - df: DataFrame containing the data.
    - column: The column for which the distribution is to be plotted (default is 'data_value(%)').
    - nbins: Number of bins to use in the histogram (default is 50).
    """
    # Create a histogram for the specified column
    fig = px.histogram(
        df,
        x='data_value(%)',
        color_discrete_sequence=px.colors.qualitative.Set3,
        nbins=50,
        title=f'Distribution of data_value(%)'
    )
    return fig

def plot_mean_prevalence(group_by_column):
    """
    Plots a bar chart of mean prevalence for a given grouping.

    Parameters:
    - group_by_column: The column to group by (e.g., 'locationdesc', 'age', 'raceethnicity', 'gender').
    """
    # Determine the column to group by and set labels and title accordingly
    if group_by_column == 'locationdesc':
        x_label = 'State'
        title = 'Mean Prevalence Across Different States'
    elif group_by_column == 'age':
        x_label = 'Age Group'
        title = 'Mean Prevalence Across Different Age Groups'
    elif group_by_column == 'raceethnicity':
        x_label = 'Race/Ethnicity'
        title = 'Mean Prevalence Across Different Race/Ethnicities'
    elif group_by_column == 'gender':
        x_label = 'Gender'
        title = 'Mean Prevalence Across Different Genders'

    # Calculate the mean prevalence for the specified group
    mean_prevalence = df.groupby(group_by_column, as_index=False)['data_value(%)'].mean()

    # Create a bar chart for mean prevalence
    fig = px.bar(
        mean_prevalence,
        x=group_by_column,
        y='data_value(%)',
        title=title,
        color_discrete_sequence=px.colors.qualitative.Set3,
        labels={group_by_column: x_label, 'data_value(%)': 'Mean Prevalence (%)'}
    )

    # Sort the bars in descending order of mean prevalence
    fig.update_layout(xaxis={'categoryorder': 'total descending'})

    return fig



def plot_box_plot_for_category(specific_category, y_column='data_value(%)', category_column='category'):
    """
    Plots a box plot of the specified y_column for a given specific category.

    Parameters:
    - df: DataFrame containing the data.
    - specific_category: The specific category to plot (e.g., 'Glaucoma', 'Cataract').
    - y_column: The column to plot on the y-axis (default is 'data_value(%)').
    - category_column: The column to filter by for the specific category (default is 'category').
    """

    # Filter data for the specific category
    filtered_df = df[df[category_column] == specific_category]
    
    # Create a box plot
    fig = px.box(
        filtered_df,
        y=y_column,
        title=f'Box Plot of {y_column} for {specific_category}',
        color_discrete_sequence=px.colors.qualitative.Set3
    )
    
    # Update layout with axis titles
    fig.update_layout(
        xaxis_title=f'{category_column}: {specific_category}',
        yaxis_title=y_column
    )
    
    # Show the plot
    return fig


 # Tap_3  (category)

# Count of each eye disorder in the category column
category_counts = df['category'].value_counts().reset_index()
category_counts.columns = ['Category', 'Count']

def plot_eye_disorders(plot_type):
    """
    Generate a plot for eye disorders based on the specified plot type.

    Parameters:
    - category_counts: DataFrame containing 'Category' and 'Count' columns.
    - plot_type: Type of plot to generate ('bar' or 'pie').

    Returns:
    - None: Displays the plot directly.
    """
    if plot_type == 'pie':
        # Create a pie chart
        fig = px.pie(
            category_counts,
            values='Count',
            names='Category',
            title='Proportion of Eye Disorders Categories',
            color_discrete_sequence=px.colors.qualitative.Set3
        )

    elif plot_type == 'bar':
        # Create a bar plot
        fig = px.bar(
            category_counts,
            x='Category',
            y='Count',
            color='Category',
            title='Frequency Distribution of Eye Disorders',
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig.update_layout(
            xaxis_title='Eye Disorder Category',
            yaxis_title='Count'
        )

    # return the plot
    return fig


def eye_disorders_by(groupby_col):
    # Group by the selected column and category to see how the prevalence of different eye disorders varies
    category_counts = df.groupby(['category', groupby_col]).size().reset_index(name='Count')

    if groupby_col == 'age':
        # Stacked Bar Plot: Distribution of Eye Disorders by Age Group
        fig = px.bar(category_counts, x=groupby_col, y='Count', color='category', 
                     title='Distribution of Eye Disorders by Age Group', 
                     barmode='stack', 
                     color_discrete_sequence=px.colors.qualitative.Set3)
        fig.update_layout(xaxis_title='Age Group', yaxis_title='Count')
        return fig

    elif groupby_col == 'gender':
        # Grouped Bar Plot: Distribution of Eye Disorders by Gender
        fig = px.bar(category_counts, x='category', y='Count', color=groupby_col, 
                     title='Distribution of Eye Disorders by Gender', 
                     barmode='group', 
                     color_discrete_sequence=px.colors.qualitative.Set3)
        fig.update_layout(xaxis_title='Eye Disorder Category', yaxis_title='Count')
        return fig
        
    elif groupby_col == 'response':
        # Scatter plot: Prevalence of Eye Disorders by Response
        fig = px.scatter(df, x='data_value(%)', y=groupby_col, color='category', orientation='h',
                         title='Prevalence of Eye Disorders by Response',
                         color_discrete_sequence=px.colors.qualitative.Set3)
        fig.update_layout(xaxis_title='Data Value (%)', yaxis_title='Response')
        return fig


