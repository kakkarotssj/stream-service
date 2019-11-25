from .utils import Singleton
from .data import StreamManager


class Server(metaclass=Singleton):
    def __init__(self):
        self.stream_manager = StreamManager()

    def add_stream(self, stream):
        self.stream_manager.add_stream(stream)

    def delete_stream(self, stream):
        self.stream_manager.delete_stream(stream)

    def retrieve_streams(self):
        return self.stream_manager.retrieve_streams()
