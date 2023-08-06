import pickle
import socket


class WS_Response:
    method: str
    data: dict

    def __init__(self, method, data=None):
        self.method = method
        self.data = data


class WS_Session:
    id: str
    ws_socket: socket.socket

    def __init__(self, ws_id: str, ws_socket: socket.socket):
        self.id = ws_id
        self.ws_socket = ws_socket

    def send(self, method: str, data: dict = None):
        ws_response = WS_Response(method, data)
        self.ws_socket.send(pickle.dumps(ws_response))
