import sys

from constants import VALID_SERVICES, VALID_ACTIVITIES
from errors.errors.argument_variable_errors import ArgumentVariableError
from errors.exceptions.argument_variable_exceptions import InvalidArgumentLengthException
from errors.exceptions.argument_variable_exceptions import InvalidServiceException
from errors.exceptions.argument_variable_exceptions import InvalidActivityException


def main():
	"""
		** entry point of this stream-service **
		1). start stream server ===> python main.py
		2). provide options from command line for various other options
			a). start/stop producer for a certain stream and a topic ===> python main.py producer start/stop
			[stream-name] [topic-name]
			b). start/stop consumer for a certain stream and a topic ===> python main.py consumer start/stop
			[stream-name] [topic-name]
			c). create/delete stream(s) ===> python main.py stream create/delete [stream-name]
			d). create/delete topic(s) on a certain stream ===> python main.py topic create/delete [stream-name]
			[topic-name]
			e). list all topics on a certain stream ===> python main.py topic list [stream-name]
			f). modify retention time on a certain stream on a certain topic ===> python main.py topic retention
			[stream-name] [topic-name] [new-retention-time]
	"""

	args = sys.argv[2:]
	if not args:
		# TO-DO: instantiate or get singleton object of server
		print('starting server...')
	else:
		if len(args) < 2:
			issue = ArgumentVariableError.INVALID_ARGUMENTS_LENGTH.name
			help = ArgumentVariableError.INVALID_ARGUMENTS_LENGTH.value
			data = {'data': args}

			raise InvalidArgumentLengthException(issue, help, data)
		else:
			service, activity = args[:2]
			extras = args[2:]

			# TO-DO: open a new validationBase class and derived validationClasses, implement a common method to
			# throw error and validation flow
			validate_service(service, args)
			validate_activity(activity, service, args)
			validate_extras(activity, service, extras, args)

			# TO-DO: global constants will define all activities from something like enum which will map to
			# activities implementations


def validate_service(service, args):
	if service not in VALID_SERVICES:
		issue = ArgumentVariableError.INVALID_SERVICE.name
		help = ArgumentVariableError.INVALID_SERVICE.value
		data = {'data': args}

		raise InvalidServiceException(issue, help, data)


def validate_activity(service, activity, args):
	if VALID_ACTIVITIES[service].get(activity):
		issue = ArgumentVariableError.INVALID_ACTIVITY.name
		help = ArgumentVariableError.INVALID_ACTIVITY.value
		data = {'data': args}

		raise InvalidActivityException(issue, help, data)


def validate_extras(service, activity, extras, args):
	# TO-DO: implement validation according to length of args
	pass


if __name__ == '__main__':
	main()
