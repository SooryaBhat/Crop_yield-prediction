import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Smart Farming Yield Dashboard")

# Load dataset
df = pd.read_csv("Smart_Farming_Crop_Yield_2024.csv")

st.subheader("Dataset Preview")
st.write(df.head())

# Yield Distribution
st.subheader("Yield Distribution")
fig, ax = plt.subplots()
sns.histplot(df['yield_kg_per_hectare'], kde=True, ax=ax)
st.pyplot(fig)

# Crop Analysis
st.subheader("Yield by Crop Type")
crop_avg = df.groupby('crop_type')['yield_kg_per_hectare'].mean()
fig, ax = plt.subplots()
crop_avg.plot(kind='barh', ax=ax)
st.pyplot(fig)

# Region Analysis
st.subheader("Yield by Region")
region_avg = df.groupby('region')['yield_kg_per_hectare'].mean()
fig, ax = plt.subplots()
region_avg.plot(kind='barh', ax=ax)
st.pyplot(fig)

# Disease Impact
st.subheader("Disease Impact")
fig, ax = plt.subplots()
sns.boxplot(x='crop_disease_status', y='yield_kg_per_hectare', data=df, ax=ax)
st.pyplot(fig)

# NDVI
st.subheader("NDVI vs Yield")
fig, ax = plt.subplots()
sns.scatterplot(x='NDVI_index', y='yield_kg_per_hectare', data=df, ax=ax)
st.pyplot(fig)