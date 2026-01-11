import streamlit as st 
import pandas as pd
from utils.helpers import load_data, slider

df = load_data()


st.sidebar.header("Filter Optionen")

df = slider(df,"Age")
df = slider(df,"Sleep_Quality(1-10)")
df = slider(df,"Daily_Screen_Time(hrs)")
df = slider(df,"Stress_Level(1-10)")
df = slider(df,"Days_Without_Social_Media")
df = slider(df,"Exercise_Frequency(week)")

sex_filter = st.sidebar.multiselect(
    'Geschlecht:',
    options=df['Gender'].unique(),
    default=df['Gender'].unique()
)
df = df[df["Gender"].isin(sex_filter)]


tab1, tab2, tab3 = st.tabs(["📊 Übersicht", "📈 Statistiken", "🔢Rohdaten"])

with tab1:
 col1, col2 = st.columns(2)
 col1.metric("Gefilterte Zeilen", len(df))
 col2.metric("Spalten", len(df.columns))
with tab2:
 st.dataframe(df.describe())
with tab3:
 st.dataframe(df)