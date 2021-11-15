import pymongo

MONGO_HOST = "10.8.156.57"
MONGO_PORT = 23016
MONGO_DB   = "db_cicd"
MONGO_USER = "admin"
MONGO_PASS = "welcome2cliqr"

con = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
print(con)
db = con[MONGO_DB]
print(db)
db.authenticate(MONGO_USER, MONGO_PASS)

print(db)


