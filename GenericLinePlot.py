import plotly.express as px
import pandas as pd


class GenericLinePlot:
    def __init__(self, title):
        self.title = title

    def plot(self):
        pd.options.plotting.backend = "plotly"
        df = pd.read_csv("data.csv")
        fig = px.line(df, x="date", y=self.title, markers=True)
        fig.write_html(f'templates/{self.title}.html')
