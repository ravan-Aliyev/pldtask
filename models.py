from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
import uuid
Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"
    id = Column(String(60), primary_key=True)
    name = Column(String(128), nullable=False)
    category_id = Column(String(60), ForeignKey("category.id"))
    deadline = Column(DateTime, nullable=False)
    description = Column(String(128))

    def __init__(self, name, desc, deadline, category_id):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = desc
        self.deadline = deadline
        self.category_id =category_id

class Category(Base):
    __tablename__ = "category"
    id = Column(String(60), primary_key=True)
    name = Column(String(128), nullable=False)
    tasks = relationship("Task", backref="categories", cascade="delete")
    def __init__(self):
        self.id = str(uuid.uuid4())