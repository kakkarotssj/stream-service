from errors.errors import StreamManagerError
from errors.exceptions import StreamAlreadyExistsException
from errors.exceptions import StreamDoesNotExistsException


class StreamManager:
    stream_data = {}
    error = StreamManagerError

    def add_stream(self, stream):
        if self.stream_data.get(stream):
            self.error.raise_exception(
                self.error.STREAM_ALREADY_EXISTS,
                {'data': self.stream_data},
                StreamAlreadyExistsException
            )
        else:
            self.stream_data[stream] = stream

    def delete_stream(self, stream):
        if self.stream_data.get(stream):
            self.stream_data.pop(stream)
        else:
            self.error.raise_exception(
                self.error.STREAM_DOES_NOT_EXISTS,
                {'data': self.stream_data},
                StreamDoesNotExistsException
            )

    def retrieve_streams(self):
        return self.stream_data.values()
