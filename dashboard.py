import csv
import pandas as pd
from bokeh.charts import Bar, Donut, output_file, show
from bokeh.plotting import figure
from bokeh.layouts import layout, gridplot
from bokeh.models import HoverTool
from bokeh.models.sources import ColumnDataSource

output_file('dashboard.html')
original_data_Set = pd.DataFrame(pd.read_csv("bevgeburtenjahrgeschlquartstz.csv"));

def loadDataSet_list():
    with open('bevgeburtenjahrgeschlquartstz.csv','r', encoding='utf8') as f:
      csv_reader = csv.reader(f)
      dataSet = list(csv_reader)
      return dataSet;

def loadPlot1(year):
    dataSet = original_data_Set
    dataSet = dataSet[dataSet['StichtagDatJahr'] == year]
    dataSet = dataSet.groupby(['QuarLang', 'SexKurz'])['AnzGebuWir'].sum().reset_index()
    title = 'Aggregated births of Zurich in %d by area' % (year)
    
    bar = Bar(dataSet, values = 'AnzGebuWir', 
              label = 'QuarLang', 
              stack = 'SexKurz', 
              title = title, 
              legend = 'top_right', 
              plot_width = 1800, 
              tooltips = [('Area:', '@QuarLang'), ('Gender:', '@SexKurz'), ('Births:', '@height')])
    return bar;
    
def loadPlot2():
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
    
    # create a new plot with a title and axis labels
    p = figure(title="simple line example", x_axis_label='X-Axis Label', y_axis_label='Y-Axis Label', plot_height=400, plot_width=400,)
    
    # add a line renderer with legend and line thickness
    p.line('StichtagDatJahr', 'AnzGebuWir', legend="females", line_width=2, line_color='blue', source=sourceFemale)
    p.line('StichtagDatJahr', 'AnzGebuWir', legend="males", line_width=2, line_color='red', source=sourceMale)
    p.line('StichtagDatJahr', 'AnzGebuWir', legend="total", line_width=2, line_color='black', source=sourceTotal)
    
    hover = HoverTool(
            tooltips=[
                    ("Births: ", "@AnzGebuWir"),
                    ("Year: ", "@StichtagDatJahr"),
                    #("Gender: ", "@SexKurz")
                    ]
    )
    p.add_tools(hover)
    p.legend.location = "top_left"
    
    return p;

def loadPlot3(year):
    dataSet = original_data_Set
    
    dataSet_Female = dataSet[dataSet['SexKurz'] == 'W']
    dataSet_Female = dataSet_Female[dataSet_Female['StichtagDatJahr'] == year]
    dataSet_Female = dataSet_Female.groupby(['SexKurz','StichtagDatJahr'])['AnzGebuWir'].sum().reset_index()
    
    dataSet_Male = dataSet[dataSet['SexKurz'] == 'M']
    dataSet_Male = dataSet_Male[dataSet_Male['StichtagDatJahr'] == year]
    dataSet_Male = dataSet_Male.groupby(['SexKurz', 'StichtagDatJahr'])['AnzGebuWir'].sum().reset_index()
    
    data = pd.Series([dataSet_Male['AnzGebuWir'][0],dataSet_Female['AnzGebuWir'][0]], index = ['Male', 'Female'])
    pie_chart = Donut(data, hover_text='Births', plot_height=600, plot_width=600,)
    return pie_chart;

def loadPlot4(year):
    dataSet = original_data_Set
    
    dataSet_Female = dataSet[dataSet['SexKurz'] == 'W']
    dataSet_Female = dataSet_Female[dataSet_Female['StichtagDatJahr'] == year]
    dataSet_Female = dataSet_Female.groupby(['SexKurz','StichtagDatJahr'])['AnzGebuWir'].sum().reset_index()
    
    dataSet_Male = dataSet[dataSet['SexKurz'] == 'M']
    dataSet_Male = dataSet_Male[dataSet_Male['StichtagDatJahr'] == year]
    dataSet_Male = dataSet_Male.groupby(['SexKurz', 'StichtagDatJahr'])['AnzGebuWir'].sum().reset_index()
    
    data = pd.Series([dataSet_Male['AnzGebuWir'][0],dataSet_Female['AnzGebuWir'][0]], index = ['Male', 'Female'])
    pie_chart = Donut(data, hover_text='Births', plot_height=600, plot_width=600,)
    return pie_chart;


l = layout([
loadPlot1(2015)],[
loadPlot2(),
loadPlot3(2015),
loadPlot4(2015)]
#sizing_mode='stretch_both'
)

show(l)
    
