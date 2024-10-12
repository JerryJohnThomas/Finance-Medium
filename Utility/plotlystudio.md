


```
import chart_studio
username='jerryfinance'
api_key='DmH1HMvvHeyFXY06cX69' 
# This is a sample api key, which is no longer working, please generate one
chart_studio.tools.set_credentials_file(username=username,
                                        api_key=api_key)


import chart_studio.plotly as py
import chart_studio.tools as tls
import plotly.express as px

fig = plot_interactive_metric_across_stocks(stock_data, 'Close')
py.plot(fig, filename="FinanceEP01_Close", auto_open = True)

```