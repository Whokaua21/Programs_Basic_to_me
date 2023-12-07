import requests
import json
dados ={'v':100}
s = requests.patch('https://id-prosuct-default-rtdb.firebaseio.com/Chave/.json',data=json.dumps(dados))
print(s)
print(s.text)