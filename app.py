import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(
    page_title="German Credit", 
    page_icon = "📊",
    layout="wide", 
    initial_sidebar_state="expanded"
)
st.markdown('<style> div.block-container{padding-top:3rem;}</style>', unsafe_allow_html=True)
# Open and resize the image
image = Image.open("scaled.jpg")
resized_image = image.resize((image.width, int(image.height * 0.1)))  # Reduce height by 50%

# Display the resized image
st.image(resized_image, caption="")

st.markdown(
    "<h1 style='text-align: center;'>German Credit Prediction with Random Forest</h1>", 
    unsafe_allow_html=True
)


def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"]::before {
                content: "Menu";
                margin-left: 20px;
                margin-top: 2px;
                font-size: 30px;
                position: relative;
                top: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

add_logo()
st.sidebar.title("")

univariate_page = st.Page("univariate.py", title="Univariate Analysis", icon="📶")
bivariate_page = st.Page("bivariate.py", title="Biariate Analysis", icon="📊")
model_page = st.Page("model.py", title="Model Results", icon="🧮")
predictions_page = st.Page("predictions.py", title="Model Forcasting", icon="🚀")

pg = st.navigation([univariate_page, bivariate_page, model_page, predictions_page])

pg.run()
