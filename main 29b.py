import requests
import json

url = "https://api.imagga.com/v2/tags"

querystring = {"image_url":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRNrg4qvHt5U_iLDDmJZzAgy6shYAoAaYV-UQ&usqp=CAU.jpeg"}

headers = {
    'accept': "application/json",
    'authorization': "Basic YWNjX2Q0NWZmZGU2MTc5NGUyNDpiYzk0NjMzNTE3NDhmYTYxYjQxODRhZmU4MDAxNjFhOA=="
    }

response = requests.request("GET", url, headers=headers, params=querystring)
data = json.loads(response.text.encode("ascii"))

for i in range(6):
    tag = data["result"]["tags"][i]["tag"]["en"]
    print(tag)
