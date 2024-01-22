import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
pixela_username = USER
pixela_token = TOKEN
graph_id = "graph1"

user_params = {
    "token": pixela_token,
    "username": pixela_username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs"

graph_config = {
    "id": graph_id,
    "name": "Studying graph",
    "unit": "min",
    "type": "int",
    "color": "sora",
}

headers = {"X-USER-TOKEN": pixela_token}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

yesterday = datetime(year=2023, month=7, day=21)
yesterday_formatted = yesterday.strftime("%Y%m%d")

# # Posting data to the graph
# pixel_creation_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs/{graph_id}"
# pixel_data = {
#     "date": yesterday.strftime("%Y%m%d"),
#     "quantity": "190"
# }

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# Editing a data
pixela_edit_endpoint = (
    f"{pixela_endpoint}/{pixela_username}/graphs/{graph_id}/{yesterday_formatted}"
)
data_for_edit = {"quantity": "190"}
response = requests.put(url=pixela_edit_endpoint, json=data_for_edit, headers=headers)
print(response.text)
