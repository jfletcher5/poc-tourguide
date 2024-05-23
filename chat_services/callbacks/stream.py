from typing import Any, Dict, List
from uuid import UUID
# add BaseCallbackHandler to the import statement
from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.messages import BaseMessage


class   StreamingHandler(BaseCallbackHandler):
    def __init__(self, queue):
        self.queue = queue
        self.streaming_run_id = set()

    def on_chat_model_start(self, serialized, message, run_id, **kwargs):
        if serialized["kwargs"]["streaming"]:
            self.streaming_run_id.add(run_id)

    def on_llm_new_token(self, token, **kqargs):
        #send token to generator
        self.queue.put(token)

    def on_llm_end(self, response,run_id, **kwargs):
        #send end token to generator
        if run_id in self.streaming_run_id:
            self.queue.put(None)
            self.streaming_run_id.remove(run_id)


    def on_llm_error(self, error, **kqargs):
        #send error to generator
        self.queue.put(None)