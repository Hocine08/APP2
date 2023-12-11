import csv

f = open('file1.csv')
fichierCSV = csv.reader(f)
listex = []
listey = []

for ligne in fichierCSV:
    x = float(ligne[0])
    y =ligne[1]
    listex.append(x)
    listey.append(y)

print(listex)
print(listey)