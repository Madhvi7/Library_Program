from fastapi import APIRouter

from Script.Schemas.library_schema import Email
from Script.core.DB.MongoDB import Book
from Script.core.Handlers.Library_handler import library_object

book_router = APIRouter()



@book_router.get("/")
def get_all_data():
    all_book = library_object.get_all_book()
    return all_book


@book_router.get("/book_based_on_id/{id}")
def get1_data(id: int):
    return library_object.get_book_id(id)



@book_router.post("/books/{book_id}")
def create_data(book_id: int, book: Book):
    all_book = library_object.create_book(book_id, book)
    return all_book

@book_router.put("/books/{book_id}")
def update_data(book: Book, book_id: int):
    all_book = library_object.update_book(book_id, book)
    return all_book


@book_router.delete("/books/{book_id}")
def delete_book(book_id: int):
    all_book = library_object.delete_book(book_id)
    return all_book


@book_router.post("/send_Email")
def email_data(email: Email):
    all_book = library_object.send_Email(email)
    return all_book
