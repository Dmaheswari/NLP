import streamlit as st
import pandas as pd
from sentiment_analysis import get_sentiment
from data_loader import load_data
from utils import clean_text
import plotly.express as px

st.title("📊 Sentiment Analysis Dashboard")

uploaded_file = st.file_uploader("TestReviews", type=["csv"])
if uploaded_file:
    df = load_data(uploaded_file)
    df["cleaned"] = df["review"].apply(clean_text)
    df["sentiment"] = df["cleaned"].apply(get_sentiment)

    st.write("### Sample Data", df.head())

    fig = px.histogram(df, x="sentiment", color="sentiment", title="Sentiment Distribution")
    st.plotly_chart(fig)
