import sqlite3
import time
import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd
tiny = 'C:\\Users\\Полина\\lab3\\nyc_yellow_tiny.csv'
df=pd.read_csv(tiny)
if 'Airport_fee' in df:
  df.pop('Airport_fee')
df_file='C:\\Users\\Полина\\lab3\\dbfile.db'
connection = sqlite3.connect(df_file)
df["tpep_pickup_datetime"]=pd.to_datetime(df["tpep_pickup_datetime"])
df.to_sql('taxi',connection,if_exists='replace',index=False)
cursor = connection.cursor()
# querry1
start_time = time.time()
for i in range(10):
  cursor.execute('SELECT "VendorID", COUNT(*) FROM taxi GROUP BY 1')
end_time = time.time()
execution_time = (end_time - start_time) / 10
print(f"Среднее время выполнения 1 запроса: {execution_time} секунд")
results = cursor.fetchall()
for row in results:
  print(row)
# querry2
start_time2 = time.time()
for i in range(10):
  cursor.execute('SELECT "passenger_count", AVG("total_amount")FROM taxi GROUP BY 1;')
end_time2 = time.time()
execution_time2 = (end_time2 - start_time2)/10
print(f"Среднее время выполнения 2 запроса: {execution_time2} секунд")
results2 = cursor.fetchall()
for row2 in results2:
  print(row2)
# querry3
start_time3 = time.time()
for i in range(10):
  cursor.execute('SELECT "passenger_count", strftime("%Y","tpep_pickup_datetime")  , COUNT(*) FROM taxi GROUP BY 1, 2')
end_time3 = time.time()
execution_time3 = (end_time3 - start_time3)/10
print(f"Среднее время выполнения 3 запроса: {execution_time3} секунд")
results3 = cursor.fetchall()
for row1 in results3:
  print(row1)
# querry4
start_time4 = time.time()
for i in range(10):
  cursor.execute('SELECT "passenger_count", strftime("%Y","tpep_pickup_datetime") , ROUND("trip_distance"), COUNT(*) FROM taxi GROUP BY 1, 2, 3 ORDER BY 2, 4 DESC;')
end_time4 = time.time()
execution_time4 = (end_time4 - start_time4)/10
print(f"Среднее время выполнения 4 запроса: {execution_time4} секунд")
results4 = cursor.fetchall()
for row4 in results4:
  print(row4)


connection.close()