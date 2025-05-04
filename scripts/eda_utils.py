# scripts/eda_utils.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import folium

def run_eda(df):
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='Severity', palette='coolwarm')
    plt.title('Accident Severity Distribution')
    plt.savefig('../visuals/severity_distribution.png')
    plt.close()

    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x='Hour', palette='mako')
    plt.title('Accidents by Hour of Day')
    plt.savefig('../visuals/accidents_by_hour.png')
    plt.close()

def generate_visuals(df):
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, y='Weather_Condition', order=df['Weather_Condition'].value_counts().head(10).index)
    plt.title('Top 10 Weather Conditions During Accidents')
    plt.savefig('../visuals/top_weather_conditions.png')
    plt.close()

    # Heatmap of accident hotspots
    map_center = [df['Start_Lat'].mean(), df['Start_Lng'].mean()]
    accident_map = folium.Map(location=map_center, zoom_start=5)

    for _, row in df.sample(500).iterrows():
        folium.CircleMarker(
            location=[row['Start_Lat'], row['Start_Lng']],
            radius=2,
            color='red',
            fill=True,
            fill_opacity=0.3
        ).add_to(accident_map)

    accident_map.save('../visuals/hotspot_map.html')
