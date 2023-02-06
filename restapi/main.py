import csv
import os
import json
# Create a list of dictionaries
tasks = []

class Task:
    def __init__(self):
        self.data = []
        current_directory = os.getcwd()
        list_length = len(tasks)
        if list_length == 0:
            with open(current_directory + '/restapi/movies.csv', 'r') as file:
                reader = csv.reader(file)
                headers = next(reader)
                for row in reader:
                    # Create a dictionary for each row, mapping the headers to the values
                    row_data = dict(zip(headers, row))
                    # Add a new dictionary to the list
                    self.data.append(row_data)
                    
    def __init__(self, data):
        self.data = data

    # def read_csv_file():
    #     current_directory = os.getcwd()
    #     # Read the CSV file
    #     list_length = len(tasks)
    #     if list_length == 0:
    #         with open(current_directory + '/restapi/movies.csv', 'r') as file:
    #             reader = csv.reader(file)
    #             headers = next(reader)
    #             for row in reader:
    #                 # Create a dictionary for each row, mapping the headers to the values
    #                 row_data = dict(zip(headers, row))
    #                 # Add a new dictionary to the list
    #                 tasks.append(row_data)
    #     else:
    #         return tasks
    #     return tasks

    # def get_tasks():
    #     # :Load data 
    #     read_csv_file()
    #     return jsonify({'tasks': tasks})

# @app.route('/tasks/<int:task_id>', methods=['GET'])
    def get_task(self,task_id):
        task = [task for task in tasks if task['id'] == task_id]
        if len(task) == 0:
            return {
                'statusCode': 200,
                'body': json.dumps({"status": "done", "message": "task not found"})
            }
        return {
                'statusCode': 200,
                'body': json.dumps({"tasks": self.data})
            }

# @app.route('/tasks', methods=['POST'])
    def create_task(self, task):
        # :Load data 
        if not task:
            return {
                'statusCode': 400,
                'body': json.dumps({"status": "error", "message": "body data is empty"})
            }

        id = int(tasks[-1]["id"]) +1
        task = {
            'id': id,
            'name': task['name'],
            'description':task('description', ""),
            'category' :task('category', ""),
            'director' :task('director', ""),
            'income' :task('income', ""),   
            'invest' :task('invest', ""),   
            'location' :task('location', ""),     
            'percentage': task('percentage', ""),     
            'rating': task('rating', ""),   
            'revenue': task('revenue', ""),     
        }
        tasks.append(task)
        return {
                'statusCode': 200,
                'body': json.dumps({"task": task})
            }

# @app.route('/tasks/<int:task_id>', methods=['PUT'])
    def update_task(self,task_id, task):
        # :Load data 
        task = [task for task in self.data if task['id'] == task_id]
        if len(task) == 0:
            return {
                'statusCode': 200,
                'body': json.dumps({"status": "done", "message": "task not found"})
            }
        if not task:
             return {
            'statusCode': 404,
            'body': {'message': 'Bad request'}
        } 
                
        task[0]['name'] = task['name']
        task[0]['description'] = task['description']
        task[0]['category'] = task['category']
        task[0]['director'] = task['director']
        task[0]['income'] = task['income']
        task[0]['invest'] = task['invest']
        task[0]['location'] = task['location']   
        task[0]['percentage'] = task['percentage']
        task[0]['rating'] = task['rating']
        task[0]['revenue'] = task['revenue'] 
        return {
            'statusCode': 200,
            'body': task
        } 

# @app.route('/tasks/<int:task_id>', methods=['DELETE'])
    def delete_task(self,task_id):
        # :Load data 
        task = [task for task in self.data if task['id'] == task_id]
        if len(task) == 0:
            return {
            'statusCode': 200,
            'body': json.dumps({"status": "error", "message": "task not found"})
        } 
            return jsonify(), 404
        tasks.remove(task[0])
        return  {
            'statusCode': 200,
            'body': json.dumps({"status": "done", "message": "tasked"})
        } 

# if __name__ == '__main__':
#     app.run()


def lambda_handler(event, context):
    api = Task()
    if event['httpMethod'] == 'POST':
        item_id = event['pathParameters']['item_id']
        body = json.loads(event['body'])
        result = api.update_task(item_id, body)
    elif event['httpMethod'] == 'GET':
        item_id = event['pathParameters']['item_id']
        result = api.get(item_id)
    elif event['httpMethod'] == 'PUT':
        item_id = event['pathParameters']['item_id']
        body = json.loads(event['body'])
        result = api.put(item_id, body)
    elif event['httpMethod'] == 'DELETE':
        item_id = event['pathParameters']['item_id']
        result = api.delete(item_id)
    else:
        result = {"status": "error", "message": "invalid request type"}

    return {
        'statusCode': 200,
        'body': json.dumps(result)
    }

    # return app(event, context)
  

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


# rom flask import Flask, jsonify, request

# app = Flask(__name__)

# tasks = []

# @app.route('/tasks', methods=['GET'])
# def get_tasks():
#     return jsonify({'tasks': tasks})

# @app.route('/tasks/<int:task_id>', methods=['GET'])
# def get_task(task_id):
#     task = [task for task in tasks if task['id'] == task_id]
#     if len(task) == 0:
#         return jsonify({'message': 'Task not found'})
#     return jsonify({'task': task[0]})

# @app.route('/tasks', methods=['POST'])
# def create_task():
#     task = {
#         'id': tasks[-1]['id'] + 1 if len(tasks) > 0 else 1,
#         'title': request.json['title'],
#         'description': request.json.get('description', ""),
#         'done': False
#     }
#     tasks.append(task)
#     return jsonify({'task': task}), 201

# @app.route('/tasks/<int:task_id>', methods=['PUT'])
# def update_task(task_id):
#     task = [task for task in tasks if task['id'] == task_id]
#     if len(task) == 0:
#         return jsonify({'message': 'Task not found'})
#     task = task[0]
#     task['title'] = request.json.get('title', task['title'])
#     task['description'] = request.json.get('description', task['description'])
#     task['done'] = request.json.get('done', task['done'])
#     return jsonify({'task': task})

# @app.route('/tasks/<int:task_id>', methods=['DELETE'])
# def delete_task(task_id):
#     task = [task for task in tasks if task['id'] == task_id]
#     if len(task) == 0:
#         return jsonify({'message': 'Task not found'})
#     tasks.remove(task[0])
#     return jsonify({'message': 'Task deleted'})

# def lambda_handler(event, context):
#     return app(event, context)