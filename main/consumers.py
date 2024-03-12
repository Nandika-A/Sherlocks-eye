from channels.generic.websocket import AsyncJsonWebsocketConsumer
from .views import get_llm_output
#web socket
class PracticeConsumer(AsyncJsonWebsocketConsumer):

      async def connect(self):
           await self.accept()

      async def receive(self, text_data=None, bytes_data=None, **kwargs):
            #get message and send to llm
            await self.send(get_llm_output(text_data))
            if text_data == 'PING':
                 await self.send('PONG')
