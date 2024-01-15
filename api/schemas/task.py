from typing import Optional
from pydantic import BaseModel,Field

class TaskBase(BaseModel):
    title:Optional[str]=Field(None,example="go to cleaning")

class TaskCreate(TaskBase):
    pass

class TaskCreateResponse(TaskCreate):
    id:int

    class Config:
        orm_mode=True

class Task(TaskBase):
    id:int
    done:bool=Field(False,descreption="完了フラグ")

    class Config:
        orm_mode=True