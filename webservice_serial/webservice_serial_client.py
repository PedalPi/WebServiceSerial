from tornado import gen
from tornado.ioloop import IOLoop
from tornado.tcpclient import TCPClient

from webservice_serial.protocol.message_builder import MessageBuilder


class WebServiceSerialClient(object):

    def __init__(self, address, port, encoding="utf-8"):
        self.address = address
        self.port = port
        self.encoding = encoding

        self.stream = None
        self.message_listener = lambda message: ...
        self.connected_listener = lambda: ...

    def connect(self):
        IOLoop.current().spawn_callback(lambda: self._connect())

    @gen.coroutine
    def _connect(self):
        self.stream = yield TCPClient().connect(self.address, self.port)
        self.connected_listener()

        while True:
            data = yield self.stream.read_until('\n'.encode(self.encoding))
            data = data.decode(self.encoding).strip()

            generated = MessageBuilder.generate(data)
            if generated is not None:
                self.message_listener(generated)

    def send(self, message):
        text = str(message).encode(self.encoding)
        self.stream.write(text)

    def close(self):
        if self.stream is not None:
            self.stream.close()
