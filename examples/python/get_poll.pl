import requests

endpoint = "https://api.strawpoll.com/v3"
api_key = "YOUR_API_KEY"

poll_id = "NPgxkzPqrn2"

response = requests.get(endpoint + '/polls/' + poll_id, headers = { 'X-API-KEY': api_key })

if response:
	poll = response.json() # response is Poll object
	print(poll)
else:
	error = response.json()
	print(error)
