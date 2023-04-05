from pymongo import MongoClient
from bson.objectid import ObjectId

class bookModel:
    def __init__(self, database):
        self.db = database
        self.collection = database.collection

    def create_book(self, _id: int, titulo: str, autor: str, ano: int, preco: int) -> str:
        try:
            result = self.collection.insert_one({"_id": _id, "titulo": titulo, "autor": autor, "ano": ano, "preco": preco})
            print(f"Book {titulo} created with _id: {_id}")
            return _id
        except Exception as error:
            print(f"An error occurred while creating book: {error}")
            return None

    def read_book_by_id(self, _id: int) -> dict:
        try:
            book = self.collection.find_one({"_id": ObjectId(_id)})
            if book:
                print(f"book found: {book}")
                return book
            else:
                print(f"No book found with _id {_id}")
                return None
        except Exception as error:
            print(f"An error occurred while reading book: {error}")
            return None

    def update_book(self, _id: int, titulo: str, autor: str, ano: int, preco: int) -> int:
        try:
            result = self.collection.update_one({"_id": ObjectId(_id)}, {"$set": {"_id": _id, "titulo": titulo, "autor": autor, "ano": ano, "preco": preco}})
            if result.modified_count:
                print(f"book {_id} updated with name {titulo}, author {autor}, ano {ano} and price {preco} !")
            else:
                print(f"No book found with _id {_id}")
            return result.modified_count
        except Exception as error:
            print(f"An error occurred while updating book: {error}")
            return None

    def delete_book(self, _id: int) -> int:
        try:
            result = self.collection.delete_one({"_id": ObjectId(_id)})
            if result.deleted_count:
                print(f"book {_id} deleted !")
            else:
                print(f"No book found with _id {_id}")
            return result.deleted_count
        except Exception as error:
            print(f"An error occurred while deleting book: {error}")
            return None