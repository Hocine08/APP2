
import pandas
import numpy
"s4 = pandas.Series([2, 5, 7, 3], index = ['a', 'b', 'c', 'd'])"
"s = pandas.Series([1, 2, 5, 7])"
"s1 = pandas.Series([1.3, 2, 5.3, 7])"
"s3 = pandas.Series([1, 2, 5, 7], dtype = numpy.int8)"
"print(s4['b']+s4['c'])"
"df = pd.read_csv('file1.csv', sep = ';' )"
df = pandas.read_csv('file1.csv', sep = ',', names = ['X1', 'X2'], header = None)
print(df['X2']*df['X2'])
"df.head(3)"
"df.columns"





"for x in df: print(x) # imprime le nom de la colonne"

"df = pandas.read_csv('file1.csv', sep = ';', names = ['X1'; 'X2'])"
