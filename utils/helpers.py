import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



@st.cache_data
def load_data():
    return pd.read_csv('data/ihr_datensatz_cleaned.csv')

@st.cache_data
def load_dirty_data():
    return pd.read_csv('data/Mental_Health_and_Social_Media_Balance_Dataset_dirty.csv')


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


def show_histogram(df, feature):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(df[feature], bins=30, edgecolor='black', color='skyblue')
    ax.set_xlabel(feature, fontsize=12)
    ax.set_ylabel('Häufigkeit', fontsize=12)
    ax.set_title(f'Verteilung von {feature}')
    ax.grid(True, alpha=0.3)
    st.pyplot(fig)

def show_boxplot(df, feature):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(y=df[feature])
    st.pyplot(fig)

def show_scatterplot(df, feature_a, feature_b):
    #numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.scatter(df[feature_a], df[feature_b], alpha=0.5)
    plt.xlabel(feature_a)
    plt.ylabel(feature_b)
    st.pyplot(fig)

def selectbox_widget(unique_key):
    feature = st.selectbox(
        "Wähle ein Feature",
        [
            "Daily_Screen_Time(hrs)",
            "Days_Without_Social_Media",
            "Sleep_Quality(1-10)",
            "Stress_Level(1-10)",
            "Exercise_Frequency(week)",
            "Happiness_Index(1-10)"
        ],
        key=unique_key
    )
    return feature

