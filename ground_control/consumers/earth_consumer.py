from ground_control.consumers.satellite_consumer import GROUP_NAME
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from . import GROUP_NAME
from . import earth_utils

SATELLITES = ['satellite1', 'satellite2']

class EarthConsumer(AsyncWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.channel_name = 'earth_control'

    async def connect(self):
        self.room_name = self.scope['url_route']
        self.room_group_name = GROUP_NAME

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        for satellite in SATELLITES:
            await self.channel_layer.group_add(
                satellite,
                self.channel_name
            )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = json.loads(text_data_json['message'])
        total_tasks = message['task']
        
        sorted_by_weight = earth_utils.sort_task_list(total_tasks)
        for satellite in SATELLITES:
            task, sorted_by_weight = earth_utils.distribute_tasks(sorted_by_weight)
            await self.channel_layer.group_send(
                satellite,
                {
                    'type': 'chat_message',
                    'message': 'Earth control to ' + satellite + ': \n' + str(task),
                    'tasks': task['tasks']
                }
            )
        
        if len(sorted_by_weight) > 0:
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'free_tasks',
                    'message': 'Unable to allocate: ' + str(sorted_by_weight)
                }
            )


    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

    async def free_tasks(self, event):
        message = event['message']
        
        await self.send(text_data=json.dumps({
            'message': message
        }))
    