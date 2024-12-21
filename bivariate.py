import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt

## Import data

dashboard_data = pd.read_csv("dashboard_data.csv")

def plot_bivariate_histogram(data, variable, target, xlabel, ylabel="frequency", title=""):
    fig = px.histogram(data_frame=data, x=variable, nbins=30, color=target)
    
    fig.update_layout(
         title={
        "text": title,
        "x": 0.5,  
        "xanchor": "center",
    },
    xaxis_title=xlabel,
    yaxis_title=ylabel)
    fig.update_traces(marker=dict(opacity=0.4)) 

    return fig
    

st.markdown(
    "<h2 style='text-align: center;'>Bivariate Analysis</h2>", 
    unsafe_allow_html=True
)



row1_col1, row1_col2 = st.columns(2)

fig1 = plot_bivariate_histogram(data=dashboard_data,
                                variable="Age", target="Risk", 
                                xlabel="Age", ylabel="frequency", title="Age Vs Credit Risk")
row1_col1.plotly_chart(fig1)


fig2 = plot_bivariate_histogram(data=dashboard_data,
                                variable="Credit amount", target="Risk", 
                                xlabel="Credit amount", ylabel="frequency", title="Credit Amount Vs Credit Risk")

row1_col2.plotly_chart(fig2)

row2_col1, row2_col2 = st.columns(2)

fig3 = plot_bivariate_histogram(data=dashboard_data,
                                variable="Duration", target="Risk", 
                                xlabel="Credit Duration (months)", ylabel="frequency", title="Credit Duration Vs Credit Risk")

row2_col1.plotly_chart(fig3)

## Purpose bar plot

fig4 = px.bar(data_frame=dashboard_data, x="Purpose", color="Risk")

fig4.update_layout(
        title={
    "text": "Credit Purpose Vs Credit Risk",
    "x": 0.5,  
    "xanchor": "center",
},
# xaxis_title=xlabel,
# yaxis_title=ylabel
)
fig4.update_traces(marker=dict(opacity=0.4)) 
row2_col2.plotly_chart(fig4)