import streamlit as st 
import pandas as pd



@st.cache_data
def load_data():
    return pd.read_csv('data/ihr_datensatz_cleaned.csv')


def slider(df, feature):
    if feature in df.columns:
        age_range = st.sidebar.slider(
        f"{feature}:",
        int(df[feature].min()),
        int(df[feature].max()),
        (int(df[feature].min()), int(df[feature].max()))
        )
        df = df[(df[feature] >= age_range[0]) & (df[feature] <=
age_range[1])]
    return df
