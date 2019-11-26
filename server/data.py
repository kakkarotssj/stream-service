from collections import defaultdict

from errors.errors import StreamManagerError
from errors.errors import TopicManagerError
from errors.exceptions import StreamAlreadyExistsException
from errors.exceptions import StreamDoesNotExistsException
from errors.exceptions import TopicAlreadyExistsException
from errors.exceptions import TopicDoesNotExistsException


class StreamManager:
    streams = {}
    error = StreamManagerError

    def add_stream(self, stream):
        if self.streams.get(stream):
            self.error.raise_exception(
                self.error.STREAM_ALREADY_EXISTS,
                {'data': self.streams},
                StreamAlreadyExistsException
            )

        self.streams[stream] = stream

    def delete_stream(self, stream):
        if not self.streams.get(stream):
            self.error.raise_exception(
                self.error.STREAM_DOES_NOT_EXISTS,
                {'data': self.streams},
                StreamDoesNotExistsException
            )

        self.streams.pop(stream)

    def get_stream(self, stream):
        return self.streams.get(stream)

    def retrieve_streams(self):
        return self.streams.values()

    def stream_exists(self, stream):
        return stream in self.streams.values()


class TopicManager:
    topics = defaultdict(list)
    error = TopicManagerError

    def add_topic(self, stream, topic):
        if topic in self.topics[stream]:
            self.error.raise_exception(
                self.error.TOPIC_ALREADY_EXISTS,
                {'data': self.topics},
                TopicAlreadyExistsException
            )

        self.topics[stream].append(topic)

    def delete_topic(self, stream, topic):
        if topic not in self.topics[stream]:
            self.error.raise_exception(
                self.error.TOPIC_DOES_NOT_EXISTS,
                {'data': self.topics},
                TopicDoesNotExistsException
            )

        topic_index = self.topics[stream].index(topic)
        self.topics[stream].pop(topic_index)

    def retrieve_topics_on_stream(self, stream):
        return self.topics.get(stream)
