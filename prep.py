# %%

import numpy as np
import pandas as pd

import plotly.express as px
import plotly.io as pio
pio.renderers.default = "plotly_mimetype+notebook"

# %%[markdown]

# ### Time Series Data

# Financial and economic data is mostly displayed and stored as time series. The time series data in the `csv` file is in long format

# %%

# read data
df_prices = pd.read_csv('price_data.csv')
df_prices

# %%

# data in wide format
print('---> csv data in wide form')
df_prices_wide = df_prices.pivot(index='date', columns='stock', values='price')
df_prices_wide

# %%

# the 3 stocks price series diplayed on the same chart
fig1 = px.line(data_frame=df_prices, x='date', y='price', line_group='stock', color='stock', title='Stock Price Series')
fig1.show()

# %%[markdown]

# ### Converting To Return Series & Total Return Series

# It may be difficult to compare the 3 price series above because the starting price is not the same. To overcome this, calculate the return series $r_t$ for a stock and build a price series from a common base value.

# The total return for a stock at time $T$ is defined as 

# $$ TR(T) = 100 \times \Big[ \Pi_{i=1}^{t\leq T}  \big( 1 + r_{t} \big)\Big]$$

# Return at time $t$ is 

# $$ r_t = \frac{p_t - p_{t-1}}{p_{t-1}}$$

# Compare the Total Return series for the 3 stocks

# %%

# convert price series to return series
df_returns = df_prices_wide.pct_change()
df_returns = df_returns.dropna()

# plot - directly going from wide to long form for the plot
fig2 = px.line(data_frame=df_returns.reset_index().melt(id_vars='date'), x='date', y='value', line_group='stock', color='stock', title='Stock Return Series')
fig2.show()

# %%

# calc total return
df_returns = df_returns + 1
df_returns = 100 * df_returns.cumprod()
df_returns

# plot
fig3 = px.line(data_frame=df_returns.reset_index().melt(id_vars='date'), x='date', y='value', line_group='stock', color='stock', title='Stock Total Return Series')
fig3.show()

# %%[markdown]

# ### Questions

# 1. Notice the difference once adjusted to the same reference?
# 2. Which stock or combination would you have chosen?
