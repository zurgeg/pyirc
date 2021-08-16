Quickstart
==========
To begin using PyIRC, create a client:
```
from pyirc.irc import client
# Now we create the client
irc = Client("myserver.local", 1234) # Replace myserver.local with your server, and 1234 with your port
```
The next step is to create an `asyncio` mainloop, this is important because PyIRC is async.
```
async def mainloop(client):
  while True:
    await client.ping() # Ping the IRC server.
```
Now we can run it. But first, you need to import `asyncio.run` at the top of your code:
```
from asyncio import run
# ...
```
Now we can actually run the mainloop:
```
# ...
run(mainloop(irc))
```
Now, you may have noticed absolutely nothing happened! This is because your client has only connected to the server and started pinging. To join a channel, you can use :meth:`Client.join_channel`, like so:
```
# In your mainloop, above the while True loop:
await client.join_channel("#example")
```
Of course, replacing `#example` with a channel.

For more info, you can look at :class:`Client`, or use :class:`Bot` to create a more high-level bot.

