import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np


st.markdown(
    "<h2 style='text-align: center;'>Model Results</h2>", 
    unsafe_allow_html=True
)

features =  pd.read_csv("features.csv")
features = features.columns.to_list()

importances =  pd.read_csv("importances.csv")
importances = [round(float(num),4) for num in importances.columns.to_list()]

st.markdown(
    "<h2 style='text-align: right;'>Model Accuracy: 0.655</h2>", 
    unsafe_allow_html=True
)


st.subheader("Features importances")


fig, ax = plt.subplots(figsize=(7, 6), dpi=500)

# Sort the indices by importances
indices = np.argsort(importances)

# Plot horizontal bar chart
ax.barh(range(len(indices)), np.array(importances)[indices], color='b', align='center', alpha=0.6)
ax.set_yticks(range(len(indices)))
ax.set_yticklabels([features[i] for i in indices])
ax.set_xlabel('Relative Importance', fontsize=10)

# Display using st.pyplot
st.pyplot(fig)



