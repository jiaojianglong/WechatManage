from message.base_message import BaseMessage
import requests
from settings import QAURL


class TextMessage(BaseMessage):
    
    def reply(self):
        res = requests.post(QAURL, data={"content": self.text})
        reply_msg = res.json().get("data", {}).get("answer", {}).get("answer")
        self.reply_text(reply_msg)
