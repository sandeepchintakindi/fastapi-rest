from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from fastapi import Depends, FastAPI, Header, HTTPException
from sqlalchemy.orm import Session
from utils.db import db_session

from user.User import User
from user.UserInput import UserInput

userRouter = InferringRouter()

@cbv(userRouter)
class UserController:
    db: Session = Depends(db_session)
    def __init__(self):
        pass

    @userRouter.get("/users/search")
    def search(self):
        try:
            data = self.db.query(User).limit(100).all()
            return {"data": data}
        except Exception as error:
            print(error)
            return { "error": error }

    @userRouter.post("/users/save")
    def save(self, user: UserInput):
        try:
            db_item = User(**user.dict())
            self.db.add(db_item)
            self.db.commit()
            self.db.refresh(db_item)
            return {"data": db_item}
        except Exception as error:
            print(error)
            return { "error": error }