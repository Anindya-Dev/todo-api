from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import select,delete
from sqlalchemy import Boolean

app=FastAPI()

DATABASE_URL= "sqlite:///./todo.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread":False})
SessionLocal= sessionmaker(bind=engine)
Base = declarative_base()

class Todo(Base):
    __tablename__="todo"
    id = Column(Integer,primary_key=True, index=True)
    title = Column(String)
    completed = Column(Boolean)

class TodoCreate(BaseModel):
    title: str
    completed: bool

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {
        "message":"Todo API is running"
    }

@app.post("/todos")
def create_todo(todo: TodoCreate):
    db=SessionLocal()
    new_todo=Todo(title=todo.title, completed=todo.completed)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    db.close()
    return new_todo

@app.get("/todos")
def get_all_todo():
    db=SessionLocal()
    stmt=select(Todo)
    result=db.execute(stmt)
    all_todo=result.scalars().all()
    db.close()
    response=[]
    for todo in all_todo:
        response.append({
            "id":todo.id,
            "title":todo.title,
            "completed":bool(todo.completed)
        })
    return response

@app.get("/todos/{id}")
def get_specific_todo(id:int):
    db=SessionLocal()
    todo=db.get(Todo,id)
    db.close()
    return{
        "id":todo.id,
        "title":todo.title,
        "completed":bool(todo.completed)
    }

@app.put("/todos/{id}")
def mark_completed(id:int,completed:bool):
    db=SessionLocal()
    complete=db.get(Todo,id)
    if complete:
        complete.completed = completed
    db.commit()
    result={
        "id":id,
        "title":complete.title,
        "completed":bool(complete.completed)
    }
    db.close()
    return result

@app.delete("/todos/{id}")
def delete_specific_todo(id:int):
    db=SessionLocal()
    stmt=delete(Todo).where(Todo.id== id)
    db.execute(stmt)
    db.commit()
    db.close()
    return{
    "message": "Todo deleted successfully"
}
