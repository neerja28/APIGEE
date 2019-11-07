from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
#from flask.ext.jsonpify import jsonify is Deprecated
from flask import jsonify #Use

# Connect to database
db_connect = create_engine('sqlite:///chinook.db')

#Following two lines is used to initialise the app. It is the main entry point for the appiication
app = Flask(__name__)
api = Api(app)

class Employees(Resource):
    def get(self):
        # get method needs 'self' as a parameter, since it is a class method and not a function.
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from employees") # This line performs query and returns json result
        return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches first column that is Employee ID

class Tracks(Resource):
    def get(self):
        # get method needs 'self' as a parameter, since it is a class method and not a function.
        conn = db_connect.connect()
        query = conn.execute("select trackid, name, composer, unitprice from tracks;")
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

class Employees_Name(Resource):
    def get(self, employee_id):
        # get method needs 'self' as a parameter, since it is a class method and not a function.
        conn = db_connect.connect()
        query = conn.execute("select * from employees where EmployeeId =%d "  %int(employee_id))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)

# api.add_resource Adds a resource to the api.
api.add_resource(Employees, '/employees') # Route_1: http://127.0.0.1:5002/employees
api.add_resource(Tracks, '/tracks') # Route_2: http://127.0.0.1:5002/tracks
api.add_resource(Employees_Name, '/employees/<employee_id>') # Route_3: http://127.0.0.1:5002/employees/5


if __name__ == '__main__':
     app.run(port='5002')


# Notes:
# cursor.fetchall() fetches all the rows of a query result.
# db_connect = create_engine('sqlite:///chinook.db') Or connection = sqlite3.connect('chinook.db')

# app = Flask(__name__)
# api = Api(app)
# (or)
# app = Flask(__name__)
# api = Api()
# api.init_app(app)
