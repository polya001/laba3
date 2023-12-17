import duckdb#
import time
duck_file='C:\\Users\\Полина\\lab3\\duck.db'
conn = duckdb.connect(duck_file)
c = conn.cursor()
# Create tables by importing the content from the CSVs
#c.execute( "CREATE TABLE taxi AS SELECT * FROM read_csv_auto('nyc_yellow_tiny.csv');")
#1
start_time = time.time()
for i in range(10):
    a=c.sql('''SELECT "VendorID", COUNT(*) FROM taxi GROUP BY 1;''')
end_time = time.time()
execution_time = (end_time - start_time) / 10
print(f"Среднее время выполнения 1 запроса: {execution_time} секунд")
a.show()
#2
start_time2 = time.time()
for i in range(10):
    b=c.sql('''SELECT "passenger_count", AVG("total_amount")FROM taxi GROUP BY 1;''')
end_time2 = time.time()
execution_time2 = (end_time2 - start_time2)/10
print(f"Среднее время выполнения 2 запроса: {execution_time2} секунд")
b.show()
#3
start_time3 = time.time()
for i in range(10):
    d=c.sql('''SELECT "passenger_count", EXTRACT(year FROM "tpep_pickup_datetime"), COUNT(*) FROM taxi GROUP BY 1, 2''')
d.show()
end_time3 = time.time()
execution_time3 = (end_time3 - start_time3)/10
print(f"Среднее время выполнения 3 запроса: {execution_time3} секунд")
#4
start_time4 = time.time()
for i in range(10):
    f=c.sql('''SELECT "passenger_count", EXTRACT(year FROM "tpep_pickup_datetime"), ROUND("trip_distance"), COUNT(*) FROM taxi GROUP BY 1, 2, 3 ORDER BY 2, 4 DESC;''')
f.show()
end_time4 = time.time()
execution_time4 = (end_time4 - start_time4)/10
print(f"Среднее время выполнения 4 запроса: {execution_time4} секунд")
