import requests

ENDPOINT = "https://api.strawpoll.com/v3"
API_KEY = "YOUR_API_KEY"

poll_id = "NPgxkzPqrn2"

response = requests.get(ENDPOINT + '/polls/' + poll_id, headers = { 'X-API-KEY': API_KEY })

if response:
	poll = response.json() # response is Poll object
	print(poll)
else:
	error = response.json()
	print(error)
