from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship

from api.db import Base

class Task(Base):
    __tablename__="tasks"

    id=Column(Integer,primary_key=True)
    #id=Column(Integer,primary_key=True,auto_increment=True)
    #とすることで明示的にauto_incrementを設定できる
    #auto_incrementとは、dbにコミットするときなどにdb側で数値を増加して生成してくれること
    #基本的にint型はそのまま設定されてるらしい
    
    title=Column(String(1024))
    done=relationship("Done",back_populates="task",cascade="delete")

class Done(Base):
    __tablename__="dones"

    id=Column(Integer,ForeignKey("tasks.id"),primary_key=True)
    task=relationship("Task",back_populates="done")