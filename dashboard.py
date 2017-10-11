# Data Visualisation, HS17
# University of Zurich
# Exercise 1
#
# Author: Nik Zaugg
# Student NUmber: 12-716-734

import csv
import pandas as pd
import numpy as np
from bokeh.charts import Bar, Donut, output_file, show
from bokeh.plotting import figure
from bokeh.layouts import layout, column, row
from bokeh.models import HoverTool, Div
from bokeh.models.sources import ColumnDataSource

###################################FUNCTIONS##########################################

def loadDataSet_list():
    '''Read data from the csv that holds the data.
    '''
    # Use built-in python csv reader
    with open('bevgeburtenjahrgeschlquartstz.csv','r', encoding='utf8') as f:
      csv_reader = csv.reader(f)
      dataSet = list(csv_reader)
      return dataSet;

def loadPlot1(year, width, title_font_size):
    '''Plot stacked bar chart for every area in Zurich
    '''
    # Arrange the dataset
    dataSet = original_data_Set
    
    dataSet = dataSet[dataSet['StichtagDatJahr'] == year]
    dataSet = dataSet.groupby(['QuarLang', 'SexKurz'])['AnzGebuWir'].sum().reset_index()
    dataSet.rename(columns={'QuarLang': 'Area', 'SexKurz': 'Gender', 'AnzGebuWir': 'Number of Births'}, inplace=True)
    title = 'Aggregated births of Zurich in %d by area' % (year)
    
    # Define HoverTool
    hover = HoverTool(
            tooltips=[
                    ('Area:', '@Area'), 
                    ('Gender:', '@Gender'), 
                    ('Births:', '@height')
                    ]
    )
    # Create a Bar glyph
    bar = Bar(dataSet, 
              values = 'Number of Births', 
              label = 'Area', 
              stack = 'Gender',
              title = title, 
              legend = 'top_right',
              plot_width = width,
              plot_height = 500,
              color=['#444C5C', '#CE5A57'],
              tools=[hover])

    # Configure the x and y labels
    bar.xaxis.axis_label= 'Areas in Zurich'
    bar.yaxis.axis_label= 'Number of Births'
    # Configure the font-size of the x and y labels
    bar.xaxis.axis_label_text_font_size = '16px'
    bar.yaxis.axis_label_text_font_size = '18px'
    bar.title.text_font_size = title_font_size
    return bar;

def loadPlot2(height, width, title_font_size):
    '''Plot lines, one for each gender in the dataset and one line for the total
    '''
    # Arrange the dataset
    dataSet = original_data_Set
    
    dataSet_Female = dataSet[dataSet['SexKurz'] == 'W']
    dataSet_Female = dataSet_Female.groupby(['SexKurz','StichtagDatJahr'])['AnzGebuWir'].sum().reset_index()
    sourceFemale = ColumnDataSource(dataSet_Female)
    
    dataSet_Male = dataSet[dataSet['SexKurz'] == 'M']
    dataSet_Male = dataSet_Male.groupby(['SexKurz', 'StichtagDatJahr'])['AnzGebuWir'].sum().reset_index()
    sourceMale = ColumnDataSource(dataSet_Male)

    dataSet_Total = dataSet
    dataSet_Total = dataSet_Total.groupby(['StichtagDatJahr'])['AnzGebuWir'].sum().reset_index()
    sourceTotal = ColumnDataSource(dataSet_Total)
    
    # Create a figure to add the glyphs to
    plot = figure(title="Total births in Zurich between 1993 and 2015", 
               x_axis_label='Year', 
               y_axis_label='Number of Births',
               x_range=[1992,2016], 
               y_range=[0, 5500], 
               plot_height=height, 
               plot_width=width,
               )
    # Configure the font-size of the plot title
    plot.title.text_font_size = title_font_size
    # Configure the font-size and color of the x and y labels and grid lines
    plot.xaxis.axis_label_text_font_size = '16px'
    plot.yaxis.axis_label_text_font_size = '18px'
    plot.xgrid.grid_line_color = None
    plot.ygrid.grid_line_color = None
    
    # Add the line glyphs to the figure
    plot.line('StichtagDatJahr', 'AnzGebuWir', legend="females", line_width=2, line_color='#CE5A57', source=sourceFemale)
    plot.line('StichtagDatJahr', 'AnzGebuWir', legend="males", line_width=2, line_color='#444C5C', source=sourceMale)
    plot.line('StichtagDatJahr', 'AnzGebuWir', legend="total", line_width=2, line_color='black', source=sourceTotal)
    # Add the circle glyphs to the figure
    plot.circle(x='StichtagDatJahr', y='AnzGebuWir',source=sourceFemale, name ='circle', line_color='black', color="white", radius=0.15)
    plot.circle('StichtagDatJahr', 'AnzGebuWir',source=dataSet_Male, name ='circle', line_color='black', color="white", radius=0.15)
    plot.circle('StichtagDatJahr', 'AnzGebuWir',source=dataSet_Total, name ='circle', line_color='black', color="white", radius=0.15)
    
    # Define HoverTool
    hover = HoverTool(
            tooltips=[
                    ("Births: ", "@AnzGebuWir"),
                    ("Year: ", "@StichtagDatJahr")
                    ]
    )
    # Add the HoverTool to the figure
    plot.add_tools(hover)
    plot.legend.location = "top_left"
    
    return plot;

# Bottom-middle plot
def loadPlot3(year, height, width, title_font_size):
    '''Plot donut which depicts the number of births of 2015 according to gender
    '''
    # Arrange the dataset
    dataSet = original_data_Set
    
    dataSet_Female = dataSet[dataSet['SexKurz'] == 'W']
    dataSet_Female = dataSet_Female[dataSet_Female['StichtagDatJahr'] == year]
    dataSet_Female = dataSet_Female.groupby(['SexKurz','StichtagDatJahr'])['AnzGebuWir'].sum().reset_index()
    
    dataSet_Male = dataSet[dataSet['SexKurz'] == 'M']
    dataSet_Male = dataSet_Male[dataSet_Male['StichtagDatJahr'] == year]
    dataSet_Male = dataSet_Male.groupby(['SexKurz', 'StichtagDatJahr'])['AnzGebuWir'].sum().reset_index()
    
    data = pd.Series([dataSet_Male['AnzGebuWir'][0],dataSet_Female['AnzGebuWir'][0]], index = ['Male', 'Female'])
    
    # Create a Donut glyph
    pie_chart = Donut(data, 
                      hover_text='Births',
                      plot_height=height, 
                      plot_width=width, 
                      text_font_size='16pt',
                      color=['#CE5A57','#444C5C'],
                      title="Percentages of births in Zurich 2015",
                      tools="")
            
    pie_chart.title.text_font_size = title_font_size
    return pie_chart;

# Bottom-right plot
def loadPlot4(height, width, title_font_size):
    '''Plot annular_glyphs, filled with the percentage in relation to the zone with the most births
    '''
    # Arrange the dataset
    dataSet = original_data_Set
    dataSet_Area = dataSet[dataSet['QuarLang'] == 'Altstetten']
    dataSet_Area = dataSet_Area[dataSet_Area['StichtagDatJahr'] == 2015]
    dataSet_Area = dataSet_Area.groupby(['StichtagDatJahr','StatZoneLang'])['AnzGebuWir'].sum().reset_index()
    dataSet_Area = dataSet_Area.sort_values(by='AnzGebuWir' ,ascending=0)
    dataSet_Area = dataSet_Area[:][:5]
    dataSet_Area['Percentage'] = dataSet_Area['AnzGebuWir'][:]/dataSet_Area['AnzGebuWir'][0]
    dataSet_Area = dataSet_Area.round(2)    
    dataSet_Area['PercentageString'] = dataSet_Area['Percentage']*100
    dataSet_Area['PercentageString'] = dataSet_Area['PercentageString'].astype(str)
    
    # Configure the Hover Tool to be shown
    hover = HoverTool(
            names=['circle'],
            tooltips=[
            ("Births","@AnzGebuWir")        
            ])
    
    # Create a figure to add the glyphs to
    p = figure(
            plot_width=width, 
            plot_height=height, 
            title="Birth comparison of top 5 Zones in Altstetten", 
            x_range=[0,6.5], 
            y_range=[0,6],
            tools = [hover]
            )
    # Add the wedges to the figure
    p.annular_wedge(
            x=[1,2,3,4,5], 
            y=[5,4,3,2,1], 
            inner_radius=0, 
            outer_radius=0.5,
            start_angle=np.pi/2, 
            end_angle=(np.pi*2)*dataSet_Area['Percentage'] + np.pi/2, 
            color=["rgba(0, 0, 255,1)", "rgba(0, 0, 255,0.8)", "rgba(0, 0, 255,0.6)", "rgba(0, 0, 255,0.4)", "rgba(0, 0, 255,0.2)"], 
            )
    # Add circles to the figure to mark data points
    p.circle(
            name = 'circle',
            radius = 0.1,
            source = dataSet_Area,
            x=[1,2,3,4,5], 
            y=[5,4,3,2,1], 
            color="black", alpha=0.9
            )
    # Add text to the figure for each Zone
    p.text(
            x=[0.8,1.8,2.8,3.8,4.8], 
            y=[5.6,4.6,3.6,2.6,1.6],
            text = dataSet_Area['StatZoneLang'],
            text_font_size = '10pt'
            )
    # Add text to the figure for every percentace
    p.text(
            x=[0.8,1.8,2.8,3.8,4.8], 
            y=[5.1,4.1,3.1,2.1,1.1], 
            text = dataSet_Area['PercentageString']+'%',
            text_font_size = '10pt'
            )
    
    # Set font size of title
    p.title.text_font_size = title_font_size
    return p
    
########################################################################################
# Entry

# Define the name and title of the generated .html file
output_file('dashboard.html', title="Births in Zurich")

# Load original CSV into a DataFrame for later manipulation
original_data_Set = pd.DataFrame(pd.read_csv("bevgeburtenjahrgeschlquartstz.csv"));

# Configure the height, width and font size of the plots
plot_height = 500
plot_width = 500
title_font_size = '10pt'

# Create HTML-tags for title and subtitle
dashboard_title = Div(text= '<div style="text-align: center; margin-top: 40px !important"><h1>Dashboard</h1></div>', width = 3*plot_width)
dashboard_subtitle = Div(text= '<div style="text-align: center; color: grey"><h2>Overview of Births in the Canton of Zurich between 1993 and 2015</h1></div>', width = 3*plot_width)

# Simple HTML-div to add margin between first plot and the following plots
divider_div = Div(text= '<div style="height: 30px"></div>', width = 3*plot_width)

# Load all plots
plot1 = loadPlot1(2015, plot_width*3, title_font_size)
plot2 = loadPlot2(plot_height, plot_width, title_font_size)
plot3 = loadPlot3(2015, plot_height, plot_width, title_font_size)
plot4 = loadPlot4(plot_height, plot_width, title_font_size)

# Arrange the plots before displaying them
dashboard = layout([column([
        row([dashboard_title]),
        row([dashboard_subtitle]),
        row([plot1]),
        row([divider_div]),
        row([plot2, plot3, plot4])
        ])])

# Load the dasboard into the output_file    
show(dashboard)
########################################################################################
