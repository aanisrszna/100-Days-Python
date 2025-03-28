import requests
from datetime import datetime
USERNAME= "YOUR NAME"
TOKEN = "token"
GRAPHID="graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "ddsjhebcjebqiecj",
    "username": "token",
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
#
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id" : "graph1",
    "name" : "Cycling Graph",
    "unit" : "Km",
    "type": "float",
    "color": "ajisai"
}

header = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url = graph_endpoint, json=graph_config, headers=header)
# print (response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}"
today = datetime.now()
print (today.strftime("%Y%m%d"))
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today ?"),
}
response = requests.post(url = pixel_creation_endpoint, json=pixel_data, headers=header)
print (response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime("%Y%m%d")}"

new_pixel_data  ={
    "quantity": "4.5"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=header)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPHID}/{today.strftime("%Y%m%d")}"

# response = requests.delete(url=delete_endpoint, headers=header)
# print(response.text)