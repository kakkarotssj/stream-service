# list of all services provided
VALID_SERVICES = ['producer', 'consumer', 'stream', 'topic']

# list of all valid activities mapped to services
VALID_ACTIVITIES = {
	'producer': ['start', 'stop'],
	'consumer': ['start', 'stop'],
	'stream': ['create', 'delete'],
	'topic': ['create', 'delete', 'list', 'retention']
}

STREAM_TOPIC = ['stream', 'topic']

# extras available for mapped services and activities
VALID_EXTRAS = {
	'producer': {
		'start': STREAM_TOPIC,
		'stop': STREAM_TOPIC
	},
	'consumer': {
		'start': STREAM_TOPIC,
		'stop': STREAM_TOPIC
	},
	'stream': {
		'create': ['stream'],
		'delete': ['stream'],
	},
	'topic': {
		'create': STREAM_TOPIC,
		'delete': STREAM_TOPIC,
		'list': ['stream'],
		'retention': [*STREAM_TOPIC, 'new_retention_time']
	}
}
