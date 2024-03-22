import requests
from datetime import datetime

USERNAME = "cavalcantevitor"
TOKEN = "token"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

# Creating the user
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Creating the graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Water Graph",
    "unit": "ml",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Adding a pixel
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
today_formatted = today.strftime("%Y%m%d")

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "300",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# Updating a pixel
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_formatted}"

new_pixel_data = {
    "quantity": "700",
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# Deleting a pixel
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_formatted}"

response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)