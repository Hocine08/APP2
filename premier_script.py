import cx_Oracle
import pandas as pd
#connection =cx_Oracle.connect("hr/@localhost:1521/orcl2.lan")#


dsn = cx_Oracle.makedsn(
    'localhost',
    '1521',
    service_name='orcl2.lan'
)

conn=cx_Oracle.connect(
    user='hr',
    password='',
    dsn= dsn
)

c = conn.cursor()

c.execute('select * from employees where rownum <10')

"for  row in c: print(row)"

df = pd.DataFrame(c)
df.index
df.columns

