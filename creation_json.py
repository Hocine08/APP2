import pandas as pd

csv_file = r'file1.csv'
var_csv = pd.read_csv(csv_file , names = ['X1', 'X2'],     header = None)



json_file = r'fichier1.json'
output = var_csv.to_json(json_file, indent = 1, orient ='records')


json_file_compressed = r'fichier1.json.gzip'
output_compressed = var_csv.to_json(json_file_compressed, indent = 1, orient ='records' , compression='gzip')
