from flask import Flask, jsonify, request
import csv
import os

app = Flask(__name__)

# Create a list of dictionaries
tasks = []


def read_csv_file():
    current_directory = os.getcwd()
    # Read the CSV file
    list_length = len(tasks)
    if list_length == 0:
        with open(current_directory + '/restapi/movies.csv', 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            for row in reader:
                # Create a dictionary for each row, mapping the headers to the values
                row_data = dict(zip(headers, row))
                # Add a new dictionary to the list
                tasks.append(row_data)
    else:
        return tasks
    return tasks

@app.route('/tasks', methods=['GET'])
def get_tasks():
    # :Load data 
    read_csv_file()
    return jsonify({'tasks': tasks})

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({'message': 'Task not found'}), 404
    return jsonify({'task': task[0]})

@app.route('/tasks', methods=['POST'])
def create_task():
     # :Load data 
    read_csv_file()
    if not request.json or not 'name' in request.json:
        return jsonify({'message': 'Bad request'}), 400
    print(tasks)
    id = int(tasks[-1]["id"]) +1
    task = {
        'id': id,
        'name': request.json['name'],
        'description':request.json.get('description', ""),
        'category' :request.json.get('category', ""),
        'director' :request.json.get('director', ""),
        'income' :request.json.get('income', ""),   
        'invest' :request.json.get('invest', ""),   
        'location' :request.json.get('location', ""),     
        'percentage': request.json.get('percentage', ""),     
        'rating': request.json.get('rating', ""),   
        'revenue': request.json.get('revenue', ""),     
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
     # :Load data 
    read_csv_file()
    task = [task for task in tasks if int(task['id']) == task_id]
    if len(task) == 0:
        return jsonify({'message': 'Task not found'}), 404
    if not request.json:
        return jsonify({'message': 'Bad request'}), 400
            
    task[0]['name'] = request.json['name']
    task[0]['description'] = request.json.get('description', "")
    task[0]['category'] = request.json.get('category', "")
    task[0]['director'] = request.json.get('director', "")
    task[0]['income'] = request.json.get('income', "")
    task[0]['invest'] = request.json.get('invest', "")   
    task[0]['location'] = request.json.get('location', "")     
    task[0]['percentage'] = request.json.get('percentage', "")     
    task[0]['rating'] = request.json.get('rating', "")   
    task[0]['revenue'] = request.json.get('revenue', "")        
    return jsonify({'task': task})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
     # :Load data 
    read_csv_file()
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({'message': 'Task not found'}), 404
    tasks.remove(task[0])
    return jsonify({'result': 'Task deleted'})

if __name__ == '__main__':
    app.run()


  