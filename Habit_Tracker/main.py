import requests
from datetime import datetime

USERNAME = 'muhid'
TOKEN = 'perry123'

END_POINT = 'https://pixe.la/v1/users'

users_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

# initially creating an account
# response = requests.post(url=END_POINT, json=users_params)
# print(response.text)

GRAPH_ENDPOINT = f'https://pixe.la/v1/users/{USERNAME}/graphs'

graph_params = {
    "id": "graph1",
    "name": "My Cycling graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    'X-USER-TOKEN': TOKEN
}

# response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
# print(response.text)

VALUE_ENDPOINT = f'https://pixe.la/v1/users/{USERNAME}/graphs/graph1'

today = datetime(year=2023, month=6, day=28)
date = today.strftime('%Y%m%d')

value_params = {
    'date': date,
    'quantity': '15',
}

# response = requests.post(url=VALUE_ENDPOINT, json=value_params, headers=headers)
# print(response.text)

UPDATE_ENDPOINT = f'https://pixe.la/v1/users/{USERNAME}/graphs/graph1/{date}'

update_params = {
    'quantity': '20.12'
}

response = requests.put(url=UPDATE_ENDPOINT, json=update_params, headers=headers)
print(response.text)

DELETE_ENDPOINT = f'https://pixe.la/v1/users/{USERNAME}/graphs/graph1/{date}'

# response = requests.delete(url=DELETE_ENDPOINT, headers=headers)
# print(response.text)
