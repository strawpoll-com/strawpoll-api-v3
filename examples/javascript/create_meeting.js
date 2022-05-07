const axios = require('axios');

const ENDPOINT = 'https://api.strawpoll.com/v3'
const API_KEY = 'YOUR_API_KEY'

let poll = {
	"title": "When do we meet to discuss this JavaScript example?",
	"media": null,
	"poll_options": [
		{
			"type": "date",
			"date": "2022-08-13"	// All-day option
		},
		{
			"type": "time_range",
			"start_time": 1660989600,
			"end_time": 1660993200
		},
		{
			"type": "time_range",
			"start_time": new Date('2022-08-27T12:00:00+02:00').getTime() / 1000,	// new Date() reads UTC time so it is recommended to use a timezone offset (e.g. +02:00)
			"end_time": null	// Open end
		}
	],
	"poll_config": {
		"is_private": true,
		"vote_type": "participant_grid",
		"allow_comments": true,
		"allow_indeterminate": true,
		"deadline_at": null,
		"duplication_checking": "none",
		"edit_vote_permissions": "admin_voter",
		"allow_vpn_users": true,
		"hide_participants": false,
		"is_multiple_choice": true,
		"multiple_choice_min": 0,
		"multiple_choice_max": 0,
		"require_voter_names": true,
	},
	"poll_meta": {
		"description": null,
		"location": "Online (Teams)",
		"timezone": "Europe/Berlin"		// Use null for automatic timezones
	},
	"type": "meeting",
}

axios.post(ENDPOINT + '/polls', 
	poll,
	{
		headers:
			{
				'Content-Type': 'application/json',
				'X-API-KEY': API_KEY 
			},
	}
)
.then(res => {
	console.log(res.data.url) // res.data is a Poll object
})
.catch(error => {
	console.error(error)
})
