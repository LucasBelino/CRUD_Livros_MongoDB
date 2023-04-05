from model import PersonModel;

db = DataBase(database='relatorio5', collection='relatorio')
db.reset_database()
person_model = PersonModel(db)




