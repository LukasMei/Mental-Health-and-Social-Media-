import streamlit as st 
import matplotlib.pyplot as plt
import seaborn as sns

from utils.helpers import load_data, selectbox_widget, show_boxplot, show_histogram, show_scatterplot, slider    


df = load_data()

df = slider(df,"Age")

sex_filter = st.sidebar.multiselect(
    'Geschlecht:',
    options=df['Gender'].unique(),
    default=df['Gender'].unique()
)
df = df[df["Gender"].isin(sex_filter)]

tab1, tab2, tab3, tab4= st.tabs(["Histogramme", "Boxplot", "Korrelationsmatrix", "Scatterplot"])


with tab1:
    feature = selectbox_widget("histogram_widget")

    st.subheader(feature)
    show_histogram(df, feature)

with tab2:
    feature = selectbox_widget("boxplot_widget")
    st.subheader(feature)
    show_boxplot(df, feature)

with tab3:
    st.subheader('Übersicht aller korrelierenden Features')
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    correlation_matrix = df[numeric_cols].corr()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, 
                square=True, linewidths=1, fmt='.2f')
    plt.title('Korrelationsmatrix')
    st.pyplot(fig)

with tab4:
    feature_a = selectbox_widget("feature_a")
    feature_b = selectbox_widget("feature_b")

    st.write("Tipp: Schaue dir die Features Daily Screen Time, Stress Level und Schlafqualität genauer an")
    show_scatterplot(df, feature_a, feature_b)


    



