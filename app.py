from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:your_password@localhost/devops_project'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    completed = db.Column(db.Boolean, default=False)

@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.json
    new_todo = Todo(title=data['title'])
    db.session.add(new_todo)
    db.session.commit()
    print('no print');
    return jsonify({"id": new_todo.id, "title": new_todo.title, "completed": new_todo.completed}), 201

@app.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify([{"id": todo.id, "title": todo.title, "completed": todo.completed} for todo in todos])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)