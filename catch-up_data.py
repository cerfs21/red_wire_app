# catch-up_data v1.2
# Script to catch up REE data from the last collect date up to the current date
# 	Updates from v1.1:
# 	- Import DATA_PATH constant
# 	- Record last collect date in a file

'''
This script catches up REE data from the last collect date up to the current date, if for any reason the data
collection has been interrupted for a period of time.
It repeats the treatment of the original daily_update.py script for a range of dates based on the last collect
date read from the last line in REE_data_aggregated_by_1d.csv.
'''

# Import librairies
from utils import API_request, aggreg_to_utc_duration, moment
import pandas as pd
import csv
from datetime import datetime as dt, timedelta
import pytz

# Import constants
from utils import URL, DATA_PATH

# Open the 1-day aggregated data file aligned with UTC and look for the end of the file to get the last collect start date
with open(DATA_PATH+'last_collect_date.txt', 'r') as file:
    last_collect_date = file.readline()
    print("Last collect date:", last_collect_date)
# Use last_collect_date to set the begin date for catching up data
begin_date = dt.strptime(last_collect_date, '%Y-%m-%d %H:%M:%S').replace(hour=0, minute=0, second=0) + timedelta(days=1)
# Set the finish date to stop catching up data
finish_date = moment('yesterday', 'PM')
                           
print("Define period for data collection")
print("Begins:", begin_date)
print("Finishes:", finish_date)
print("Duration:", finish_date-begin_date)

# Loop through the days between the last collect date and yesterday
print("Start collecting data...")
collect_date = begin_date.astimezone(pytz.timezone('UTC'))
while collect_date < finish_date:

    # Set the data collection start and end dates for the current day
    start_date = collect_date.astimezone(pytz.timezone('Europe/Madrid'))
    print("\n---------------------------------")
    print("Start date for data collection:", start_date)
    end_date = start_date+timedelta(hours=23)+timedelta(minutes=59)

    # # Collect raw data from REE API
    # response = API_request(URL, start_date, end_date)

    # # Extract values from JSON structure returned in API response
    # demanda_real = response.json()['included'][0]['attributes']['values']
    # demanda_programada = response.json()['included'][1]['attributes']['values']
    # demanda_prevista = response.json()['included'][2]['attributes']['values']

    # # Initialize an empty list which will be converted to a DataFrame in the data aggregation step
    # df_data = []

    # # Collect raw data and append it to REE_data.csv 
    # with open(DATA_PATH+'REE_data.csv', 'a', newline='') as file:
    #     csv_writer = csv.writer(file)
    #     for real, programada, prevista in zip(demanda_real, demanda_programada, demanda_prevista):
    #         # Write data to REE_data.csv
    #         date_time = real['datetime']
    #         demand = real['value']
    #         planned = programada['value']
    #         forecast = prevista['value']
    #         csv_writer.writerow([date_time, demand, planned, forecast])
    #         # Append the row to the list which will be converted to a DataFrame in the next step
    #         df_data.append({'datetime': date_time, 'demanda': demand, 'programada': planned, 'prevista': forecast})

    # # Append REE data to the various aggregated files
    # for duration in ['10mn', '1h', '1d']:
    #     df = pd.DataFrame(df_data)
    #     print(f"Aggregating data by {duration}...")
    #     print(df.head(3))
    #     file_path = f'{DATA_PATH}REE_data_aggregated_by_{duration}.csv'
    #     df_duration = aggreg_to_utc_duration(df, duration)
    #     print(df_duration.head(1))
    #     # Append dataframe with reformatted data to destination CSV file
    #     df_duration.to_csv(file_path, header=False, index=False, mode='a', sep=',')
    
    # Increment the collect date by one day to continue the loop
    collect_date = collect_date+timedelta(days=1)

with open(DATA_PATH+'last_collect_date.txt', 'w') as file:
    file.write(f"{finish_date}")