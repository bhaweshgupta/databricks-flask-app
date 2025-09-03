"""
Databricks App deployment for Flask Todo Application
"""
import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configuration for Databricks
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'databricks-todo-app-key')
# Use Databricks-compatible database path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Todo model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Todo {self.title}>'

# Routes
@app.route('/')
def index():
    todos = Todo.query.order_by(Todo.created_at.desc()).all()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    title = request.form.get('title')
    description = request.form.get('description')
    
    if not title:
        flash('Title is required!', 'error')
        return redirect(url_for('index'))
    
    todo = Todo(title=title, description=description)
    db.session.add(todo)
    db.session.commit()
    flash('Todo added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/complete/<int:id>')
def complete_todo(id):
    todo = Todo.query.get_or_404(id)
    todo.completed = not todo.completed
    db.session.commit()
    flash('Todo updated!', 'success')
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    flash('Todo deleted!', 'success')
    return redirect(url_for('index'))

# Initialize database
with app.app_context():
    db.create_all()

# This is the entry point for Databricks Apps
if __name__ == '__main__':
    # For local testing
    app.run(host='0.0.0.0', port=8080, debug=False)