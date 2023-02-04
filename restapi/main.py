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


  

#   import json
# import boto3
# from boto3.dynamodb.conditions import Key, Attr

# def lambda_handler(event, context):
#     dynamodb = boto3.resource("dynamodb")
#     table = dynamodb.Table("YourTableName")

#     if event["httpMethod"] == "GET":
#         response = table.scan()
#         return {
#             "statusCode": 200,
#             "body": json.dumps(response["Items"])
#         }
#     elif event["httpMethod"] == "POST":
#         data = json.loads(event["body"])
#         response = table.put_item(Item=data)
#         return {
#             "statusCode": 201,
#             "body": json.dumps(data)
#         }
#     elif event["httpMethod"] == "PUT":
#         data = json.loads(event["body"])
#         response = table.update_item(
#             Key={"id": event["pathParameters"]["id"]},
#             UpdateExpression="set data = :data",
#             ExpressionAttributeValues={":data": data["data"]}
#         )
#         return {
#             "statusCode": 200,
#             "body": json.dumps(data)
#         }
#     elif event["httpMethod"] == "DELETE":
#         response = table.delete_item(
#             Key={"id": event["pathParameters"]["id"]}
#         )
#         return {
#             "statusCode": 200,
#             "body": json.dumps({})
#         }
#     else:
#         return {
#             "statusCode": 400,
#             "body": json.dumps({"error": "Invalid httpMethod"})
#         }



# def lambda_handler(event, context):
#     if event['path'] == '/items':
#         if event['httpMethod'] == 'GET':
#             return get_items()
#         elif event['httpMethod'] == 'POST':
#             return create_item(event)
#     elif event['path'].startswith('/items/'):
#         item_id = event['path'].split('/')[2]
#         if event['httpMethod'] == 'GET':
#             return get_item(item_id)
#         elif event['httpMethod'] == 'PUT':
#             return update_item(item_id, event)
#         elif event['httpMethod'] == 'DELETE':
#             return delete_item(item_id)
#     else:
#         return {
#             'statusCode': 404,
#             'body': 'Not Found'
#         }

# def lambda_handler(event, context):
#     api_key = event.get('headers', {}).get('Authorization', '')
#     if api_key != 'YOUR_API_KEY':
#         return {
#             'statusCode': 401,
#             'body': 'Unauthorized'
#         }
#     # Your code here



# def lambda_handler(event, context):
#     authorization_header = event.get('headers', {}).get('Authorization', '')
#     if not authorization_header:
#         return {
#             'statusCode': 401,
#             'body': 'Unauthorized'
#         }
#     token = authorization_header.split()[1]
#     try:
#         decoded = jwt.decode(token, 'YOUR_SECRET_KEY', algorithms=['HS256'])
#     except jwt.exceptions.DecodeError:
#         return {
#             'statusCode': 401,
#             'body': 'Unauthorized'
#         }
#     # Your code here




# import boto3
# import jwt

# kms = boto3.client('kms')

# def lambda_handler(event, context):
#     authorization_header = event.get('headers', {}).get('Authorization', '')
#     if not authorization_header:
#         return {
#             'statusCode': 401,
#             'body': 'Unauthorized'
#         }
#     token = authorization_header.split()[1]
#     try:
#         # Decrypt the secret key using KMS
#         encrypted_secret_key = kms.decrypt(CiphertextBlob=b64decode(os.environ['SECRET_KEY']))['Plaintext']
#         decoded = jwt.decode(token, encrypted_secret_key, algorithms=['HS256'])
#     except jwt.exceptions.DecodeError:
#         return {
#             'statusCode': 401,
#             'body': 'Unauthorized'
#         }
#     # Your code here


rom flask import Flask, jsonify, request

app = Flask(__name__)

tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({'message': 'Task not found'})
    return jsonify({'task': task[0]})

@app.route('/tasks', methods=['POST'])
def create_task():
    task = {
        'id': tasks[-1]['id'] + 1 if len(tasks) > 0 else 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({'message': 'Task not found'})
    task = task[0]
    task['title'] = request.json.get('title', task['title'])
    task['description'] = request.json.get('description', task['description'])
    task['done'] = request.json.get('done', task['done'])
    return jsonify({'task': task})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        return jsonify({'message': 'Task not found'})
    tasks.remove(task[0])
    return jsonify({'message': 'Task deleted'})

def lambda_handler(event, context):
    return app(event, context)