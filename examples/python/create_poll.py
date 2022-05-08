import requests

ENDPOINT = "https://api.strawpoll.com/v3"
API_KEY = "YOUR_API_KEY"

payload = {
	"title": "Is this a good Python example?",
	"media": None,
	"poll_options": [
		{
			"type": "text",
			"value": "Yes"
		},
		{
			"type": "text",
			"value": "No"
		},
		{
			"type": "text",
			"value": "I don't know"
		}
	],
	"poll_config": {
		"is_private": False,
		"vote_type": "default",
		"allow_comments": True,
		"allow_indeterminate": False,
		"allow_other_option": False,
		"custom_design_colors": None,
		"deadline_at": None,
		"duplication_checking": "ip",
		"allow_vpn_users": False,
		"edit_vote_permissions": "nobody",
		"force_appearance": None,
		"hide_participants": False,
		"is_multiple_choice": False,
		"multiple_choice_min": None,
		"multiple_choice_max": None,
		"number_of_winners": 1,
		"randomize_options": False,
		"require_voter_names": False,
		"results_visibility": "always",
		"use_custom_design": False
	},
	"poll_meta": {
		"description": "I don't write much Python myself.",
		"location": None,
	},
	"type": "multiple_choice",
}

response = requests.post(ENDPOINT + '/polls', json = payload, headers = { 'X-API-KEY': API_KEY })

if response:
	poll = response.json() # response is Poll object
	print(poll["url"])
else:
	error = response.json()
	print(error)
