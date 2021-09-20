from ground_control.consumers.satellite_consumer import GROUP_NAME
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from . import GROUP_NAME
from . import earth_utils



class EarthConsumer(AsyncWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.channel_name = 'earth_control'

    async def connect(self):
        self.number_of_satellites = self.scope['url_route']['kwargs']['number_of_satellites']
        self.room_name = self.scope['url_route']
        self.room_group_name = GROUP_NAME

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        for satellite in range(1, int(self.number_of_satellites) + 1):
            channel_name = 'satellite_' + str(satellite)
            await self.channel_layer.group_add(
                channel_name,
                self.channel_name
            )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    #generic message
    def message_to_group(self, group_name, message, message_type, task=''):
        return self.channel_layer.group_send(
            group_name,
            {
                'type': message_type,
                'message': message,
                'tasks': task
            }
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            message = json.loads(text_data_json['message'])

            total_tasks = message['task']
            sorted_by_weight = earth_utils.sort_task_list(total_tasks)

            for satellite in range(1, int(self.number_of_satellites) + 1):
                channel_name = 'satellite_' + str(satellite)
                task, sorted_by_weight = earth_utils.distribute_tasks(sorted_by_weight)
                message = 'Earth control to ' + channel_name + ': \n' + str(task)
                await self.message_to_group(channel_name, message, 'chat_message', task['tasks'])

            if len(sorted_by_weight) > 0:
                message = 'Unable to allocate: ' + str(sorted_by_weight)
                await self.message_to_group(self.room_group_name, message, 'free_tasks')
           
        except KeyError:
            message = 'Key error. Please check your input'
            await self.message_to_group(self.room_group_name, message, 'chat_message')

        except json.decoder.JSONDecodeError:
            message = 'JSON error! Please, check your input.'
            await self.message_to_group(self.room_group_name, message, 'chat_message')

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