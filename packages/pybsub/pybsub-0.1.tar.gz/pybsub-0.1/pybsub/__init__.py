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
        return channel in self._subscriptions.keys()

    def has_key(self, channel: str, key: int) -> bool:
        if not self.has_channel(channel):
            return False

        return key in self._subscriptions[channel].keys()

    def get_subscriptions_for_channel(self, channel: str) -> int:
        if not self.has_channel(channel):
            return -1
        return len(self._subscriptions[channel].keys())

    def publish(self, channel: str, message) -> bool:
        if not self.has_channel(channel):
            return False

        for sub in self._subscriptions[channel].values():
            sub(message)

        return True

    def pub(self, channel: str, msg) -> bool:
        return self.publish(channel, msg)

    def p(self, channel: str, msg) -> bool:
        return self.publish(channel, msg)

    def subscribe(self, channel: str, callback) -> int:
        if not self.has_channel(channel):
            self._subscriptions[channel] = {}

        k = self.get_subscriptions_for_channel(channel) + 1
        self._subscriptions[channel][k] = callback
        return k

    def sub(self, channel: str, cb) -> int:
        return self.subscribe(channel, cb)

    def s(self, channel: str, cb) -> int:
        return self.subscribe(channel, cb)

    def unsubscribe(self, channel: str, key: int) -> bool:
        if not self.has_key(channel, key):
            return False

        del self._subscriptions[channel][key]
        return True

    def unsub(self, channel: str, key: int) -> bool:
        return self.unsubscribe(channel, key)

    def u(self, channel: str, key: int) -> bool:
        return self.unsubscribe(channel, key)

    def clear(self) -> None:
        self._subscriptions.clear()

    def clear_channel(self, channel: str) -> bool:
        if not self.has_channel(channel):
            return False

        self._subscriptions[channel].clear()
        return True


__all__ = ["PubSub"]
