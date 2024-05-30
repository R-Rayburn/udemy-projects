from typing import Optional
from fastapi import Depends, HTTPException, APIRouter

import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from .auth import get_current_user, get_user_exception

router = APIRouter(prefix='/todos',
                   tags=['todos'],
                   responses={404: {"todo": "not found"}})

models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


class Todo(BaseModel):
    title: str
    description: Optional[str]
    priority: int = Field(ge=1, le=5, description='The priority must be between 1 and 5')
    complete: bool


@router.get('/')
async def read_all(db: Session = Depends(get_db)):
    return db.query(models.Todos).all()


@router.get('/user')
async def read_all_by_user(user: dict = Depends(get_current_user),
                           db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()
    return db.query(models.Todos).filter(models.Todos.owner_id == user.get('id')).all()


@router.get('/{todo_id}')
async def read_todo(todo_id: int,
                    user: dict = Depends(get_current_user),
                    db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()
    todo_model = db.query(models.Todos)\
        .filter(models.Todos.id == todo_id)\
        .filter(models.Todos.owner_id == user.get('id'))\
        .first()
    if todo_model is None:
        raise http_exception_todo_not_found()

    return todo_model


@router.post('/', status_code=201)
async def create_dodo(todo: Todo,
                      user: dict = Depends(get_current_user),
                      db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()
    todo_model = models.Todos()
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete
    todo_model.owner_id = user.get('id')

    db.add(todo_model)
    db.commit()

    return successful_response(status_code=201)


@router.put('/{todo_id}')
async def update_todo(todo_id: int,
                      todo: Todo,
                      user: dict = Depends(get_current_user),
                      db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()
    todo_model = db.query(models.Todos)\
        .filter(models.Todos.id == todo_id)\
        .filter(models.Todos.owner_id == user.get('id'))\
        .first()
    if todo_model is None:
        raise http_exception_todo_not_found()
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo.complete

    db.add(todo_model)
    db.commit()

    return successful_response()


@router.delete('/{todo_id}')
async def delete_todo(todo_id: int,
                      user: dict = Depends(get_current_user),
                      db: Session = Depends(get_db)):
    if user is None:
        raise get_user_exception()
    data_model = db.query(models.Todos)\
        .filter(models.Todos.id == todo_id)\
        .filter(models.Todos.owner_id == user.get('id'))\
        .first()
    if data_model is None:
        raise http_exception_todo_not_found()
    # db.query(models.Todos).filter(models.Todos.id == todo_id).delete()

    data_model.is_deleted = True
    db.add(data_model)
    db.commit()
    return successful_response()


def successful_response(status_code: int = 200):
    return {
        'status': status_code,
        'transaction': 'Successful',
    }


def http_exception_todo_not_found():
    return HTTPException(status_code=404,
                         detail='Todo not found')
