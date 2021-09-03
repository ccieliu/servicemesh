'''
Author: your name
Date: 2021-09-02 14:25:18
LastEditTime: 2021-09-02 16:57:35
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /mesh_demo/http-backend.py
'''

from flask import Flask
from flask_restful import Resource, Api,reqparse
import os,socket

app = Flask(__name__)
api = Api(app)


class ResponseVersion(Resource):
    def get(self):

        responseDic={
            'hostname': socket.gethostname(),
            'version': os.environ['APP_VERSION']
        }

        return responseDic

api.add_resource(ResponseVersion, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
