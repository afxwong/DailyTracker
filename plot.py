import plotly.express as px
import pandas as pd
import datetime

# fig = px.scatter(x=[1, 2, 3, 4, 5], y=[10, 11, 12, 13, 1])
# fig.write_html("test.html")
pd.options.plotting.backend = "plotly"
df = pd.read_csv("data.csv")
fig = df.plot(x="date", y="happiness")
fig.show()
