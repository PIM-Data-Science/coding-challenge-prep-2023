# %%

import numpy as np
import pandas as pd

import plotly.express as px

# %%[markdown]

# ### Time Series Data

# Financial and economic data is mostly displayed and stored as time series. The time series data in the `csv` file is in long format

# %%

# read data
df_prices = pd.read_csv('price_data.csv')
df_prices

# %%

print('---> csv data in wide form')
df_prices_wide = df_prices.pivot(index='date', columns='stock', values='price')
df_prices_wide


# %%

# the 3 stocks price series diplayed on the same chart
fig1 = px.line(data_frame=df_prices, x='date', y='price', line_group='stock', color='stock', title='Stock Price Series')
fig1.show()

# %%[markdown]

# ### Investing Oversimplified

# Not sure what to say in summary here
