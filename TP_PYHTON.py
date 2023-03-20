import cx_Oracle
import csv
import pandas as pd

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

c.execute(
          'select A.EMPLOYEE_ID, A.FIRST_NAME, A.LAST_NAME, A.EMAIL,A.PHONE_NUMBER,A.HIRE_DATE,A.JOB_ID,A.SALARY ,A.COMMISSION_PCT, A.MANAGER_ID, A.DEPARTMENT_ID , B.JOB_TITLE, B.MIN_SALARY,B.MAX_SALARY   from   EMPLOYEES A INNER join JOBS  B ON  A.JOB_ID = B.JOB_ID where A.EMPLOYEE_ID > 200'
          )

#for  row in c: print( "ID:" , row[0]  ,   "Nom:" , row[1] , "Prenom:" , row[2]   , "EMAIL:" , row[3]   , "TEL:" , row[4])

#data = row[4]




#with open("file7.csv","w") as file7:
#    file7.write(data )


fichier_export = open("Fichier202303202.csv", "w" )
fieldnames = ['ID_EMP'+ ';'+'FIRET_NAME'+ ';'+'LAST_NAME'+ ';'+'MAIL' + ';'+'TELE' + ';'+ 'SALAIRE']
writer = csv.DictWriter(fichier_export, fieldnames=fieldnames)
writer.writeheader()
for row  in c:
    fichier_export.write( str(row[0]) + ';' +  row[1] +';' +  row[2] +';' +  row[3]   +';' +   row[4]   +';' +   str(row[7])  +'\n' )
fichier_export.close()


csv_file = r'Fichier202303202.csv'
var_csv = pd.read_csv(csv_file , delimiter=';' , header = 0)
json_file = r'fichier202303202.json'
output = var_csv.to_json(json_file, indent = 1, orient ='records')





df = pd.read_csv('Fichier202303202.csv', sep =';',index_col = 3)
print(df)
maxs=df.max()
print("max" , + maxs)