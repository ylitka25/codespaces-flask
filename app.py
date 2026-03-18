from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Хранилище задач в памяти (для примера)
tasks = []
task_id_counter = 1

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Получить все задачи"""
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    """Создать новую задачу"""
    global task_id_counter
    data = request.json
    
    task = {
        'id': task_id_counter,
        'title': data.get('title'),
        'completed': False,
        'priority': data.get('priority', 'medium'),
        'dueDate': data.get('dueDate'),
        'createdAt': datetime.now().isoformat()
    }
    
    tasks.append(task)
    task_id_counter += 1
    
    return jsonify(task), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Обновить задачу (переключить выполнение)"""
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        task['completed'] = not task['completed']
        return jsonify(task)
    return jsonify({'error': 'Task not found'}), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Удалить задачу"""
    global tasks
    tasks = [t for t in tasks if t['id'] != task_id]
    return jsonify({'message': 'Task deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)