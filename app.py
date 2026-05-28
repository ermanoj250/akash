from pymongo import MongoClient
from pymongo.server_api import ServerApi

# MongoDB Atlas Connection String

MONGO_URI = "mongodb+srv://ermanoj250:ermanoj250@parul.xpxgml1.mongodb.net/?appName=parul"

# Create a new client and connect to the server
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

app = Flask(__name__)


client = MongoClient(MONGO_URI)

# Database and Collection
db = client["flaskdb"]
collection = db["users"]

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