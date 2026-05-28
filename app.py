from flask import Flask, render_template, request
from pymongo import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)

# MongoDB Atlas Connection String
MONGO_URI = "mongodb+srv://ermanoj250:ermanoj250@parul.xpxgml1.mongodb.net/?appName=parul"

# Create MongoDB client
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))

# Test connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Database and Collection
db = client["flaskdb"]
collection = db["users"]

# Frontend To-Do Page
@app.route('/todo')
def todo():
    return render_template('todo.html')

# Backend API Route
@app.route('/submittodoitem', methods=['POST'])
def submit_todo():

    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')

    todo_data = {
        "itemName": item_name,
        "itemDescription": item_description
    }

    collection.insert_one(todo_data)

    return "To-Do Item Saved Successfully"

if __name__ == '__main__':
    app.run(debug=True)