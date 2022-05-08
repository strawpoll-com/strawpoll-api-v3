import requests

ENDPOINT = "https://api.strawpoll.com/v3"
API_KEY = "YOUR_API_KEY"

poll_id = "XOgOJjEQon3" # Use "NPgxkzPqrn2" for an example without participants

response = requests.get(ENDPOINT + '/polls/' + poll_id + '/results', headers = { 'X-API-KEY': API_KEY })

if response:
	poll_results = response.json() # response is PollResults object
	print("+".ljust(63, "-") + "+".ljust(14, "-") + "+")
	for option in poll_results["poll_options"]:
		print("| " + option["value"].ljust(60) + " | " + str(option["vote_count"]).ljust(12) + "|")
		print("+".ljust(63, "-") + "+".ljust(14, "-") + "+")
	if (len(poll_results["poll_participants"]) > 0):
		row_space = "+".ljust(33, "-") + "+" + "+".join(["".ljust(14, "-") for option in poll_results["poll_options"]]) + "+"
		print("Participants:")
		print(row_space)
		print("| " + "Name".ljust(30) + " | " + " | ".join([option["value"].ljust(12) for option in poll_results["poll_options"]]) + " |")
		print(row_space)
		for participant in poll_results["poll_participants"]:
			print("| " + participant["name"].ljust(30) + ' | ' + " | ".join(str(vote).ljust(12) for vote in participant["poll_votes"]) + " |")
			print(row_space)
	print("Total 'yes' votes: " + str(poll_results["vote_count"]))
	print("Total participants: " + str(poll_results["participant_count"]))
else:
	error = response.json()
	print(error)
