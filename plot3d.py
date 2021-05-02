from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
import plotly.express as px

startFile = 'absolute path of 4-degree data set goes here'

colNames = ['x', 'y', 'z', 'id']
colVals = []

with open(startFile, mode='rb') as txtFile:
  fl = txtFile.readlines()
  for l in fl:
    r = l.strip().decode()
    if r == "":
      continue
    r = r.split(' ')
    
    colVals.append(r)

# print(colVals)

# # This is to remove noise
# temp = zip(*colVals)

# temp = [item for item in temp if item[10] != 0] # scatter matrix
temp = [item for item in colVals if item[3] != '0'] # scatter 3D

# Create a DataFrame object
# zip(*list) creates the transpose of the list
# data = pd.DataFrame(colVals, columns=colNames) # this is used when noise is included
data = pd.DataFrame(temp, columns=colNames)

# https://plot.ly/python/3d-scatter-plots/
# The following block is to display 4 dimensions
fig = px.scatter_3d(data, x='x', y='y', z='z', color='id');
fig.show()
print(len(colVals))
print(len(temp))

exit()