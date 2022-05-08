import requests
from datetime import datetime

ENDPOINT = "https://api.strawpoll.com/v3"
API_KEY = "YOUR_API_KEY"

payload = {
	"title": "When do we meet to discuss this Python example?",
	"media": None,
	"poll_options": [
		{
			"type": "date",
			"date": "2022-08-13"	# All-day option
		},
		{
			"type": "time_range",
			"start_time": 1660989600,
			"end_time": 1660993200
		},
		{
			"type": "time_range",
			"start_time": datetime.strptime("2022-08-27T12:00:00+02:00", "%Y-%m-%dT%H:%M:%S%z").timestamp(),	# datetime reads UTC time so it is recommended to use a timezone offset (e.g. +02:00)
			"end_time": None	# Open end
		}
	],
	"poll_config": {
		"is_private": True,
		"vote_type": "participant_grid",
		"allow_comments": True,
		"allow_indeterminate": True,
		"deadline_at": None,
		"duplication_checking": "none",
		"edit_vote_permissions": "admin_voter",
		"allow_vpn_users": True,
		"hide_participants": False,
		"is_multiple_choice": True,
		"multiple_choice_min": 0,
		"multiple_choice_max": 0,
		"require_voter_names": True,
	},
	"poll_meta": {
		"description": None,
		"location": "Online (Teams)",
		"timezone": "Europe/Berlin"		# Use None for automatic timezones
	},
	"type": "meeting",
}

response = requests.post(ENDPOINT + '/polls', json = payload, headers = { 'X-API-KEY': API_KEY })

if response:
	poll = response.json() # response is Poll object
	print(poll["url"])
else:
	error = response.json()
	print(error)
