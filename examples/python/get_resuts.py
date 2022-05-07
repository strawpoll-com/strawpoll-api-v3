import requests

endpoint = "https://api.strawpoll.com/v3"
api_key = "YOUR_API_KEY"

poll_id = "XOgOJjEQon3"

response = requests.get(endpoint + '/polls/' + poll_id + '/results', headers = { 'X-API-KEY': api_key })

if response:
	poll_results = response.json() # response is PollResults object
	print("-------------------------------------------------------------------------------")
	print("| " + "Name".ljust(30) + " | " + " | ".join([option["value"].ljust(12) for option in poll_results["poll_options"]]) + " |")
	print("-------------------------------------------------------------------------------")
	for participant in poll_results["poll_participants"]:
		print("| " + participant["name"].ljust(30) + ' | ' + " | ".join(str(vote).ljust(12) for vote in participant["poll_votes"]) + " |")
		print("-------------------------------------------------------------------------------")
	print("Total 'yes' votes: " + str(poll_results["vote_count"]))
	print("Total participants: " + str(poll_results["participant_count"]))
else:
	error = response.json()
	print(error)
