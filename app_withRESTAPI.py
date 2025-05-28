#app_withRESTAPI

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    done = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'done': self.done
        }

@app.route('/api/todos', methods=['GET'])
def get_todos():
    todos = Task.query.all()
    return jsonify([todo.to_dict() for todo in todos]), 200

@app.route('/api/todos/<int:id>', methods=['GET'])
def get_task(id):
    task = Task.query.get(id)
    if not task:
        return jsonify({'error': 'Task not found'}), 404
    return jsonify(task.to_dict()), 200

@app.route('/api/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'Title is required'}), 400
    todo = Task(
        title=data['title'],
        description=data.get('description', ''),
        done=data.get('done', False)
    )
    db.session.add(todo)
    db.session.commit()
    return jsonify(todo.to_dict()), 201


@app.route('/api/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    todo = Task.query.get_or_404(id)
    data = request.get_json()
    if 'title' in data:
        todo.title = data['title']
    if 'description' in data:
        todo.description = data['description']
    if 'done' in data:
        todo.done = data['done']
    db.session.commit()
    return jsonify(todo.to_dict()), 200


@app.route('/api/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = Task.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return jsonify({'message': 'Todo deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)

