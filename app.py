import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utils.helpers import load_data


st.title("Mental Health and Social Media")

st.subheader("Thema")
st.write("Einfluss von Social Media auf die Mentale Gesundheit und das allgemeine Wohlbefinden")
st.subheader("Forschungsfrage")
st.write("Können wir die „Happiness“ eines Menschen aus seinem Social-Media- und Lifestyle-Verhalten vorhersagen?")



def main():
    df = load_data()
    col1, col2, col3 = st.columns(3)
    col1.metric("Datensätze", len(df))
    col2.metric("Features", len(df.columns))

    st.subheader('Übersicht')

    st.write(f'Datensatz enthält **{len(df)} Patienten** und **{len(df.columns)} Features**')
    st.dataframe(df.head(10))

    st.subheader('Statistiken')
    st.write(df.describe())


    st.markdown("---")
    st.write("Datenquelle: Social Median and Mental Health Balance Dataset")
    st.write("https://www.kaggle.com/datasets/ayeshaimran123/social-media-and-mental-health-balance")

if __name__ == "__main__":
    main()