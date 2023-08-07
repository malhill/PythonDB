import sqlite3
import pymongo
from pymongo import MongoClient
from tabulate import tabulate

# https://api.mongodb.com/python/current
# Connecting to database
client = pymongo.MongoClient("mongodb://localhost:27017/")
print(client)
filter={  }


result = client["Fitness_App"]["Python_Test"].find(
  filter=filter
)
db = client["Python_Test"]
collection = db["People"]
# print(collection)

# Reading Database!
def read_db(collection):
    try:
        documents = collection.find()
        for doc in documents:
            titles = [ "Name", "Age"]
            name = doc['name']
            age = doc['age'] 
            tables = tabulate(documents, showindex='never')
            # print(f'Name:{name} Age:{age}')
            print(tables)
    except pymongo.errors.PyMongoError as e:
        print("Error reading documents:", e)
# print(read_db(collection))

# Updating Database!
def update_db(collection, query, update):
    try:
        result = collection.update_one(query, {"$set": update})
        if result.modified_count > 0:
            print("Db pdated!")
        else:
            print("Nothing found.")
    except pymongo.errors.PyMongoError as e:
        print("Error updating document: ", e)
# print(update_db)


# Creating a terminal menu
def print_menu():
    print("\n======== MongoDB CRUD ========")
    print("1. Create a document")
    print("2. Read all documents")
    print("3. Update a document")
    print("4. Delete a document")
    print("5. Exit")

print_menu()
action = input("Enter your choice (1-5): ")

if action == "2":
  read_db(collection)
else:
  print_menu()  
  action 
     
if action == "3":
    name = input("Enter name in data: ")
    update_age = int(input("Enter the new age: "))
    update_name = {"name": name }
    update_age = {"age": update_age}
    update_db(collection, update_name, update_age)



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
