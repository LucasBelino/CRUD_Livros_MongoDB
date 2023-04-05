from database import Database
from model import bookModel

db = Database(database='relatorio5', collection='relatorio')
db.reset_database()
book_model = bookModel(db)

id_livro = book_model.create_book(1, "Moby Dick", "Herman Melville", 1851, 25.0)
livro = book_model.read_book_by_id(id_livro)




