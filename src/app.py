from flask import Flask, request, json
from flask import jsonify
app = Flask(__name__)

todos = [
    { "label": "Mi primera tarea", "done": False },
    { "label": "Mi segunda tarea", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = json.loads(request.data)
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[position]
    print("This is the position to delete: ",position)
    return jsonify(todos)   
#print(delete_todo(1))
   


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)