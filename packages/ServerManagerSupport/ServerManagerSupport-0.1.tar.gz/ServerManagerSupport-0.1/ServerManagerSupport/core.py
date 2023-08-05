import asyncio

import aiohttp
import requests

from ServerManagerSupport.events import AppClosedEvent
from ServerManagerSupport.event_handler import EventManager
from ServerManagerSupport.exceptions import *


class Client:
    __init_flag = False

    def __init__(self, app_name, event_handler, port=8080):
        if Client.__init_flag:
            raise ThisIsSingletonClass()

        self.__app_name = app_name
        self.__port = port

        self.__event_manager = EventManager(event_handler)

        self.__is_alive = True

        self.__client = aiohttp.ClientSession()
        self.__longpol_client = aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(40))

        Client.__init_flag = True

    @property
    def app_name(self):
        return self.__app_name

    @property
    def port(self):
        return self.__port

    @property
    def event_manager(self):
        return self.__event_manager

    async def handler(self):
        while self.__is_alive:
            try:
                response = await self.__longpol_client.post(
                    f'http://localhost:{self.__port}/apps/longpoll/',
                    params={'app': self.__app_name})

                if response.status == 200:
                    event_response = await self.__event_manager.handle_event(await response.json())

                    if event_response:
                        print(event_response)
                        if type(event_response) is AppClosedEvent:
                            self.__is_alive = False

                        await self.send_event(event_response, response=True)

                else:
                    print('SMP bad response: ', await response.text())

                response.close()

            except Exception as ex:
                print('SMP not serialized exception: ', ex)

        await self.__client.close()
        await self.__longpol_client.close()

    async def send_event(self, event, response=False):
        if not getattr(event, 'app', None):
            event.app = self.__app_name
            event.id = id(event)

        await self.__client.post(
            f'http://localhost:{self.__port}/apps/{"response" if response else "request"}/',
            params=event.json()
        )

    def send_event_sync(self, event):
        if not getattr(event, 'app', None):
            event.app = self.__app_name
            event.id = id(event)

        requests.post(f'http://localhost:{self.__port}/apps/request/', params=event.json())

    async def close(self):
        self.__is_alive = False

    def sync_close(self):
        loop = asyncio.get_event_loop()
        tasks = asyncio.wait([
            self.__client.close(),
            self.__longpol_client.close()
        ])
        loop.run_until_complete(tasks)
        loop.close()
