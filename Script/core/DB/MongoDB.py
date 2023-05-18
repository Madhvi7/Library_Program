from fastapi import FastAPI
from Script.Schemas.library_schema import Email
from Script.Schemas.library_schema import Book
from Script.core.Handlers.Library_handler import library_object



def generate_book():
    return library_object.create_book()



def fetch_data():
    return library_object.get_all_data()



def fetch_book_id(id: int):
    return library_object.get_book_id(id)



def remove_book(book_id: int):
    return library_object.delete_book(book_id)



def send_Email(email: Email):
    return library_object.send_Email(email)
