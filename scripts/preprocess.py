import pandas as pd

def load_and_clean_data(filepath):
    df = pd.read_csv(filepath)

    # Drop rows with missing critical info
    df.dropna(subset=["Start_Time", "Weather_Condition", "Severity", "Start_Lat", "Start_Lng"], inplace=True)

    # Convert time columns
    df['Start_Time'] = pd.to_datetime(df['Start_Time'])
    df['Hour'] = df['Start_Time'].dt.hour
    df['DayOfWeek'] = df['Start_Time'].dt.day_name()

    return df
