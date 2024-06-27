from typing import Optional
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app import db

class Post(db.Model):
    __tablename__ = 'posts'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[Optional[str]] = mapped_column(String(250), nullable=True)

    def __repr__(self):
        return f'{self.author} says "{self.body}"'