import requests
from datetime import datetime

ENDPOINT = "https://api.strawpoll.com/v3"
API_KEY = "YOUR_API_KEY"

poll_id = "mpnba8P4vy5"

response = requests.get(ENDPOINT + '/polls/' + poll_id + '/results', headers = { 'X-API-KEY': API_KEY })

def meeting_option_name(option):
	if (option["type"] == 'date'):
		return option["date"]
	elif (option["type"] == 'time_range'):
		datetime_start = datetime.fromtimestamp(option["start_time"])
		datetime_end = datetime.fromtimestamp(option["end_time"])
		return datetime_start.strftime('%Y-%m-%d') + " (" + datetime_start.strftime('%H:%M') + " - " + datetime_end.strftime('%H:%M') + ")"
	else:
		return option["value"]

if response:
	poll_results = response.json() # response is PollResults object
	print("+".ljust(63, "-") + "+".ljust(30, "-") + "+")
	for option in poll_results["poll_options"]:
		print("| " + meeting_option_name(option).ljust(60) + " | " + str(option["vote_count"]).ljust(28) + "|")
		print("+".ljust(63, "-") + "+".ljust(30, "-") + "+")
	if (len(poll_results["poll_participants"]) > 0):
		row_space = "+".ljust(33, "-") + "+" + "+".join(["".ljust(30, "-") for option in poll_results["poll_options"]]) + "+"
		print("Participants:")
		print(row_space)
		print("| " + "Name".ljust(30) + " | " + " | ".join([meeting_option_name(option).ljust(28) for option in poll_results["poll_options"]]) + " |")
		print(row_space)
		for participant in poll_results["poll_participants"]:
			print("| " + participant["name"].ljust(30) + ' | ' + " | ".join(str(vote).ljust(28) for vote in participant["poll_votes"]) + " |")
			print(row_space)
	print("Total 'yes' votes: " + str(poll_results["vote_count"]))
	print("Total participants: " + str(poll_results["participant_count"]))
else:
	error = response.json()
	print(error)
