"""
Analyzing the dataframe by plotly lib, checking the informations through graphics
"""

import pandas as pd
#importing the clients bank data
clients_df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/ClientesBanco.csv', encoding='latin1')
#deleting the unnecessary columns
clients_df = clients_df.drop('CLIENTNUM', axis = 1)
display(clients_df)

#Checking the dataframe info
display(clients_df.info())

#Deleting all empty elements
clients_df = clients_df.dropna()
display(clients_df.info())

#Describe the values from the df
display(clients_df.describe())

#analyzing the data [any columns] by numbers, or use value_counts(True) to check in %
display(clients_df['Dependentes'].value_counts())

#Analyzing all clients that are canceled and active by the column 'Categoria'
import plotly.express as px
fig =  px.histogram(clients_df,  x = 'Idade', color='Categoria')
fig.show()

#using a repetition FOR to get all graphics using 'Categoria' to differentiate
for coluna in clients_df:
  fig= px.histogram(clients_df, x= coluna, color='Categoria')
  fig.show()