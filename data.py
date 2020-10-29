import logging
import pandas as pd
from app import cache
import numpy as np

TIMEOUT = 120

pd.set_option('display.max_columns', None)
pd.options.display.float_format = '{:,.1f}'.format
aws_access_key_id="AKIAI4AGF74Z5Z63F7CA"
aws_secret_access_key="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"

region_name = "us-east-2"

bucket = "teate"
#key='teate.csv'
key='teate.pkl'

#df = pd.read_csv('https://teate.s3.us-east-2.amazonaws.com/teate.csv', low_memory=False)
df = pd.read_pickle('https://teate.s3.us-east-2.amazonaws.com/teate.pkl')
#df = pd.read_pickle("./teate.pkl")
print("producto OK")

@cache.memoize(timeout=TIMEOUT)
def get_product_df():
    # Generate a dataframe with only columns to use
    #df = pd.read_pickle("./teate.pkl")
    cols = ['NOMBRE CAT', 'Material', 'Fecha Pedido', 'NOMBRE SUB', 'Población', 'UM']
    df['Población'] = df['Población'].fillna(0)
    df2 = df[cols]
    return df2


