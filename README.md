# laba3
## КАК ЗАПУСТИТЬ
### Подключение к серверу postgres
Открыть программу Docker Desktop(должна быть установлена)

Следуя инструкциям https://github.com/DumDereDum/DataBase_cource/blob/main/postgres/README.md нужно подключиться к серверу
### Скачивание базы данных в .csv 
С диска https://drive.google.com/drive/folders/1usY-4CxLIz_8izBB9uAbg-JQEKSkPMg6 нужно скачать файл "nyc_yellow_tiny.csv"
### Клонирование файлов формата .py с репозитория
Нажмите кнопку "Code" в правом верхнем углу. Выпадет меню, в котором нужно выбрать Download ZIP


![](https://github.com/polya001/laba3/blob/main/howdownload.png)

### Запуск кода
В файлах main.py, 2bib.py, 4bib.py для tiny = "Path_to_file_nyc_yellow_tiny.csv"  указать в кавычках путь к файлу nyc_yellow_tiny.csv 

В файле 2bib.py для df_file='Path_to_file\\dbfile.db'  указать в кавычках путь к файлу dbfile.db

В файле 3bib.py для duck_file='Path_to_file\\duck.db'  указать в кавычках путь к файлу duck.db

1. запустить файл main.py
2. можно запускать файлы 1bib.py, 2bib.py, 3bib.py, 4bib.py

### Описание содержания файлов
Файл main.py загружает базу данных на сервер

Файлы 1bib.py, 2bib.py, 3bib.py, 4bib.py используют библиотеки psycopg2, sqlite3, duckdb, pandas соответственно для выполнения запросов

### Сравнение скорости выполнения запросов для 4 библиотек
