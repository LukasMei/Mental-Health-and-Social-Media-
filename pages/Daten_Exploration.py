import streamlit as st 
import pandas as pd
from utils.helpers import load_data

df = load_data()


tab1, tab2, tab3 = st.tabs(["📊 Übersicht", "📈 Statistiken", "🔢Rohdaten"])

with tab1:
 col1, col2 = st.columns(2)
 col1.metric("Gefilterte Zeilen", len(df))
 col2.metric("Spalten", len(df.columns))
with tab2:
 st.dataframe(df.describe())
with tab3:
 st.dataframe(df)