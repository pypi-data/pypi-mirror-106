#  MIT License
#
#  Copyright (c) 2021 Pascal Eberlein
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.


class PubSub(object):
    _subscriptions: dict

    def __init__(self):
        self._subscriptions = {}

    def has_channel(self, channel: str) -> bool:
        """
        checks if the _subscriptions variable has the channel as a key
        :param channel: str
        :rtype: bool
        :return: True if it has the channel as a key
        """
        return channel in self._subscriptions.keys()

    def channel_has_key(self, channel: str, key: int) -> bool:
        """
        :param channel: used for calling self.has_channel internally
        :param key: used for checking if this key exists
        :rtype: bool
        :return: True if the key exists in the channel
        """
        if not self.has_channel(channel):
            return False

        return key in self._subscriptions[channel].keys()

    def get_subscription_count(self, channel: str) -> int:
        """
        gets the count of keys in channel
        :param channel: str
        :rtype: int
        :return: -1 if the channel does not exist else the count of keys
        """
        if not self.has_channel(channel):
            return -1
        return len(self._subscriptions[channel].keys())

    def publish(self, channel: str, message) -> bool:
        """
        publish a message to the channel
        :param channel: str
        :param message: Any python object
        :rtype: bool
        :return: False if the channel does not exist else true
        """
        if not self.has_channel(channel):
            return False

        for sub in self._subscriptions[channel].values():
            sub(message)

        return True

    def pub(self, channel: str, msg) -> bool:
        """
        this is a shorthand function for publish
        :param channel: str
        :param msg: Any python object
        :rtype: bool
        :return: False if the channel does not exist else true
        """
        return self.publish(channel, msg)

    def p(self, channel: str, msg) -> bool:
        """
        this is a shorthand function for publish
        :param channel: str
        :param msg: Any python object
        :rtype: bool
        :return: False if the channel does not exist else true
        """
        return self.publish(channel, msg)

    def subscribe(self, channel: str, callback) -> int:
        """
        add a callback function to a channel
        :param channel: str
        :param callback: function which shall be called when new data comes in
        :rtype: int
        :return: the key, which has been assigned to the callback
        """
        if not self.has_channel(channel):
            self._subscriptions[channel] = {}

        k = self.get_subscription_count(channel) + 1
        self._subscriptions[channel][k] = callback
        return k

    def sub(self, channel: str, cb) -> int:
        """
        shorthand function for subscribe
        :param channel: str
        :param cb: function which shall be called when new data comes in
        :rtype: int
        :return: the key, which has been assigned to the callback
        """
        return self.subscribe(channel, cb)

    def s(self, channel: str, cb) -> int:
        """
        shorthand function for subscribe
        :param channel: str
        :param cb: function which shall be called when new data comes in
        :rtype: int
        :return: the key, which has been assigned to the callback
        """
        return self.subscribe(channel, cb)

    def unsubscribe(self, channel: str, key: int) -> bool:
        """
        deletes a callback by its key from a channel
        :param channel: str
        :param key: the previously obtained key
        :rtype: bool
        :return: False if the channel or key does not exist else True
        """
        if not self.channel_has_key(channel, key):
            return False

        del self._subscriptions[channel][key]
        return True

    def unsub(self, channel: str, key: int) -> bool:
        """
        shorthand function for unsubscribe
        :param channel: str
        :param key: the previously obtained key
        :rtype: bool
        :return: False if the channel or key does not exist else True
        """
        return self.unsubscribe(channel, key)

    def u(self, channel: str, key: int) -> bool:
        """
        shorthand function for unsubscribe
        :param channel: str
        :param key: the previously obtained key
        :rtype: bool
        :return: False if the channel or key does not exist else True
        """
        return self.unsubscribe(channel, key)

    def clear(self) -> None:
        """
        remove all callbacks from all channels
        """
        self._subscriptions.clear()

    def clear_channel(self, channel: str) -> bool:
        """
        remove all callbacks from a specific channel
        :param channel: str
        :rtype: bool
        :return: False if the channel does not exist else True
        """
        if not self.has_channel(channel):
            return False

        self._subscriptions[channel].clear()
        return True


__all__ = ["PubSub"]
