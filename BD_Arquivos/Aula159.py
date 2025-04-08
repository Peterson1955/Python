import pymongo

con = pymongo.MongoClient()

db = con.cadastrodb

db.create_collection("minhacolecao2")

db.minhacolecao2.insert_one({
    'titulo':'Curso Pyton',
    'descricao': 'Curso de Python',
    'by': 'Piva Jr',
    'url': 'http://www.pypro.com.br',
    'tags': ['python', 'django', 'flask'],
    'likes': 200
    })

