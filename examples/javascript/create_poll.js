const axios = require('axios');

const ENDPOINT = 'https://api.strawpoll.com/v3'
const API_KEY = 'YOUR_API_KEY'

let poll = {
	"title": "Is this a good JavaScript example?",
	"media": null,
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
		"vote_type": "default",
		"allow_comments": true,
		"allow_indeterminate": false,
		"allow_other_option": false,
		"custom_design_colors": null,
		"deadline_at": null,
		"duplication_checking": "ip",
		"edit_vote_permissions": "nobody",
		"force_appearance": null,
		"hide_participants": false,
		"is_multiple_choice": true,
		"multiple_choice_min": 1,
		"multiple_choice_max": 3,
		"number_of_winners": 1,
		"randomize_options": false,
		"require_voter_names": false,
		"results_visibility": "always",
		"use_custom_design": false
	},
	"poll_meta": {
		"description": "I do write some JavaScript myself.",
		"location": null,
	},
	"type": "multiple_choice",
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

