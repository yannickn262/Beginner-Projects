#imports bokeh and pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

#prepare data
file = pandas.read_csv("http://pythonhow.com/data/bachelors.csv")
x = file["Year"]
y = file["Engineering"]

#output
output_file("Line_from_bachelors.html")

f = figure()
f.line(x,y)
show(f)
