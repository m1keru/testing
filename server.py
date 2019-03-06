import socketserver
import os
import socket
import logging


class Cli(object):
    def __init__(self, host, port):
        self.HOST = host
        self.PORT = port

    def send_bye(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.connect((self.HOST, self.PORT))
                sock.sendall(bytes("bye", "ascii"))
                received = str(sock.recv(1024), "ascii")
                print("response: {}".format(received))
            except socket.error as e:
                print(e)


class ForkingTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = str(self.request.recv(1024), 'ascii')
	logging.	
        response = bytes("{}: {}".format(os.getpid(), data), 'ascii')
        self.request.sendall(response)


class ForkingTCPServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


if __name__ == "__main__":

    logging.basicConfig(filename="/var/log/proxy.log", level=logging.INFO)
    HOST, PORT = "localhost", 8888
    ForkingTCPServer.server = ForkingTCPServer(
            (HOST, PORT),
            ForkingTCPRequestHandler)
    ForkingTCPServer.server.serve_forever()
