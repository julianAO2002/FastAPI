#modulo de conexion pymongo
#ejecucion mongod --path path/de/la/base


from pymongo import MongoClient



#Base de datos local
#db_client = MongoClient().local

#Base de datos remota - .users la tabla de la base de datos (cambiar para usar otra tabla)
db_client = MongoClient("mongodb+srv://<user>:<pass>@fastapi.miatsb8.mongodb.net/?retryWrites=true&w=majority&appName=FastAPI").users