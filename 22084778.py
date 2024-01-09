# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 15:44:12 2024

@author: jayan
"""

# Import the required libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def process_data(df, series_name, years):
    """
    Process the data for a specific series and years.

    Parameters:
    - df (pd.DataFrame): The input DataFrame containing the data.
    - series_name (str): The name of the series to extract.
    - years (list): List of years to consider.

    Returns:
    - clean_df (pd.DataFrame): Cleaned DataFrame for the specified series.
    - df_t (pd.DataFrame): Transposed DataFrame for the specified series.
    """
    # Select data for the specified series
    data = df[df['Series Name'] == series_name]

    # Drop unnecessary columns and reset the index
    cleaned_data = data.drop(
        ['Country Code', 'Series Code', 'Series Name'], axis=1).reset_index(drop=True)

    # Rename columns with years and transpose the DataFrame
    clean_df = cleaned_data.rename(
        columns={f'{year} [YR{year}]': str(year) for year in years})
    df_t = clean_df.transpose()

    # Set columns to the first row of the transposed DataFrame
    df_t.columns = df_t.iloc[0]

    # Exclude the first row (header) from the DataFrame
    df_t = df_t.iloc[1:]

    # Convert the index to numeric values
    df_t.index = pd.to_numeric(df_t.index)

    # Add a 'Years' column based on the index
    df_t['Years'] = df_t.index

    # Convert all columns to float
    df_t = df_t.apply(lambda x: x.astype(float))

    # Set 'Years' as a separate column in the DataFrame
    df_t['Years'] = df_t.index

    return clean_df, df_t


def lineplot_fig(ax, df, y_label, title):
    """
    Create a line plot for the given DataFrame.

    Parameters:
    - ax (matplotlib.axes._subplots.AxesSubplot): The subplot to plot on.
    - df (pd.DataFrame): The DataFrame to plot.
    - y_label (str): Label for the y-axis.
    - title (str): Title of the plot.

    Returns:
    None
    """
    # Set the seaborn style for a white grid background
    sns.set_style("whitegrid")

    # Plot the line plot for selected countries
    df.plot(x='Years', y=['Australia', 'India', 'United Kingdom', 'Malaysia',
                          'Japan'], xlabel='Years',
            ylabel=y_label, marker='.', ax=ax)

    # Set the title, x-axis label, and y-axis label
    ax.set_title(title)
    ax.set_xlabel('Years')
    ax.set_ylabel(y_label)

    # Set custom x-axis ticks for every 2 years
    ax.set_xticks(range(1998, 2015, 2))

    # Remove legend for the line plot
    ax.legend().set_visible(False)

    # Set the background color of the plot
    ax.set_facecolor('beige')

    # Function to create a dot plot


def dotplot(ax, df, title, y_label):
    """
    Create a dot plot for the given DataFrame.

    Parameters:
    - ax (matplotlib.axes._subplots.AxesSubplot): The subplot to plot on.
    - df (pd.DataFrame): The DataFrame to plot.
    - title (str): Title of the plot.
    - y_label (str): Label for the y-axis.

    Returns:
    None
    """
    # Set the seaborn style for a white grid background
    sns.set_style("whitegrid")

    # Create a point plot for selected countries
    sns.pointplot(x='Years', y='Value', hue='Country', data=df.melt(
        id_vars=['Years'], var_name='Country', value_name='Value'),
        ax=ax)

    # Rotate x-axis labels for better visibility
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90)

    # Set the title and y-axis label
    ax.set_title(title)
    ax.set_ylabel(y_label)

    # Add legend for the dot plot on the left side outside the plot
    ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), facecolor='beige')

    # Set the background color of the plot
    ax.set_facecolor('beige')

# Function to create a pie chart


def pieplot(ax, df, Years, title, autopct='%1.0f%%', fontsize=11):
    """
    Create a pie chart for the given DataFrame.

    Parameters:
    - ax (matplotlib.axes._subplots.AxesSubplot): The subplot to plot on.
    - df (pd.DataFrame): The DataFrame to plot.
    - Years (int): The specific year to consider for the pie chart.
    - title (str): Title of the plot.
    - autopct (str, optional): Format of the percentage labels. Defaults to '%1.0f%%'.
    - fontsize (int, optional): Font size for the percentage labels. Defaults to 11.

    Returns:
    None
    """
    explode = (0.1, 0.1, 0.1, 0.1, 0.1)
    label = ['Australia', 'India', 'United Kingdom', 'Malaysia', 'Japan']
    numeric_df = df.select_dtypes(include=['float64', 'int64'])

    # Create a pie chart for a specific year
    ax.pie(numeric_df[str(Years)], autopct=autopct, labels=label,
           explode=explode, startangle=180,
           wedgeprops={"edgecolor": "black", "linewidth": 2, "antialiased": True})

    # Set the title and background color of the plot
    ax.set_title(title)
    ax.set_facecolor('beige')

# Function to create a bar plot


def barplot_fig(ax, df, x_value, y_value, head_title, x_label, y_label):
    """
    Create a bar plot for the given DataFrame.

    Parameters:
    - ax (matplotlib.axes._subplots.AxesSubplot): The subplot to plot on.
    - df (pd.DataFrame): The DataFrame to plot.
    - x_value (str): Column name for the x-axis.
    - y_value (str or list): Column name(s) for the y-axis.
    - head_title (str): Title of the plot.
    - x_label (str): Label for the x-axis.
    - y_label (str): Label for the y-axis.

    Returns:
    None
    """
    # Set the seaborn style for a white grid background
    sns.set_style('whitegrid')

    # Select data for a specific year and create a bar plot
    bar_df = df[df['Years'].isin([2015])]
    bar_df.plot(x=x_value, y=y_value, kind='bar', title=head_title,
                width=0.65, xlabel=x_label, ylabel=y_label, ax=ax)

    # Add legend to the best location outside the plot
    ax.legend(loc='best', bbox_to_anchor=(1, 0.4), facecolor='beige')

    # Set the background color of the plot
    ax.set_facecolor('beige')

# Function to create a horizontal bar plot


def horizontal_barplot_fig(ax, df, x_value, y_value, head_title, x_label, y_label):
    """
    Create a horizontal bar plot for the given DataFrame.

    Parameters:
    - ax (matplotlib.axes._subplots.AxesSubplot): The subplot to plot on.
    - df (pd.DataFrame): The DataFrame to plot.
    - x_value (str): Column name for the x-axis.
    - y_value (str or list): Column name(s) for the y-axis.
    - head_title (str): Title of the plot.
    - x_label (str): Label for the x-axis.
    - y_label (str): Label for the y-axis.

    Returns:
    None
    """
    # Set the seaborn style for a white grid background
    sns.set_style('whitegrid')

    # Select data for specific years and create a horizontal bar plot
    bar_df = df[df['Years'].isin([2000, 2015])]
    bar_df.plot(x=x_value, y=y_value, kind='barh', title=head_title,
                width=0.65, xlabel=x_label, ylabel=y_label, ax=ax, legend=False)

    # Set the background color of the plot
    ax.set_facecolor('beige')


# Read the CSV file into a DataFrame
df = pd.read_csv('WORLDBANK_INDICATORS.csv')

# Process data for different series
df1, df1_t = process_data(
    df, 'Electricity production from coal sources (% of total)', range(1998, 2016))
df2, df2_t = process_data(
    df, 'Electricity production from natural gas sources (% of total)', range(1998, 2016))
df3, df3_t = process_data(
    df, 'Electricity production from oil sources (% of total)', range(1998, 2016))
df4, df4_t = process_data(
    df, 'Electricity production from renewable sources, excluding hydroelectric (% of total)', range(1998, 2016))
df5, df5_t = process_data(
    df, 'Electricity production from hydroelectric sources (% of total)', range(1998, 2016))

# Create a subplot with 3 rows and 2 columns
fig, axs = plt.subplots(3, 2, figsize=(16, 15), gridspec_kw={
                        'hspace': 0.4}, facecolor='beige')
plt.subplots_adjust(left=0.10, right=0.9, top=0.85, bottom=0.1,
                    wspace=0.2, hspace=0.2)  # Adjusted left

# Plot each graph in its corresponding subplot
lineplot_fig(axs[0, 0], df1_t, 'Percentage (Total %)',
             'Electricity Production from Coal Sources')
dotplot(axs[0, 1], df2_t, 'Electricity Production from Natural Gas Sources',
        'Percentage (Total %)')
pieplot(axs[1, 0], df3, 2010, 'Electricity Production from Oil Sources (2010)')
barplot_fig(axs[1, 1], df4_t, 'Years', ['Australia', 'India', 'United Kingdom', 'Malaysia', 'Japan'],
            'Electricity Production from Renewable Sources,excluding hydroelectric', 'Years', 'Percentage (Total %)')
horizontal_barplot_fig(axs[2, 0], df5_t, 'Years', ['Australia', 'India', 'United Kingdom', 'Malaysia', 'Japan'],
                       'Electricity Production from Hydroelectric Sources', 'Percentage (Total %)', 'Years')

# Remove the empty subplot in the last row and last column
fig.delaxes(axs[2, 1])

# Adding the title to the report within given fontsize
plt.suptitle('Analysis of Global Electricity Production Trends (1998-2015)', fontsize=26, y=0.89,
             color='black', fontweight='bold', ha='center', va='center', backgroundcolor='lightyellow')

# Adding the report within the code along with name and student Id
report_text = """
    The analysis of electricity production trends from 1998 to
    2015 reveals significant shifts in energy sources for selected
    countries. Notably, coal-based production witnessed a decline,
    with Australia leading in renewable energy adoption, reaching
    62.4% in 2015. In 2005, natural gas played a substantial role,
    with Malaysia showing the highest percentage at 70.2%. The pie
    chart showcases the diversity in oil-based electricity production
    in 2010, with Japan leading at 43%. Additionally,
    the horizontal bar plot illustrates the prominence of 
    hydroelectric sources in 2000, especially in India 13.2% and Malaysia 10%.
    Renewable sources, excluding hydroelectric, witness a positive trajectory,
    with United Kingdom displaying a remarkable increase more then 20%. 
    Overall, these visualizations underscore the global trajectory 
    towards sustainable energy practices and highlight the unique 
    contributions of each country to this pivotal transition.
    
                                                        Name: Jaya Navya
                                                        Student id: 22084778
"""
fig.text(0.55, 0.02, report_text, ha='left',
         va='bottom', fontsize=14, color='black')

# Adjust layout for better spacing
plt.tight_layout()

# Save the combined plot as an image
#plt.savefig('22084778.png', dpi=300)
plt.show()

