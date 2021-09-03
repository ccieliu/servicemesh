'''
Author: your name
Date: 2021-09-02 13:39:32
LastEditTime: 2021-09-02 17:39:23
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /mesh_demo/web.py
'''
from flask import Flask
from flask_restful import Resource, Api, reqparse
import os
import grpc

import helloworld_pb2
import helloworld_pb2_grpc
import requests
app = Flask(__name__)
api = Api(app)


class ResponseVersion(Resource):
    def get(self):

        with grpc.insecure_channel('grpc-backend-svc:50051') as channel:
            stub = helloworld_pb2_grpc.GreeterStub(channel)
            response = stub.SayHello(helloworld_pb2.HelloRequest(name='v1.0'))


        res = requests.get('http://http-backend-svc/').json()
        responseDic = {
            'web-version': os.environ['APP_VERSION'],
            'http-backend': {'hostname': res['hostname'],
                             'version': res['version']},
            'grpc-backend': {
                'hostname': response.message.split(',')[0],
                'version': response.message.split(',')[1],
            },
        }

        return responseDic


api.add_resource(ResponseVersion, '/getinfo')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
