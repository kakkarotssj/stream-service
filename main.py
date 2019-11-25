import sys

from server.server import Server
from validations.argument_variable_validations import ValidateActivity
from validations.argument_variable_validations import ValidateArgumentLength
from validations.argument_variable_validations import ValidateExtras
from validations.argument_variable_validations import ValidateService


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

	args = sys.argv[1:]
	if not args:
		server = Server()
		server.add_stream('stream-1')
		server.add_stream('stream-2')
		server.add_stream('stream-1')
		server.delete_stream('stream-3')
		streams = server.retrieve_streams()

		for stream in streams:
			print(stream)
	else:
		ValidateArgumentLength.validate(*args)

		service, activity = args[:2]
		extras = args[2:]

		ValidateService.validate(service=service)
		ValidateActivity.validate(service=service, activity=activity)
		ValidateExtras.validate(service=service, activity=activity, extras=extras)

		# TO-DO: global constants will define all activities from something like enum which will map to
		# activities implementations


if __name__ == '__main__':
	main()
