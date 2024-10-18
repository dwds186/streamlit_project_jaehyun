import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv('train.csv')

st.title('Loan Approval Prediction (JaehyunLee Mini-Project)')

st.header('Dataset Preview')
st.write(data.head())

st.sidebar.header('Visualizations Settings')
visualization_type = st.sidebar.selectbox(
    'Select Visualization Type',
    ['Data Summary', 'Distribution Plot', 'Correlation Heatmap']
)

if visualization_type == 'Data Summary':
    st.subheader('Data Summary')
    st.write(data.describe())
    st.subheader('Loan Status Distribution')
    st.bar_chart(data['loan_status'].value_counts())

elif visualization_type == 'Distribution Plot':
    st.subheader('Distribution of Numeric Features')
    numeric_cols = data.select_dtypes(include=['int64', 'float64']).columns.tolist()
    feature = st.selectbox('Select a feature to plot', numeric_cols)
    fig, ax = plt.subplots()
    sns.histplot(data[feature], kde=True, ax=ax)
    st.pyplot(fig)

elif visualization_type == 'Correlation Heatmap':
    st.subheader('Correlation Heatmap of Features')
    numeric_cols = data.select_dtypes(include=['int64', 'float64']).columns
    corr = data[numeric_cols].corr()

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)