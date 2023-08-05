from ServerManagerSupport.events import *
from ServerManagerSupport.exceptions import *


class EventManager:
    def __init__(self, event_handlers):
        if not event_handlers.get('CloseEvent', None):
            raise NoCloseEvent()

        self.event_handlers = event_handlers

    async def handle_event(self, event_data):
        if event_data:
            event_class = EVENTS.get(event_data['event_type'])

            if event_class:
                event = event_class(event_data)
                handler = self.event_handlers.get(event.get_name())

                if handler:
                    response = await handler(event)

                    if not issubclass(type(response), BaseEvent):
                        response = BaseEvent()

                    response.load(event)
                    return response
