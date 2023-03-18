import pandas as pd

parquet_fil = r'userdata1.parquet'

pd.read_parquet(parquet_fil , engine='auto')