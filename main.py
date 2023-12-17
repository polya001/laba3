
import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')
tiny = 'C:\\Users\\Полина\\lab3\\nyc_yellow_tiny.csv'
df=pd.read_csv(tiny)
df["tpep_pickup_datetime"]=pd.to_datetime(df["tpep_pickup_datetime"])
df.to_sql('taxi',engine,if_exists='replace',index=False)

