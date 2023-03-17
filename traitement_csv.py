import csv

f = open('file1.csv')
fichierCSV = csv.reader(f)
for lig in fichierCSV:
    print(lig)