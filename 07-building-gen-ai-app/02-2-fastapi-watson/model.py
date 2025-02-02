from pydantic import BaseModel

class PromptMessage(BaseModel):
  prompt: str

class Message(BaseModel):
  text: str