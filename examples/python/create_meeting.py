import requests
import datetime

endpoint = "https://api.strawpoll.com/v3"
api_key = "YOUR_API_KEY"

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
			"start_time": datetime.datetime.strptime("2022-08-27T12:00:00+02:00", "%Y-%m-%dT%H:%M:%S%z").timestamp(),	# datetime reads UTC time so it is recommended to use a timezone offset (e.g. +02:00)
			"end_time": None	# Open end
		}
	],
	"poll_config": {
		"vote_type": "participant_grid",
		"allow_comments": True,
		"allow_indeterminate": False,
		"allow_other_option": False,
		"custom_design_colors": None,
		"deadline_at": None,
		"duplication_checking": "ip",
		"edit_vote_permissions": "nobody",
		"force_appearance": None,
		"hide_participants": False,
		"is_multiple_choice": True,
		"multiple_choice_min": 0,
		"multiple_choice_max": 0,
		"number_of_winners": 1,
		"randomize_options": False,
		"require_voter_names": True,
		"results_visibility": "always",
		"use_custom_design": False
	},
	"poll_meta": {
		"description": None,
		"location": "Online (Teams)",
		"timezone": "Europe/Berlin"		# Use None for automatic timezones
	},
	"type": "meeting",
}

response = requests.post(endpoint + '/polls', json = payload, headers = { 'X-API-KEY': api_key })

if response:
	poll = response.json() # response is Poll object
	print(poll["url"])
else:
	error = response.json()
	print(error)
