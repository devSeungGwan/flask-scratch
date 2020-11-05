from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Test(Resource):
    def get(self):
        return {'hello': 'world'}

api.add_resource(Test, '/')

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)