#!/usr/bin/env python
import pandas as pd
import plotly.express as px
import plotly.offline as pyo
import plotly.graph_objects as go

# reads the data from the csv file
log_file = "../data.csv"
df = pd.read_csv(log_file)

def figuresToHTML(figs: list[go.Figure], file: str) -> None:
    with open(file, "w", encoding="utf-8") as f:
        f.write("<html><head></head><body>" + "\n")
        add_js = True
        for fig in figs:
            inner_html = pyo.plot(
                fig, include_plotlyjs=add_js, output_type='div'
            )
            f.write(inner_html)
            add_js = False
        f.write("</body></html>")
        
# signal columns:
#   time_s
#   engine_rpm
#   secondary_rpm
#   filtered_engine_rpm
#   filtered_secondary_rpm
#   target_rpm
#   velocity_command
#   velocity_estimate
#   throttle
#   brake

# creates a figure with two lines: engine_rpm and filtered_engine_rpm
fig1 = px.line(df, x="time_s", y=["engine_rpm", "filtered_engine_rpm"])

# creates a figure with one line: secondary_rpm
fig2 = px.line(df, x="time_s", y="secondary_rpm")

# saves fig1 and fig2 to plots.html
figuresToHTML([fig1, fig2], "plots.html")
