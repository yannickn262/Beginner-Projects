from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

file = pandas.read_excel("http://pythonhow.com/data/verlegenhuken.xlsx", sheet_name = 0)
file["Temperature"] = file["Temperature"]/10
file["Pressure"] = file["Pressure"]/10

output_file("weather.html")
f = figure(plot_width=500,plot_height=400, tools='pan',logo=None)
f.title.text="Weather Data Temp vs Air Pressure"
f.title.text_color="Gray"
f.xaxis.axis_label="Temperature"
f.yaxis.axis_label="Air Pressure"
f.circle(file["Temperature"],file["Pressure"],size=0.5)
show(f)
