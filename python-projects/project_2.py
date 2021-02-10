import pandas as pd

import plotly.express as px
fig =  px.histogram('Dependentes', x = 4)
clients_df = pd.read_csv('python-projects/ClientesBanco.csv', encoding='latin1')
fig.show()