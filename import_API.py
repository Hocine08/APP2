import requests
reponse = requests.get('https://randomuser.me/api')
print(reponse.status_code)
print(reponse.json())