# US Traffic Accident Analysis

## 📊 Project Overview

This project explores and analyzes the **US Traffic Accidents (March 2023)** dataset using Python and Power BI. It performs data cleaning, feature engineering, exploratory data analysis (EDA), and creates visualizations including an interactive accident hotspot map and a professional Power BI dashboard. The goal is to uncover patterns and trends in accidents across different times and locations.

---

## 📁 Project Structure

```
US_Traffic_Accident_Analysis/
├── data/
│   └── US_Accidents_March23.csv         # Original dataset
├── Cleaned data/
│   └── processed_data.csv               # Cleaned dataset
├── visuals/
│   ├── accidents_by_day.png             # Day-wise accident plot
│   ├── severity_by_hour.png             # Hour-wise severity plot
│   ├── top_states.png                   # Top 10 states by accident count
│   └── hotspot_map.html                 # Interactive map
├── notebooks/
│   ├── 01_Data_Cleaning_and_Exploration.ipynb
│   ├── 02_Feature_Analysis.ipynb
│   └── 03_Hotspot_Visualization.ipynb
├── main.py                              # Master script to run the project
├── US_Traffic_Accident_Insights.pbix    # Power BI Dashboard file
└── README.md                            # Project documentation
```

---

## ⚙️ Features Implemented

* Cleaned missing values in key columns
* Extracted time-based features (hour, day of week)
* Visualized accident trends by:

  * Day of week
  * Hour of day
  * State-wise frequency
* Mapped top hotspots using **Folium**
* Developed a comprehensive Power BI dashboard

---

## 📦 Requirements

Install dependencies using:

```bash
pip install pandas matplotlib seaborn folium
```

---

## 🚀 How to Run

```bash
# Run the full pipeline
python main.py
```

This will:

* Load and clean the dataset
* Generate and save EDA visualizations
* Create an interactive hotspot map

---

## 📍 Power BI Dashboard: US Traffic Accident Insights

### Dashboard Features

* KPI Cards: Total Accidents, Avg Severity, Monthly Trends
* Pie/Donut Chart: Severity distribution
* Bar Chart: Top 10 States with most accidents
* Line Chart: Accidents by Hour
* Map: Geospatial accident hotspots
* Slicers: Severity, State, Day of Week, Date
* Table: City, Severity, Weather Condition, Time

### Data Source for Power BI

```
Cleaned data/processed_data.csv
```

> **Note**: Due to file size, the original dataset cannot be uploaded directly here. Please download the dataset from the following link:
> 🔗 [Download US\_Accidents\_March23.csv](https://drive.google.com/drive/folders/1yYucxN7_ZV8Ub0TjqlpejefeQIAunuKs?usp=sharing)

Make sure columns like `Hour`, `DayOfWeek`, `Start_Lat`, `Start_Lng` are correctly typed in Power BI.

---

## 📚 Notebooks for Exploration

* `01_Data_Cleaning_and_Exploration.ipynb`
* `02_Feature_Analysis.ipynb`
* `03_Hotspot_Visualization.ipynb`

---

## ✍️ Author

**Shashank Mishra**
 
