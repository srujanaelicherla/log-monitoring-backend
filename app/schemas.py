from pydantic import BaseModel

class LogCreate(BaseModel):
    level: str
    message: str

class LogResponse(BaseModel):
    id: str
    level: str
    message: str
    timestamp: str

    class Config:
        orm_mode = True