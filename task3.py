#Use the template below to get started
import url 

url = 'https://api.nationalize.io/?name=nathaniel'
response = requests.get(l)

if response.status_code == ("ok"):
   data = response.json()
else: 
   print(f"Error code: {response.status_code}")
name = data["howard"]
print(name)