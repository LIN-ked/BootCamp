import pandas as pd
import matplotlib.pyplot as plt

url = "https://data.cityofnewyork.us/api/views/6fi9-q3ta/rows.csv?accessType=DOWNLOAD"
df = pd.read_csv(url)

df['hour_beginning'] = pd.to_datetime(df['hour_beginning'], errors='coerce')
weekdays_df = df[df['hour_beginning'].dt.dayofweek < 5]
weekday_counts = weekdays_df.groupby(weekdays_df['hour_beginning'].dt.day_name())['Pedestrians'].mean()

plt.figure(figsize=(10, 6))
weekday_counts.reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']).plot(kind='line', marker='o')
plt.title('Average Pedestrian')
plt.xlabel('Day')
plt.ylabel('Pedestrian Count')
plt.grid(True)
plt.show()

brooklyn_bridge_2019 = df[(df['hour_beginning'].dt.year == 2019) & (df['location'] == 'Brooklyn Bridge')]
weather_encoded = pd.get_dummies(brooklyn_bridge_2019['weather_summary'], prefix='Weather')
brooklyn_bridge_2019 = pd.concat([brooklyn_bridge_2019, weather_encoded], axis=1)
correlation_matrix = brooklyn_bridge_2019.corr(numeric_only=True)['Pedestrians'].sort_values(ascending=False)
print(correlation_matrix)

def categorize_time_of_day(hour):
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 21:
        return 'Evening'
    else:
        return 'Night'

df['Time of Day'] = df['hour_beginning'].dt.hour.apply(categorize_time_of_day)
time_of_day_counts = df.groupby('Time of Day')['Pedestrians'].mean().reindex(['Morning', 'Afternoon', 'Evening', 'Night'])

plt.figure(figsize=(10, 6))
time_of_day_counts.plot(kind='bar')
plt.title('Average Pedestrian')
plt.xlabel('Time')
plt.ylabel('Pedestrian Count')
plt.grid(True)
plt.show()
