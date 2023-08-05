class BaseEvent:
    def __init__(self, data=None):
        if data:
            self.app = data['app']
            self.id = data['event_id']

    def data(self):
        return {}

    def json(self):
        json_data = {'app': self.app, 'event_id': self.id, 'event_type': self.get_name()}

        data = self.data()
        if data:
            json_data.update(data)

        return json_data

    def load(self, event):
        self.app = event.app
        self.id = event.id

    def get_name(self):
        return type(self).__name__


class CloseEvent(BaseEvent):
    pass


class AppClosedEvent(BaseEvent):
    def __init__(self, by_self=False):
        self.by_self = by_self

        super().__init__()

    def data(self):
        return {'by_self': 1 if self.by_self else 0}


class HandlerNotImplementedEvent(BaseEvent):
    pass


EVENTS = dict(
    (event().get_name(), event) for event in [
        CloseEvent
    ]
)
