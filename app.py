import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utils.helpers import load_data


st.title("Mental Health and Social Media")



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

if __name__ == "__main__":
    main()