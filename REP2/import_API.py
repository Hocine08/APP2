import requests
reponse = requests.get('https://randomuser.me/api')
print(reponse.status_code)
print(reponse.json())
prin(" le premier script lancé via le mecanisme de deploiment(^^)bravo")