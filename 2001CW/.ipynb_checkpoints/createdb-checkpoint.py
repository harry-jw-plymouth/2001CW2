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

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

Columns = [
    'TrailID INT IDENTITY (1,1) PRIMARY KEY',
    'Trail_name VARCHAR(60) UNIQUE',
    'Trail_Summary VARCHAR(6000)',
    'Trail_Description VARCHAR(6000)',
    'Difficulty VARCHAR (10)',
    'Location VARCHAR (100)',
    'Length FLOAT',
    'Elevation_gain FLOAT',
    'Route_type VARCHAR(10)',
    'OwnerID INT',
    'timestamp DATETIME',
]

create_table_cmd = f"CREATE TABLE CW2.NewTest ({','.join(Columns)})"
cursor.execute(create_table_cmd)
cursor.commit()

