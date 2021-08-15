from asyncio import get_event_loop

class AsyncSocket:
    def __init__(self, loop):
        self._loop = loop
    async def recv(self, to_recv):
        return await self._loop.sock_recv(to_recv)
    async def send(self, to_send):
        return await self._loop.sock_send(to_send)
    async def connect(self, host):
        return await self._loop.sock_connect(host)

class Message:
    def __init__(self, name, message, raw_data):
        self.name = name
        self.content = message
        self._raw_data = raw_data
    def get_raw(self):
        return self._raw_data

class Client:
    def __init__(self, host, port, nick="pyirc", password=None, server_password=None):
        self.__socket = AsyncSocket(get_event_loop())
        await self.__socket.connect((host, port))
    async def ping(self):
        await self.__socket.send(b"PONG :pingisn")
    async def join_channel(self, channelname):
        channelname = bytes(channelname, "UTF-8")
        packet = f"JOIN {channelname}n"
        await self.__socket.send(packet)
    async def send_msg(self, target, message):
        target = bytes(target, "UTF-8")
        message = bytes(message, "UTF-8")
        packet = f"PRIVMSG {target} :{message}n"
        await self.__socket.send(packet)
    async def _get_msg(self, raw):
        return await raw.decode("UTF-8").strip("nr")
    async def _get_raw(self):
        return await self.__socket.recv(2048)
    async def get_msg(self):
        msg = await self._get_msg(await self._get_raw())
        if msg.find("PRIVMSG") != 1:
            # It's a message!
            name = msg.split('!',1)[0][1:]
            message = msg.split('PRIVMSG',1)[1].split(':',1)[1]
            return Message(name, message, msg)
        else:
            return None
        

    
