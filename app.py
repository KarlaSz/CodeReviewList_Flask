from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

#random (not for pdoruction, because we can lost user session)
#Secret key for flashing messages (important for security)
app.secret_key = os.urandom(24)

#db setup
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "todo.db")}'
db = SQLAlchemy(app)

# Inicialization Flask-Migrate, connecting app with db
migrate = Migrate(app, db)

#object aplication to interactions
#model, class which represent db table
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    priority = db.Column(db.String, nullable=False) #priority column

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'priority': self.priority}

#start app, get and show items
@app.route('/', methods=['GET', 'POST'])
def todo():
    error_message = None
    if request.method == 'POST':
        task_name = request.form['task']
        task_priority = request.form['priority'] #getting priority from form

        existing_task = Task.query.filter_by(name=task_name).first()

        # check if task exist with the same name
        if existing_task:
            # Show flash message if task with the same name already exists
            flash('Zadanie o tej nazwie już istnieje!', 'danger')
            return redirect(url_for('todo'))  # redirect to same page

        # check if task is not empty
        if task_name.strip():
            task = Task(name=task_name, priority=task_priority)
            db.session.add(task)
            db.session.commit()
            return redirect(url_for('todo'))  # redirect to home page



    tasks = Task.query.all()
    return render_template('todo.html', tasks=tasks)

#GET endpoint - info about all tasks
@app.route('/api/task', methods=['GET'])
def list_task():
    tasks = Task.query.all()
    tasks_data = [task.to_dict() for task in tasks]
    return jsonify(tasks_data)

#POST EP - creating new task
@app.route('/api/task', methods=['POST'])
def create_task():
    task_name = request.json['name']
    task = Task(name=task_name)
    db.session.add(task)
    db.session.commit()
    response_data = jsonify(task.to_dict())
    return make_response(response_data, 201)

#GET EP - details about 1 task
@app.route('/api/task/<int:task_id>', methods=['GET'])
def task_details(task_id):
    task = Task.query.get(task_id)
    if task is None:
        return make_response('', 404)
    else:
        return jsonify(task.to_dict())

#delete item EP
@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('todo'))

#edit item EP
@app.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)

    if request.method == 'POST':
        task.name = request.form['task']  # change item name
        db.session.commit()
        return redirect(url_for('todo'))  # after saving back to home page

    return render_template('edit_task.html', task=task)

#debugging for testing
if __name__ == '__main__':
    app.run(debug=True)
