import requests

header = {
    'Accept': 'application/json',
    'authorization':'Bearer <API token>',
}
def get_user():
    response = requests.get('https://api.clashofclans.com/v1/players/%2320QGPQV8', header)
    user_json = response.json()
    print(user_json)

get_user()