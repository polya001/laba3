
import time
#start_time = time.time()
import psycopg2


#querry1
conn = psycopg2.connect('postgresql://postgres:postgres@localhost:5432/postgres')
cursor = conn.cursor()
start_time = time.time()
for i in range(10):
    cursor.execute('SELECT "VendorID", COUNT(*) FROM taxi GROUP BY 1;')
end_time = time.time()
execution_time = (end_time - start_time)/10
print(f"Среднее время выполнения 1 запроса: {execution_time} секунд")
results = cursor.fetchall()
for row in results:
  print(row)
#querry2
start_time2 = time.time()
for i in range(10):
    cursor.execute('SELECT "passenger_count", AVG("total_amount")FROM taxi GROUP BY 1;')
end_time2 = time.time()
execution_time2 = (end_time2 - start_time2)/10
print(f"Среднее время выполнения 2 запроса: {execution_time2} секунд")
print(cursor.fetchall())
#querry3
start_time3 = time.time()
for i in range(10):
    cursor.execute('SELECT "passenger_count", EXTRACT(year FROM "tpep_pickup_datetime"), COUNT(*) FROM taxi GROUP BY 1, 2')
end_time3 = time.time()
execution_time3 = (end_time3 - start_time3)/10
print(f"Среднее время выполнения 3 запроса: {execution_time3} секунд")
results3 = cursor.fetchall()
for row1 in results3:
  print(row1)
#querry4
start_time4 = time.time()
for i in range(10):
    cursor.execute('SELECT "passenger_count", EXTRACT(year FROM "tpep_pickup_datetime"), ROUND("trip_distance"), COUNT(*) FROM taxi GROUP BY 1, 2, 3 ORDER BY 2, 4 DESC;')
end_time4 = time.time()
execution_time4 = (end_time4 - start_time4)/10
print(f"Среднее время выполнения 4 запроса: {execution_time4} секунд")
print(cursor.fetchall())
cursor.close()
conn.close()



