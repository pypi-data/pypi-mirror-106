import pandas as pd
import matplotlib.pyplot as plt

from .processing import set_dataframe, set_mode
from .charts import Chart
from .modedict import modedict

class vizKG:
  """
  Instantiate vizKG object.
  
  Attributes:
      sparql_query (string): The SPARQL query to retrieve.
      sparql_service_url (string): The SPARQL endpoint URL.
      mode (string): Type of visualization
                     Default = 'Table'
                     Options = {'Table', 'ImageGrid', 'Timeline' 'Graph' 
                                'Map', 'Tree','WordCloud', 'Dimensions',
                                'LineChart', 'BarChart', 'Histogram',
                                'DensityPlot', 'TreeMap' ,'SunBurstChart', 
                                'HeatMap' ,'PieChart', 'DonutChart',
                                'BoxPlot' ,'ViolinPlot', 'AreaChart',
                                'StackedAreaChart', 'ScatterChart', 'BubbleChart'}.
      dataframe (pandas.Dataframe): The data table                 
  """

  def __init__(self, sparql_query, sparql_service_url, mode=None):
      """
      Constructs all the necessary attributes for the vizKG object

      Parameters:
          sparql_query (string): The SPARQL query to retrieve.
          sparql_service_url (string): The SPARQL endpoint URL.
          mode (string): Type of visualization
          dataframe (pandas.Dataframe): The data table
      """

      self.sparql_query = sparql_query
      self.sparql_service_url = sparql_service_url
      self.mode = set_mode(mode)
      self.dataframe = set_dataframe(sparql_query, sparql_service_url)

  def plot(self):
      """
      Plot visualization with suitable corresponding mode

      """
      mode_list = modedict.keys()
      chart = Chart(self.dataframe)
      candidate_visualization = chart.candidate_form()
      figure = None
      if len(self.dataframe) != 0:
        if self.mode not in mode_list:
          print(f"No matching mode found instead use one of the available mode: {candidate_visualization}")
        else:
          try:
            if self.mode in modedict:
              figure = modedict[self.mode](self.dataframe)
          finally:
            figure.plot()
      else:
        print("No matching records found")