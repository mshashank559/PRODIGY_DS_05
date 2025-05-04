# main.py

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import folium

def load_and_clean_data(input_path, output_path):
    print("Loading data...")
    df = pd.read_csv(input_path, on_bad_lines='skip', encoding='utf-8', engine='python')
    
    print("Initial shape:", df.shape)
    df.dropna(subset=["Start_Time", "Weather_Condition", "Severity", "Start_Lat", "Start_Lng"], inplace=True)
    df['Start_Time'] = pd.to_datetime(df['Start_Time'])
    df['Hour'] = df['Start_Time'].dt.hour
    df['DayOfWeek'] = df['Start_Time'].dt.day_name()

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print("Cleaned data saved. Shape:", df.shape)
    return df


def generate_feature_visuals(df, output_folder):
    print("Generating feature analysis plots...")
    os.makedirs(output_folder, exist_ok=True)

    # Accidents by Day of Week
    plt.figure(figsize=(10, 6))
    sns.countplot(x='DayOfWeek', data=df, order=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], palette='cubehelix')
    plt.title('Accidents by Day of the Week')
    plt.tight_layout()
    plt.savefig(os.path.join(output_folder, 'accidents_by_day.png'))
    plt.close()

    # Severity by Hour
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Hour', y='Severity', data=df, palette='Set2')
    plt.title('Accident Severity by Hour of Day')
    plt.tight_layout()
    plt.savefig(os.path.join(output_folder, 'severity_by_hour.png'))
    plt.close()

    # Top 10 States
    if 'State' in df.columns:
        top_states = df['State'].value_counts().nlargest(10)
        plt.figure(figsize=(10, 6))
        sns.barplot(x=top_states.index, y=top_states.values, palette='flare')
        plt.title('Top 10 States with Most Accidents')
        plt.tight_layout()
        plt.savefig(os.path.join(output_folder, 'top_states.png'))
        plt.close()

def generate_hotspot_map(df, output_path):
    print("Creating hotspot map...")
    map_center = [df['Start_Lat'].mean(), df['Start_Lng'].mean()]
    accident_map = folium.Map(location=map_center, zoom_start=5, tiles='CartoDB positron')

    for _, row in df.sample(min(500, len(df))).iterrows():
        folium.CircleMarker(
            location=[row['Start_Lat'], row['Start_Lng']],
            radius=2,
            color='red',
            fill=True,
            fill_opacity=0.3
        ).add_to(accident_map)

    accident_map.save(output_path)
    print(f"Map saved to {output_path}")

def main():
    raw_path = 'data/US_Accidents_March23.csv'
    cleaned_path = 'Cleaned data/processed_data.csv'
    visual_dir = 'visuals'

    df = load_and_clean_data(raw_path, cleaned_path)
    generate_feature_visuals(df, visual_dir)
    generate_hotspot_map(df, os.path.join(visual_dir, 'hotspot_map.html'))

if __name__ == "__main__":
    main()
