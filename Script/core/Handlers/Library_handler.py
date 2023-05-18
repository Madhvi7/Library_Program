"""creating a class Library handler"""

from pymongo import MongoClient
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Script.Schemas.library_schema import Email
from Script.Schemas.library_schema import Book
from Script.utility.Mongo_utility import lib

class library_handler:
    """Inserting BOOK in a library"""

    def create_book(self, book_id: int, book: Book):
        """ Displaying the list of books in library """
        try:
            if list(lib.find({"id": book_id})):

                return {"error": "This ID is already present"}

            lib.insert_one(book.dict())
            return {"message": "Book is successfully Added"}

        except Exception as e:
            return {"error": str(e)}



    def get_all_book(self):
        try:
            if not list(lib.find()):
                return {"error": "No books"}
            books = lib.find()
            print(books)
            details = []
            for book in books:
                detail = {'id': book['id'], 'title': book['title'], 'author': book['author'],
                          'borrowed': book['borrowed']}
                details.append(detail)
            return {"details": details}

        except Exception as e:
            return {"error": str(e)}



    def get_book_id(self, id: int):
        """Displaying the list of books in library with provided id"""
        try:
            if not list(lib.find({"id": id})):
                return {"error":"No books with this ID"}
            book = lib.find_one({"id": id})
            detail = {'id': book['id'], 'title': book['title'], 'author': book['author'], 'borrowed': book['borrowed']}
            return {"details": detail}

        except Exception as e:
            return {"error": str(e)}



    def update_book(self, book_id: int, book: Book):
        """Updating the book details in library"""
        try:
            if list(lib.find({"id": book_id})) == []:
                return {"error":"No books with this ID"}

            lib.update_one({"id": book_id}, {"$set": book.dict()})
            return {"message": "Book updated successfully"}
        except Exception as e:
            return {"error": str(e)}



    def delete_book(self, book_id: int):
        """Deleting the book from library"""
        try:
            if not list(lib.find({"id": book_id})):
                return {"error":"No books with this ID"}
            lib.delete_one({"id": book_id})
            return {"message": "Book deleted successfully"}

        except Exception as e:
            return {"error": str(e)}

    """Sending details of library in Email"""

    def send_Email(self, email: Email):
        """Sending details of library in Email"""
        sender_Email = "madhvisingh7101998@gmail.com"
        sender_password = "qbehhlyzwgcrzvzl"
        Receiver_Email = email.Receiver_email

        message = MIMEMultipart()
        message["From"] = sender_Email
        message["To"] = Receiver_Email
        message["Subject"] = email.Subject

        books_list = list(lib.find())
        details = []
        for book in books_list:
            detail = {'id': book['id'], 'title': book['title'], 'author': book['author'], 'borrowed': book['borrowed']}
            details.append(detail)
        message.attach(MIMEText(str(details), "plain/text"))

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()

            server.login(sender_Email, sender_password)

            server.send_message(message)

            server.quit()

            return {"message": "Email sent successfully"}
        except Exception as e:

            return {"message": str(e)}



library_object = library_handler()
