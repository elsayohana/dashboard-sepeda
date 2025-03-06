import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Set style seaborn
sns.set(style='darkgrid')

# Load data
all_df = pd.read_csv("dashboard/all_df.csv")

# Sidebar untuk filter
with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    
    # Filter berdasarkan musim dan cuaca
    season_options = all_df['season'].unique() if 'season' in all_df.columns else []
    selected_season = st.multiselect('Pilih Musim', season_options, default=season_options)
    
    weather_options = all_df['weathersit'].unique() if 'weathersit' in all_df.columns else []
    selected_weather = st.multiselect('Pilih Kondisi Cuaca', weather_options, default=weather_options)

    # Filter berdasarkan musim dan cuaca
    main_df = all_df[all_df['season'].isin(selected_season) & all_df['weathersit'].isin(selected_weather)]

# Header utama
st.title("📊 Dashboard Analisis Penyewaan Sepeda")
st.markdown("---")

# Visualisasi pengaruh musim dan cuaca
st.subheader("Pengaruh Musim dan Cuaca terhadap Penyewaan Sepeda")

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x='season', y='cnt', data=main_df, estimator=sum, hue='season', palette='coolwarm', legend=False)
ax.set_title('Total Penyewaan Sepeda Berdasarkan Musim')
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x='weathersit', y='cnt', data=main_df, estimator=sum, hue='weathersit', palette='viridis', legend=False)
ax.set_title('Total Penyewaan Sepeda Berdasarkan Kondisi Cuaca')
st.pyplot(fig)

# Visualisasi pola penyewaan dalam sehari
if 'hr' in main_df.columns:
    st.subheader("Pola Penyewaan Sepeda dalam Sehari")
    hourly_avg = main_df.groupby("hr")["cnt"].mean().reset_index()
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(x='hr', y='cnt', data=hourly_avg, ax=ax)
    ax.set_title('Rata-rata Penyewaan Sepeda dalam Sehari')
    st.pyplot(fig)

# Clustering
if {'temp', 'hum', 'windspeed', 'cnt'}.issubset(main_df.columns):
    st.subheader("Clustering Penyewaan Sepeda")
    features = ["temp", "hum", "windspeed", "cnt"]
    
    # Drop rows dengan NaN pada fitur yang digunakan untuk clustering
    clustering_data = main_df[features].dropna()
    
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(clustering_data)
    
    k = st.slider("Jumlah Klaster (k)", min_value=2, max_value=10, value=3)
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    clusters = kmeans.fit_predict(scaled_data)
    
    # Menambahkan hasil clustering ke DataFrame
    main_df.loc[clustering_data.index, 'cluster'] = clusters
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=main_df['temp'], y=main_df['cnt'], hue=main_df['cluster'], palette='viridis', ax=ax)
    ax.set_title("Hasil Clustering Penyewaan Sepeda")
    st.pyplot(fig)

st.markdown("---")
st.write("Dashboard ini dibuat menggunakan Streamlit untuk analisis data penyewaan sepeda.")
