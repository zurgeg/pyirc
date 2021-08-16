API Reference 
==============  
.. class:: Client
  Class for interfacing with IRC in a low-level way.

  .. method:: Client.join_channel(channel : string) -> None
    Joins a channel.
    :async:
    :param str channel: The channel to join
    :return: None.
    :rtype: NoneType

  .. method:: Client.ping() -> None
    Tells the server the client is still connected
    :async:
    :return: None.
    :rtype: NoneType

  .. method:: Client.get_msg() -> :class:`Message` or None
    Gets the latest message.
    :async:
    :return: A message class, or None if there were no messages.
    :rtype: Message or NoneType
  :func:`Client.join_channel`
  
  :func:`Client.ping`
  
  :func:`Client.get_msg`
    
.. class:: Bot
  Not yet documented.


