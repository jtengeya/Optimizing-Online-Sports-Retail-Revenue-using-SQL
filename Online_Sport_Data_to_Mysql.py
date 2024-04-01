import pandas as pd
from sqlalchemy import create_engine, text
import urllib.parse

host = 'localhost'
username = 'root'
password = urllib.parse.quote_plus('@Badkey..26')

conn_string = f'mysql+pymysql://{username}:{password}@{host}/'

db = create_engine(conn_string)
conn = db.connect()
conn.execute(text("CREATE DATABASE IF NOT EXISTS Online_Sports_Retail"))
conn.close()

database = 'Online_Sports_Retail'
conn_string = f'mysql+pymysql://{username}:{password}@{host}/{database}'
db = create_engine(conn_string)
conn = db.connect()
files = ['brands_v2', 'finance', 'info_v2', 'reviews_v2', 'traffic_v3']
for file in files:
    df = pd.read_csv(f'C:\\Users\\Jackson Tengeya\\Desktop\\Doc\\Online_Sports_Retail\\{file}.csv')
    df.to_sql(file, con=conn, if_exists='replace', index=False)
conn.close()
