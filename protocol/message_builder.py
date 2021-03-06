import json

from webservice_serial.protocol.request_message import RequestMessage
from webservice_serial.protocol.request_verb import RequestVerb


class MessageBuilder(object):
    buffer = []

    @staticmethod
    def generate(message):
        """
        :param string message: Message part
        :return RequestMessage: Message received
        """
        if message != "EOF":
            MessageBuilder.buffer.append(message)
            return None

        buffer = MessageBuilder.clean_buffer()

        verb, path = buffer[0].split(" ")
        data = buffer[1]

        verb = MessageBuilder.discover_verb(verb)

        return MessageBuilder.generate_request_message(verb, path, data)

    @staticmethod
    def clean_buffer():
        buffer = MessageBuilder.buffer
        MessageBuilder.buffer = []
        return buffer

    @staticmethod
    def discover_verb(word):
        for verb in RequestVerb:
            if verb.value == word:
                return verb

        return RequestVerb.SYSTEM

    @staticmethod
    def generate_request_message(verb, path, data):
        """
        :param RequestVerb verb: Verb
        :param string path: Path
        :param string data: Data
        :return RequestMessage: message generated
        """
        return RequestMessage(verb, path, json.loads(data))
