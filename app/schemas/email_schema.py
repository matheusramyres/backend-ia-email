from pydantic import BaseModel

class EmailTextRequest(BaseModel):
    text: str
