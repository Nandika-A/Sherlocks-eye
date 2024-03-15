from channels.generic.websocket import AsyncJsonWebsocketConsumer
from .views import get_llm_output, get_llm_anim_no, image_to_text
#web socket
class PracticeConsumer(AsyncJsonWebsocketConsumer):

      async def connect(self):
           await self.accept()

      async def receive(self, text_data=None, bytes_data=None, **kwargs):
            #get message and send to llm
          if text_data is not None:
               animNo = (get_llm_anim_no(text_data))
               print(animNo)
               await self.send_json({'llm_out': get_llm_output(text_data),'animNo': animNo})
          elif bytes_data is not None:
               image_data = bytes_data
               result = image_to_text(image_data)
               await self.send_json({'image_text': result})
