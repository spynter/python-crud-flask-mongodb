from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://erwil:YMo4bHSmq9L003vc@cluster0.1srnj6u.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["bdd_productos_app"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db
