import csv
import pandas as pd
from bokeh.charts import Bar, output_file, show

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

loadPlot1(2015)
