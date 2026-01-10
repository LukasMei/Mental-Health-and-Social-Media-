import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from utils.helpers import load_data    


df = load_data()    

st.header('Visualisierungen')

st.subheader('Verteilung der täglichen Bildschirmzeit')
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(df['Daily_Screen_Time(hrs)'], bins=30, edgecolor='black', color='skyblue')
ax.set_xlabel('Daily Screen Time(hrs)', fontsize=12)
ax.set_ylabel('Häufigkeit', fontsize=12)
ax.set_title('Verteilung der Daily Screen Time')
ax.grid(True, alpha=0.3)
st.pyplot(fig)


st.subheader('Häufigkeit von Tagen ohne Social Media')
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(y=df['Days_Without_Social_Media'])
plt.title('Boxplot von Days_Without_Social_Media')
st.pyplot(fig)


st.subheader('Übersicht aller korrelierenden Features')
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
correlation_matrix = df[numeric_cols].corr()
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
            square=True, linewidths=1, fmt='.2f')
plt.title('Korrelationsmatrix')
st.pyplot(fig)

st.subheader('Beziehung zwischen der täglichen Bildschirmzeit und dem Stress level')
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
fig, ax = plt.subplots(figsize=(10, 6))
plt.scatter(df["Daily_Screen_Time(hrs)"], df["Stress_Level(1-10)"], alpha=0.5)
plt.xlabel('[Daily_Screen_Time(hrs)]')
plt.ylabel('[Stress_Level(1-10)]')
st.pyplot(fig)

st.subheader('Beziehung zwischen der täglichen Bildschirmzeit und der Schlafqualität')
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
fig, ax = plt.subplots(figsize=(10, 6))
plt.scatter(df["Daily_Screen_Time(hrs)"], df["Sleep_Quality(1-10)"], alpha=0.5)
plt.title('Beziehung zwischen [Daily_Screen_Time(hrs)] und [Sleep_Quality(1-10)]')
plt.xlabel('[Daily_Screen_Time(hrs)]')
plt.ylabel('[Sleep_Quality(1-10)]')
st.pyplot(fig)


st.title('Interaktiver Filter 🎛️')
daily_screen_time_filter = st.slider(
    'Bildschirmzeit auswählen:',
    min_value=int(df['Daily_Screen_Time(hrs)'].min()),
    max_value=int(df['Daily_Screen_Time(hrs)'].max()),
    value=(0, 10)  # Standard-Bereich
)

# Daten filtern
filtered_df = df[
    (df['Daily_Screen_Time(hrs)'] >= daily_screen_time_filter[0]) & 
    (df['Daily_Screen_Time(hrs)'] <= daily_screen_time_filter[1])
]

# Ergebnis anzeigen
st.write(f'Zeige **{len(filtered_df)}** von {len(df)} Personen')
st.write(f'Bildschirmzeit zwischen {daily_screen_time_filter[0]} und {daily_screen_time_filter[1]} Stunden')
st.dataframe(filtered_df)
