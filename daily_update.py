# data_update v1.0

# Import librairies
from utils import API_request, aggreg_to_utc_duration, moment
import pandas as pd
import csv

# Import constants
from utils import URL

start_date = moment('yesterday', 'AM')
end_date = moment('yesterday', 'PM')
print(start_date)
print(end_date)

# Collect raw data from REE API
response = API_request(URL, start_date, end_date)

# Extract values from JSON structure returned in API response
demanda_real = response.json()['included'][0]['attributes']['values']
demanda_programada = response.json()['included'][1]['attributes']['values']
demanda_prevista = response.json()['included'][2]['attributes']['values']

# Initialize an empty list to help the aggregation process
df_data = []

# Append new data to REE_data.csv collecting raw data
with open('data/REE_data.csv', 'a', newline='') as file:
    csv_writer = csv.writer(file)
    for real, programada, prevista in zip(demanda_real, demanda_programada, demanda_prevista):
        # Write data to REE_data.csv
        date_time = real['datetime']
        demand = real['value']
        planned = programada['value']
        forecast = prevista['value']
        csv_writer.writerow([date_time, demand, planned, forecast])
        # Append the row to the DataFrame
        df_data.append({'datetime': date_time, 'demanda': demand, 'programada': planned, 'prevista': forecast})

# Append REE data to the various aggregated files
for duration in ['10mn', '1h', '1d']:
    df = pd.DataFrame(df_data)
    print(df.head())
    print(f"Aggregating data by {duration}...")
    file_path = f'data/REE_data_aggregated_by_{duration}.csv'
    df_duration = aggreg_to_utc_duration(df, duration)
    print(df_duration.head())
    # Write dataframe with reformatted data to destination CSV file
    df_duration.to_csv(file_path, header=False, index=False, mode='a', sep=',')