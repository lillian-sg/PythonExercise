import requests

response = requests.get("https://www.python.org")

if response.status_code == 200:
    print("Deus certo")

    print(response.text[:100])
else:
    print(f"Deu ruim! Erro {response.status_code}")