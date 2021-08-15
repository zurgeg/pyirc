from socket import socket, AF_INET, SOCK_STREAM

class Message:
    def __init__(self, name, message, raw_data):
        self.name = name
        self.message = message
        self._raw_data = raw_data
    def get_raw(self):
        return self._raw_data

class Client:
    def __init__(self, host, port, nick="pyirc", password=None, server_password=None):
        self.__socket = socket(AF_INET, SOCK_STREAM)
        self.__socket.connect((host, port))
    def ping(self):
        self.__socket.send(b"PONG :pingisn")
    def join_channel(self, channelname):
        channelname = bytes(channelname, "UTF-8")
        packet = f"JOIN {channelname}n"
        self.__socket.send(packet)
    def send_msg(self, target, message):
        target = bytes(target, "UTF-8")
        message = bytes(message, "UTF-8")
        packet = f"PRIVMSG {target} :{message}n"
        self.__socket.send(packet)
    def _get_msg(self):
        return self._get_raw.decode("UTF-8").strip("nr")
    def _get_raw(self):
        return self.__socket.recv(2048)
    def get_msg(self):
        msg = self._get_msg()
        if msg.find("PRIVMSG") != 1:
            # It's a message!
            name = msg.split('!',1)[0][1:]
            message = msg.split('PRIVMSG',1)[1].split(':',1)[1]
            return Message(name, message, msg)
        else:
            return None
        

    
