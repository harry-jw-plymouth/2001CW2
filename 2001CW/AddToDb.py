import pyodbc
import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import pyodbc
import urllib.parse

server = 'dist-6-505.uopnet.plymouth.ac.uk'
database = 'COMP2001_HWatton'
username = 'HWatton'
password = 'IfrW391*'
driver =  '{ODBC Driver 17 for SQL Server}'

conn_str = (
    f'DRIVER={driver};'
    f'SERVER={server};' 
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password};'
    'Encrypt=Yes;'
    'TrustServerCertificate=Yes;'
    'Connection Timeout=30;'
    'Trusted_Connection=No'
)

Trails = [
    "'Trail1', 'Trail summary 1', 'Trail Desc1', 'Easy', 'Location1', 11.1, 1.1, 'Loop', 1,  '2024-11-19 16:15:10' ",
    "'Trail2', 'Trail summary 2', 'Trail Desc2', 'Easy', 'Location2', 22.2, 2.2, 'Loop', 2,  '2024-11-19 16:25:10' ",
    "'Trail3', 'Trail summary 3', 'Trail Desc3', 'Easy', 'Location3', 33.3, 3.3, 'Loop', 3,  '2024-11-19 16:35:10' ",
]    
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

for trail_data in Trails:
    insert_cmd = f"INSERT INTO CW2.Trail VALUES ({trail_data})"
    cursor.execute(insert_cmd)

cursor.commit()