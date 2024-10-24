# This file is run before tests. It can act as a notebook to 
# explore data. Matplotlib is supported, as well as Seaborn. 

# import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#import sklearn

# This is used to display any figures you create.
# from renderer import display_fig

# Load the data
df = pd.read_csv("usage_data.csv")

print(df[df.columns[5]].sum())

"""

########
BONEYARD
########

# print(df)

data = {
        "Sessions",
        "Time spent"
        }

df = pd.DataFrame(data)

# Define a dictionary containing employee data
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
 
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
 
# select two columns
df[['Name', 'Qualification']]

df = pd.read_csv("usage_data.csv", skiprows=0, nrows=2)
df.columns.to_list()

print(df)

print(df["Time spent"])

fig, ax = plt.subplots()

The code shown below is here for illustrative purposes, 
you should remove the example and write your own code.
x = np.linspace(0, 10, 1000)
ax.plot(x, np.sin(x))


Use display_fig to render your plots, not plt.show()
display_fig(fig, "Visualization (see notebook.py)")

df = pd.read_csv("usage_data.csv", skiprows=0, ncolumns=4)

"""
