import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt


## Import data

dashboard_data = pd.read_csv("dashboard_data.csv")

## plot histogram function
def plot_histogram(data, variable, xlabel, ylabel="frequency", title=""):
    fig = px.histogram(data_frame=data, x=variable, nbins=30)
    
    fig.update_layout(
         title={
        "text": title,
        "x": 0.5,  
        "xanchor": "center",
    },
    xaxis_title=xlabel,
    yaxis_title=ylabel)

    return fig
    
    

st.markdown(
    "<h2 style='text-align: center;'>Univariate Analysis</h2>", 
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

## Target distribution
categories = dashboard_data.Risk.value_counts(normalize=True).index
values = dashboard_data.Risk.value_counts(normalize=True).values
fig = px.pie(
    names=categories,
    values=values,
    hole=0.4  
)
fig.update_layout(
        title={
    "text": "Credit Risk Distribution",
    "x": 0.5,  
    "xanchor": "center",
})
fig.update_traces(textinfo="percent+label")  
fig.update_layout(showlegend=False) 

c1.plotly_chart(fig)




c2.plotly_chart(plot_histogram(dashboard_data, 
                               variable="Age", 
                               xlabel="Age",
                               ylabel="frequency",
                               title="Age Distribution"))

c3.plotly_chart(plot_histogram(dashboard_data, 
                               variable="Credit amount", 
                               xlabel="Credit amount",
                               ylabel="frequency",
                               title="Credit Amount Distribution"))

c4, c5 = st.columns(2)
c4.plotly_chart(plot_histogram(dashboard_data, 
                               variable="Duration", 
                               xlabel="Duration (months)",
                               ylabel="frequency",
                               title="Credit Duration Distribution"))
## bar plot for purpose
fig = px.bar(data_frame=dashboard_data, x="Purpose")

fig.update_layout(
        title={
    "text": "Credit Purpose Distribution",
    "x": 0.5,  
    "xanchor": "center",
},
xaxis_title="Purpose",
yaxis_title="Frequency")

c5.plotly_chart(fig)