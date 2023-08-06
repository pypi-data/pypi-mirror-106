# pybsub
## features
- [X] ipc
- [x] small (< 100 sloc)
- [x] no external dependencies (not even imports)
## example
```python
from pybsub import PubSub

ps = PubSub()

# the channel we will subscribe to
c = "test"
# the callback function that will be fired
# when a message has been published on the
# channel we subscribed to
cb = lambda msg: print(msg)

# various ways of subscribing to a channel
# note that it returns an integer
# you will want to save this if you want to
# remove the callback later on
k = ps.subscribe(c, cb)
# or 
k = ps.sub(c, cb)
# or
k = ps.s(c, cb)

# various ways of publishing
ps.publish(c, "somedata")
# or
ps.pub(c, {"some": "data"})
# or
ps.p(c, b"somedata")

# various ways of unsubscribing
# we will use the integer we received from
# subscribing here again
ps.unsubscribe(c, k)
# or
ps.unsub(c, k)
# or 
ps.u(c, k)

# you could also just clear all subscriptions
ps.clear()

# or you could clear all subscriptions on a channel
ps.clear_channel()
```