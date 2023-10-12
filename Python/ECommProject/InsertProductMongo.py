from flask import Flask, request, jsonify
from pymongo import MongoClient
import pymongo

import json

#app = Flask(__name__)

# Replace the following with your actual MongoDB connection details
mongo_client = MongoClient('mongodb://localhost:27017/')




#****************** Code to insert bulk data in MONGO DB using JSON file ******************
#db = mongo_client['ecomm_noopur']
#collection = db['item_catalogue']
#file_path = 'ecommerce_data.json'
#with open(file_path, 'r') as json_file:
#    data_list = json.load(json_file)
#
##print(data_list)
#
## Ensure data_list is not empty and is a list of dictionaries
#if not data_list or not isinstance(data_list, list):
#    print("Error: Invalid or empty data_list.")
#else:
#    # Insert bulk data into the collection
#    result = collection.insert_many(data_list)
#
#result = collection.insert_many(data_list)
#
#if result.acknowledged:
#    print("Insertion successful.")
#    print("Number of documents inserted:", len(result.inserted_ids))
#else:
#    print("Insertion failed.")


#****************** Code to delete bulk data from MONGO DB ******************
#db = mongo_client['ecomm_noopur']
#collection = db['item_catalogue']
# Delete one document that matches the given condition
#result = collection.delete_one({"item_id": 1})
# Delete all documents that match the given condition
#result = collection.delete_many({"price": {"$gte": 900}})

#if result.deleted_count > 0:
#    print("Deletion successful.")
#    print("Number of documents deleted:", result.deleted_count)
#else:
#    print("Deletion failed. No matching documents found.")



#****************** Code to update bulk data from MONGO DB ******************
#db = mongo_client['ecomm_noopur']
#collection = db['item_catalogue']
# Update one document that matches the given condition
#result = collection.update_one({"item_id": 3}, {"$set": {"category": "Home"}})
# Update all documents that match the given condition
#result = collection.update_many({"rating": {"$gte": 4.5}}, {"$set": {"description": "One of the highest rated product"}})
#
#if result.modified_count > 0:
#    print("Update successful.")
#    print("Number of documents updated:", result.modified_count)
#else:
#    print("Update failed. No matching documents found.")


#****************** Code to create a new collection in MONGO DB ******************
# Replace 'your_database_name' with your desired database name
#db = mongo_client['ecomm_noopur']
# Replace 'your_collection_name' with the desired collection name
#collection_name = 'new_test_db_1'
#collection = db.create_collection(collection_name)

# Example with options:
#db = mongo_client['ecomm_noopur']
#collection_name = 'new_test_db_2'
#collection_options = {
#    'capped': True,             # Creates a capped collection (fixed-size, circular buffer)
#    'size': 100000,             # Size limit in bytes for a capped collection
#    'max': 1000                 # Maximum number of documents for a capped collection
#}
#collection = db.create_collection(collection_name, **collection_options)


#****************** Code to drop a collection in MONGO DB ******************
#db = mongo_client['ecomm_noopur']
# Replace 'your_collection_name' with the collection you want to drop
#collection_name = 'new_test_db_1'
#db.drop_collection(collection_name)



#****************** Code to Retrieve all documents from the collection in MONGO DB ******************

# Replace 'your_database_name' with your desired database name
#db = mongo_client['ecomm_noopur']
# Replace 'your_collection_name' with your desired collection name
#collection = db['item_catalogue']
# Retrieve all documents from the collection
#all_documents = collection.find()

# Display all documents
#print("All records in the collection:")
#for document in all_documents:
#    print(document)


#Conditional filter-- Numeric
# Replace 'your_database_name' with your desired database name
#db = mongo_client['ecomm_noopur']
# Replace 'your_collection_name' with your desired collection name
#collection = db['item_catalogue']
# Retrieve documents that match a specific condition (e.g., age greater than 25)
#query = {"price": {"$gt": 800}}
#filtered_documents = collection.find(query)
# Display filtered documents
#print("Filtered records in the collection:")
#for document in filtered_documents:
#    print(document)


#Conditional filter-- Numeric
# Replace 'your_database_name' with your desired database name
#db = mongo_client['ecomm_noopur']
# Replace 'your_collection_name' with your desired collection name
#collection = db['item_catalogue']

#To enable text search on a specific field, you need to create a text index on that field.
# Replace 'text_column' with the name of the text field you want to filter on
#collection.create_index([("item_name", pymongo.TEXT)])
# Replace 'search_query' with the text you want to search for
#search_query = "special"
#query = {"$text": {"$search": search_query}}

# Find documents that match the text search query
#search_results = collection.find(query)
#print("Search results:")
#for document in search_results:
#    print(document)




mongo_client.close()
