# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 01:04:32 2021

@author: Robin
"""
""" We are going to do a little python project here for fun. It's based on this 
Youtube video (https://youtu.be/R6CCTuHast0) and involves pandas and plotly. 
We are going to use an API and we are going to plot on a map the actual 
current location of the International Space Station. This is literally just copied"""

import pandas as pd
import plotly.express as px
import plotly.io as pio

# Because spyder (the IDE I use) can't seem to deal with plotly figures 
# we have to show them in browser
pio.renderers.default = "browser"

# Now we are going to read the location of the ISS using this API
url = "http://api.open-notify.org/iss-now.json"
dataframe = pd.read_json(url)
#print(dataframe)

# Let's change the order now of columns to rows
dataframe['latitude'] = dataframe.loc['latitude','iss_position']
dataframe['longitude'] = dataframe.loc['longitude','iss_position']
dataframe.reset_index(inplace=True)
# print(" ")
# print(dataframe)

# Let's get rid of some of the superfluous columns
dataframe = dataframe.drop(['index','message'], axis=1)
# print(" ")
# print(dataframe)

# Now let's illustrate our data by plotting it
fig = px.scatter_geo(dataframe, lat = 'latitude', lon = 'longitude')
fig.show()



