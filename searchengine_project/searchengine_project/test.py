from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['search_engine_2']
collection = db['searchengineapp_document']

# Query the collection to retrieve documents
query = { "positional_index": { "$exists": True } }
documents_cursor = collection.find(query)

# Extract documents into a list
retrieved_documents = list(documents_cursor)

# Now retrieved_documents contains the list of documents retrieved from MongoDB
print(retrieved_documents)
