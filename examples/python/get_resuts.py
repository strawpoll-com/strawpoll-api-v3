import requests

endpoint = "https://api.strawpoll.com/v3"
api_key = "YOUR_API_KEY"

poll_id = "XOgOJjEQon3" # Use "NPgxkzPqrn2" for an example without participants

response = requests.get(endpoint + '/polls/' + poll_id + '/results', headers = { 'X-API-KEY': api_key })

if response:
	poll_results = response.json() # response is PollResults object
	print("+--------------------------------------------------------------+--------------+")
	for option in poll_results["poll_options"]:
		print("| " + option["value"].ljust(60) + " | " + str(option["vote_count"]).ljust(12) + " |")
		print("+--------------------------------------------------------------+--------------+")
	if (len(poll_results["poll_participants"]) > 0):
		print("Participants:")
		print("+--------------------------------+--------------+--------------+--------------+")
		print("| " + "Name".ljust(30) + " | " + " | ".join([option["value"].ljust(12) for option in poll_results["poll_options"]]) + " |")
		print("+--------------------------------+--------------+--------------+--------------+")
		for participant in poll_results["poll_participants"]:
			print("| " + participant["name"].ljust(30) + ' | ' + " | ".join(str(vote).ljust(12) for vote in participant["poll_votes"]) + " |")
			print("+--------------------------------+--------------+--------------+--------------+")
	print("Total 'yes' votes: " + str(poll_results["vote_count"]))
	print("Total participants: " + str(poll_results["participant_count"]))
else:
	error = response.json()
	print(error)
