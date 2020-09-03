# see: https://lucumr.pocoo.org/2016/12/29/careful-with-str-format/

CONFIG = {
    'SECRET_KEY': 'super secret key'
}


class Event(object):
    def __init__(self, id, level, message):
        self.id = id
        self.level = level
        self.message = message


def format_event(format_string, event):
    return format_string.format(event=event)


event = Event("id", "level", "hello")
print(format_event('{event.__init__.__globals__[CONFIG][SECRET_KEY]}', event))