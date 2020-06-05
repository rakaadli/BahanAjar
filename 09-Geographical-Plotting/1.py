import chart_studio.plotly as py
import plotly.graph_objects as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
# init_notebook_mode(connected=True)
import pandas as pd
data = dict(type='choropleth',
            locations=['AZ', 'CA', 'NY'],
            locationmode='USA-states',
            colorscale='Portland',
            text=['text1', 'text2', 'text3'],
            z=[1.0, 2.0, 3.0],
            colorbar={'title': 'Colorbar Title'})
layout = dict(geo={'scope': 'usa'})
# choromap = go.Figure(data=[data], layout=layout)
# print here
# iplot(choromap)


df = pd.read_csv('2011_US_AGRI_Exports')
print(df.head())
df['total exports']


data = dict(type='choropleth',
            colorscale='Blues',
            locations=df['code'],
            z=df['total exports'],
            locationmode='USA-states',
            text=df['text'],
            marker=dict(line=dict(color='rgb(255,255,255)', width=2)),
            colorbar={'title': "Millions USD"}
            )


layout = dict(title='2011 US Agriculture Exports by State',
              geo=dict(scope='usa',
                       showlakes=True,
                       lakecolor='rgb(85,173,240)')
              )


# PRINT DISINI
# choromap = go.Figure(data=[data], layout=layout)
# iplot(choromap)

df = pd.read_csv('2014_World_GDP')
df.head()
data = dict(
    type='choropleth',
    locations=df['CODE'],
    z=df['GDP (BILLIONS)'],
    text=df['COUNTRY'],
    colorbar={'title': 'GDP Billions US'},
)
layout = dict(
    title='2014 Global GDP',
    geo=dict(
        showframe=False,
        projection=go.layout.geo.Projection(type='equirectangular')
    )
)

choromap = go.Figure(data=[data], layout=layout)
iplot(choromap)
