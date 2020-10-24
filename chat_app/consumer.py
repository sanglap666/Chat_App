from channels.consumer import AsyncConsumer
import asyncio
import json
from chats.models import Thread,ChatMessage
from channels.db import database_sync_to_async

class ChatConsumer(AsyncConsumer):

    async def websocket_connect(self,event):

        other_user=self.scope['url_route']['kwargs']['username']
        me = self.scope['user']
        self.thread_obj = await self.get_thread(me,other_user)
        self.chat_room= f"thread_{self.thread_obj.id}"
        await self.channel_layer.group_add(
            self.chat_room,
            self.channel_name
        )
        await self.send(
            {
                'type':'websocket.accept'
            }
        )
        print("connected",event)

    async def websocket_disconnect(self,event):
        print("disconnected",event)

    async def websocket_receive(self,event):
        front_text = event.get('text')
        #if front_text is not None:
        loaded_dict_data = json.loads(front_text)
        msg = loaded_dict_data['message']
        self.user = self.scope['user']
        await self.save_message(msg)
        my_response = {
            'message': msg,
            'username': self.user.username
        }
        await self.channel_layer.group_send(
            self.chat_room,
            {
                'type' : 'msg_send',
                'text' : json.dumps(my_response)
            }
        )
            
            
        
        print("recived",event)        

    async def msg_send(self,event):
        await self.send({
                'type':'websocket.send',
                'text': event['text']
            })    

    @database_sync_to_async
    def get_thread(self,user,other_user):
        return Thread.objects.get_or_new(user,other_user) [0] 

    @database_sync_to_async
    def save_message(self,msg):
        return  ChatMessage.objects.create(thread=self.thread_obj,user=self.user,message=msg)        