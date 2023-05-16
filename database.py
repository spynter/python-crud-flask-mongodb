from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://spynter:josea1293@cluster0.la6e0.mongodb.net/?retryWrites=true&w=majority'
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = client["bdd_productos_app"]
    except ConnectionError:
        print('Error de conexión con la bdd')
    return db