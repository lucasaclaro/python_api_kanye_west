import requests

link = 'https://api.kanye.rest/'
request = requests.get(link)
request_json = request.json()

print('Kanye West Phrases')
print('***' * 7)

print(f"\n{request_json['quote']}.")


