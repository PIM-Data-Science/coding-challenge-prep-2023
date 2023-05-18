# libraries
library(data.table)
library(plotly)
library(dplyr)
library(tidyr)

# read file
dt_prices <- fread("price_data.csv")
dt_prices

# create wide
print("---> csv data in wide form")
dt_prices_wide <- dcast(dt_prices, date ~ stock, value.var = "price")
dt_prices_wide

# plot
fig1 <- plot_ly(dt_prices_wide, type = "scatter", mode = "lines") %>%
    add_trace(x = ~date, y = ~AAPL, name = "AAPL") %>%
    add_trace(x = ~date, y = ~AMZN, name = "AMZN") %>%
    add_trace(x = ~date, y = ~MSFT, name = "MSFT") %>%
    layout(title = "Stock Price Series", yaxis=list(title="price"), width = 1000)

fig1

# check the html or Rmd version of this file for details on the total return series

# Compare the Total Return series for the 3 stocks
dt_returns <- dt_prices_wide %>% 
  mutate(across(!date, ~ .x/lag(.x) -1)) %>% 
  drop_na()
  
fig2 <- plot_ly(dt_returns, type = "scatter", mode = "lines") %>%
    add_trace(x = ~date, y = ~AAPL, name = "AAPL") %>%
    add_trace(x = ~date, y = ~AMZN, name = "AMZN") %>%
    add_trace(x = ~date, y = ~MSFT, name = "MSFT") %>%
    layout(title = "Stock Return Series", yaxis=list(title="returns"), width = 1000)

fig2

# calc total return
dt_cumulative_returns <- dt_returns %>% 
    mutate(across(!date, ~ 100*cumprod(1+.x)))

# plot
fig3 <- plot_ly(dt_cumulative_returns, type = "scatter", mode = "lines") %>%
    add_trace(x = ~date, y = ~AAPL, name = "AAPL") %>%
    add_trace(x = ~date, y = ~AMZN, name = "AMZN") %>%
    add_trace(x = ~date, y = ~MSFT, name = "MSFT") %>%
    layout(title = "Stock Total Return Seriess", yaxis=list(title="returns"), width = 1000)

fig3

# ### Questions

# 1. Notice the difference once adjusted to the same reference?
# 2. Which stock or combination would you have chosen?