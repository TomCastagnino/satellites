import json
from . import satellite_utils
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from . import GROUP_NAME
from ..models import Task

ERROR_MARGIN = 10

class SatelliteConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['satellite_name']
        self.room_group_name = GROUP_NAME
        print(self.room_name)

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    @database_sync_to_async
    def save_task(self, task, completed, satellite):
        tk = Task(name=task, assigned_to=satellite, completed=completed)
        tk.save()
        return tk

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )


    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message + '\n'
        }))       

        for task in event['tasks']:
            result, completed = satellite_utils.solve_task(task, ERROR_MARGIN)
            tk = await self.save_task(task, completed, self.room_name)
            await self.send(text_data=json.dumps({
                'message': self.room_name + ': '  + result + '\n'
            })) 
            

    async def free_tasks(self, event):
        message = event['message']
        
        await self.send(text_data=json.dumps({
            'message': message
        }))

