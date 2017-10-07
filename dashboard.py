import csv
import pandas as pd
from bokeh.charts import Bar, output_file, show
from bokeh.plotting import figure, output_file, show

def loadDataSet_list():
    with open('bevgeburtenjahrgeschlquartstz.csv','r', encoding='utf8') as f:
      csv_reader = csv.reader(f)
      dataSet = list(csv_reader)
      return dataSet;
  
def loadDataSet_pandas():
    return pd.read_csv("bevgeburtenjahrgeschlquartstz.csv");

def loadPlot1(year):
    dataSet = pd.DataFrame( loadDataSet_pandas())
    dataSet = dataSet[dataSet['StichtagDatJahr'] == year]
    dataSet = dataSet.groupby(['QuarLang', 'SexKurz'])['AnzGebuWir'].sum().reset_index()
    title = 'Aggregated births of Zurich in %d by area' % (year)
    
    bar = Bar(dataSet, values = 'AnzGebuWir', label = 'QuarLang', stack = 'SexKurz', 
            title = title, legend = 'top_right', plot_width = 1000, 
              tooltips = [('Area:', '@QuarLang'), ('Gender:', '@SexKurz'), ('Births:', '@height')])
    show(bar)
    output_file("dashboard.html")
    
def loadPlot2():
    dataSet = pd.DataFrame( loadDataSet_pandas())
    
    dataSet_Female = dataSet[dataSet['SexKurz'] == 'W']
    dataSet_Female = dataSet_Female.groupby(['StichtagDatJahr'])['AnzGebuWir'].sum().reset_index()
    print(dataSet_Female)
    
    dataSet_Male = dataSet[dataSet['SexKurz'] == 'M']
    dataSet_Male = dataSet_Male.groupby(['StichtagDatJahr'])['AnzGebuWir'].sum().reset_index()
    print(dataSet_Male)
    
    dataSet_Total = dataSet
    dataSet_Total = dataSet_Total.groupby(['StichtagDatJahr'])['AnzGebuWir'].sum().reset_index()
    print(dataSet_Total)
    
    x = [1, 2, 3, 4, 5]
    y = [6, 7, 2, 4, 5]
    
    # output to static HTML file
    output_file("lines.html")
    
    # create a new plot with a title and axis labels
    p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')
    
    # add a line renderer with legend and line thickness
    p.line(dataSet_Female['StichtagDatJahr'], dataSet_Female['AnzGebuWir'], legend="females", line_width=2, line_color='blue')
    p.line(dataSet_Male['StichtagDatJahr'], dataSet_Male['AnzGebuWir'], legend="males", line_width=2, line_color='red')
    p.line(dataSet_Total['StichtagDatJahr'], dataSet_Total['AnzGebuWir'], legend="total", line_width=2, line_color='black')
    
    # show the results
    show(p)

    # loadPlot1(2015)
loadPlot2()
