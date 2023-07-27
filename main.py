import sqlite3
import pymongo
from pymongo import MongoClient

# https://api.mongodb.com/python/current
# Connecting to database
client = pymongo.MongoClient("mongodb://localhost:27017/")
filter={}

result = client["Fitness_App"]["Python_Test"].find(
  filter=filter
)
db = client["Python_Test"]
collection = db["People"]
# print(db)


# Reading Database!
def read_documents(collection):
    try:
        documents = collection.find()
        for doc in documents:
            print(doc)
    except pymongo.errors.PyMongoError as e:
        print("Error reading documents:", e)
# print(read_documents(collection))

# Creating a terminal menu
def print_menu():
    print("\n===== MongoDB CRUD Operations =====")
    print("1. Create a document")
    print("2. Read all documents")
    print("3. Update a document")
    print("4. Delete a document")
    print("5. Exit")

print_menu()




# Inserting multiple documents manually
# data_list = [
#     {"name": "Brianna", "age": 27},
#     {"name": "Anthony", "age": 32}
# ]
# insert_result = collection.insert_many(data_list)
# print(db)

# The code below is a sqlite3 db with no sql file needed

# Connect to the database (it will create a new one if it doesn't exist)
# connection = sqlite3.connect('example.db')

# Create a cursor object to execute SQL commands
# cursor = connection.cursor()

# Create the 'users' table if it doesn't exist
# cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                #   (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Insert some data into the table
# cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('John Doe', 30))
# cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Jane Smith', 25))

# for row in cursor.execute("select * from users"):
    # print(row)

# Commit the changes and close the connection
# connection.commit()
# connection.close()
