import signal
import socket


class Server:
    def __init__(self, config):
        # signal.signal(signal.SIGINT, self.shutdown)

        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.serverSocket.bind((config['hostname'], config['port']))

        self.serverSocket.listen(10)

        self.__clients = {}
