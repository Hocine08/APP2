import cx_Oracle
import pandas


#connection =cx_Oracle.connect("hr/@localhost:1521/orcl2.lan")#


dsn = cx_Oracle.makedsn(
    'localhost',
    '1521',
    service_name='orcl2.lan'
)

conn=cx_Oracle.connect(
    user='hr',
    password='Kamel123!',
    dsn= dsn
)

c = conn.cursor()

c.execute('select * from employees where rownum <10')

for  row in c: print(row)

print("votre requete vient d'etre exicutée "
      ""
      ""
      "\n")
df = pandas.read_csv('file1.csv', sep = ',', names = ['X1', 'X2'], header = None)
print(df['X2']*df['X2'])



