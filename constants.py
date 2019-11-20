VALID_SERVICES = ['producer', 'consumer', 'stream', 'topic']

VALID_ACTIVITIES = {
	'producer': ['start', 'stop'],
	'consumer': ['start', 'stop'],
	'stream': ['create', 'delete'],
	'topic': ['create', 'delete', 'list', 'retention']
}
