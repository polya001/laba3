import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd
import time
tiny = 'C:\\Users\\Полина\\lab3\\nyc_yellow_tiny.csv'
df=pd.read_csv(tiny)
df["tpep_pickup_datetime"]=pd.to_datetime(df["tpep_pickup_datetime"])
#1
start_time = time.time()
for i in range(10):
    a=df[['VendorID']].groupby('VendorID').size().reset_index(name='count')
end_time = time.time()
execution_time = (end_time - start_time) / 10
print(f"Среднее время выполнения 1 запроса: {execution_time} секунд")
print(a)
#2
start_time2 = time.time()
for i in range(10):
    b=df[['passenger_count', 'total_amount']].groupby('passenger_count').mean().reset_index()
end_time2 = time.time()
execution_time2 = (end_time2 - start_time2)/10
print(f"Среднее время выполнения 2 запроса: {execution_time2} секунд")
print(b)
#3
start_time3 = time.time()
for i in range(10):
    selected_df = df.loc[:, ['passenger_count', 'tpep_pickup_datetime']]
    selected_df['year'] = pd.to_datetime(selected_df.pop('tpep_pickup_datetime'),format='%Y-%m-%d %H:%M:%S').dt.year
    grouped_df = selected_df.groupby(['passenger_count', 'year'])
    final_df = grouped_df.size().reset_index(name='counts')
end_time3 = time.time()
execution_time3 = (end_time3 - start_time3)/10
print(f"Среднее время выполнения 3 запроса: {execution_time3} секунд")
print(final_df)
#4
start_time4 = time.time()
for i in range(10):
    selected_df4 = df.loc[:,[ 'passenger_count', 'tpep_pickup_datetime', 'trip_distance']]
    selected_df4['trip_distance'] = selected_df4['trip_distance'].round().astype(int)
    selected_df4['year'] = pd.to_datetime(selected_df4.pop('tpep_pickup_datetime'),format='%Y-%m-%d %H:%M:%S').dt.year
    grouped_df4 = selected_df4.groupby(['passenger_count','year','trip_distance'])
    final_df4 = grouped_df4.size().reset_index(name='counts')
    final_df4 = final_df4.sort_values(['year', 'counts'], ascending=[True, False])
end_time4 = time.time()
execution_time4 = (end_time4 - start_time4)/10
print(f"Среднее время выполнения 4 запроса: {execution_time4} секунд")
print(final_df4)


