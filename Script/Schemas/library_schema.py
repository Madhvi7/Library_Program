from pydantic import BaseModel


# Model for a book
class Book(BaseModel):
    id: int
    title: str
    author: str
    borrowed: bool


class Email(BaseModel):
    Receiver_email: str
    Subject: str
