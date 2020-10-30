from sqlalchemy import *
import pandas as pd
user_name='postgres'
password='12345678'
host='teate.ctslcs9kjcvo.us-east-2.rds.amazonaws.com'
db_name='postgres'

connection_string=f"postgresql://{user_name}:{password}@{host}/{db_name}"
engine = create_engine(connection_string, max_overflow=20)

def run_query(sql,engine):
    result = engine.connect().execution_options(isolation_level="AUTOCOMMIT").execute((text(sql)))
    return pd.DataFrame(result.fetchall(), columns=result.keys())
