from .irc import Client
from .constants import EventTypes
from asyncio import Queue, run, create_task

class Command:
    def __init__(self, cback, name):
        self._cback = cback
        self.name = name
    async def call(self, *args):
        await self._cback(*args)

class Event:
    def __init__(self, event_type, event_data):
        self.event_type = event_type
        self.event_data = event_data

class Bot:
    def __init__(self, prefix, *args, **kwargs):
        self.__client = Client(*args, **kwargs)
        self.commands = []
        self.prefix = prefix
        self._evq = Queue()
    def command(self, fn, name):
        def wrapper():
            self.commands.append(Command(fn, name))
        return wrapper
    async def handle_message(self, message):
        if message.startswith(self.prefix):
            stripped_message = message[1:].split(" ")[0]
            for command in self.commands:
                if command.name == stripped_message:
                    await command.call(*stripped_message[1:].split(" ")[1:])
    async def event_producer(self):
        raw = await self.__client._get_raw()
        message = await self.__client._get_msg(raw)
        is_message = message is not None
        if is_message:
            await self._evq.put(Event(EventTypes.MESSAGE, message))
        else:
            # Must be something else we don't know about
            await self._evq.put(Event(EventTypes.OTHER, raw))
    async def event_consumer(self):
        while True:
            event = await queue.get()
            if event.event_type == EventTypes.MESSAGE:
                await self.handle_message(event.event_data)
    async def mainloop(self):
        while True:
            producers = [asyncio.create_task(event_producer())
                 for _ in range(3)]
            consumers = [asyncio.create_task(event_consumer())
                 for _ in range(10)]
            await asyncio.gather(*producers, *consumers)

            await queue.join() 
            # Then we do it again!
    def run(self):
        run(self.mainloop)
                





