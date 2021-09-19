import json
from . import satellite_utils
from channels.generic.websocket import AsyncWebsocketConsumer
from . import GROUP_NAME

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
            result = satellite_utils.solve_task(task, ERROR_MARGIN)
            await self.send(text_data=json.dumps({
                'message': self.room_name + ': '  + result + '\n'
            })) 


    async def free_tasks(self, event):
        message = event['message']
        
        await self.send(text_data=json.dumps({
            'message': message
        }))

