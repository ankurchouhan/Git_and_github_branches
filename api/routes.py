from flask import Blueprint, request, jsonify
import json, os

api_blueprint = Blueprint('api', __name__)
DATA_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'todos.json')

@api_blueprint.route('/', methods=['GET'])
def get_todos():
    with open(DATA_FILE, 'r') as file:
        todos = json.load(file)
    return jsonify(todos)

@api_blueprint.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    data = request.get_json()
    item_name = data.get('itemName')
    item_description = data.get('itemDescription')

    new_item = {
        "itemName": item_name,
        "itemDescription": item_description
    }

    with open(DATA_FILE, 'r+') as file:
        todos = json.load(file)
        todos.append(new_item)
        file.seek(0)
        json.dump(todos, file, indent=4)

    # Insert into MongoDB
    todos_collection.insert_one(todo_item)

    return jsonify({"message": "Item added successfully!", "item": todo_item}), 201
