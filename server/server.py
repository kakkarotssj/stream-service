from .utils import Singleton
from .data import StreamManager
from .data import TopicManager
from errors.errors import StreamManagerError
from errors.exceptions import StreamDoesNotExistsException


def validate_stream_exists(func):
    def wrapper(*args, **kwargs):
        server = Server()
        if not server.stream_exists(kwargs.get('stream')):
            error = StreamManagerError
            exception = StreamDoesNotExistsException
            error.raise_exception(
                error.STREAM_DOES_NOT_EXISTS,
                {'data': server.retrieve_streams()},
                exception
            )

        return func(*args, **kwargs)

    return wrapper


class Server(metaclass=Singleton):
    def __init__(self):
        self.stream_manager = StreamManager()
        self.topic_manager = TopicManager()

    # stream related methods
    def add_stream(self, stream):
        self.stream_manager.add_stream(stream)

    def delete_stream(self, stream):
        self.stream_manager.delete_stream(stream)

    def retrieve_streams(self):
        return self.stream_manager.retrieve_streams()

    def get_stream(self, stream):
        return self.stream_manager.get_stream(stream)

    def stream_exists(self, stream):
        return self.stream_manager.stream_exists(stream)

    # topic related methods
    @validate_stream_exists
    def add_topic(self, stream=None, topic=None):
        self.topic_manager.add_topic(stream, topic)

    @validate_stream_exists
    def delete_topic(self, stream=None, topic=None):
        self.topic_manager.delete_topic(stream, topic)

    @validate_stream_exists
    def retrieve_topics_on_stream(self, stream=None):
        return self.topic_manager.retrieve_topics_on_stream(stream)
