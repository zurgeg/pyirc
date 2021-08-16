API Reference 
==============  
.. py:class:: Client
  Class for interfacing with IRC in a low-level way.

  .. py:method:: Client.join_channel(channel : string) -> None
    Joins a channel.
    :async:
    :param str channel: The channel to join
    :return: None.
    :rtype: NoneType

  .. py:method:: Client.ping() -> None
    Tells the server the client is still connected
    :async:
    :return: None.
    :rtype: NoneType

  .. py:method:: Client.get_msg() -> :class:`Message` or None
    Gets the latest message.
    :async:
    :return: A message class, or None if there were no messages.
    :rtype: Message or NoneType

  py:meth:`Client.join_channel`
  
  py:meth:`Client.ping`
  
  py:meth:`Client.get_msg`
    
.. py:class:: Bot
  Not yet documented.


