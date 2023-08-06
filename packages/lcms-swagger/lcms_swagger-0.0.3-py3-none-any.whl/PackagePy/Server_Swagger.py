# -*- coding: utf-8 -*-
# from RecivedFile.class import sqlQuery

#############################################################################################################################
#import
#############################################################################################################################
from typing import Awaitable, DefaultDict, KeysView, Text
from requests.api import request
from requests.models import stream_decode_response_unicode
from requests.sessions import InvalidSchema
from six import viewvalues
from datetime import datetime, timedelta

import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
from flask import Flask, request
from flask_restplus import Resource, Api, reqparse, fields

import queryclass
import jwtclass
import modelclass
import pymssql
import jwt
import logging
# import json
# import requests
# import argparse

#############################################################################################################################
#api config
#############################################################################################################################
app = Flask(__name__)
api = Api(app, version='1.2', title='Swagger', description='API Server')
# ns = api.namespace('vendingmachine_api_controller', description='API Server(Python)')
app.config.SWAGGER_UI_DOC_EXPANSION = 'None'  # None, list, full
app.config.RESTPLUS_VALIDATE = True
app.config.RESTPLUS_MASK_SWAGGER = False
app.config.RESTX_MASK_SWAGGER  = False
app.config.ERROR_404_HELP = False
#############################################################################################################################
#class
#############################################################################################################################
token_class = jwtclass.Token()
query_class = queryclass.sqlQuery()

#############################################################################################################################
#swagger model 
#############################################################################################################################
model_login = api.model('login', {
    'firstclasscode': fields.String(required=True, description='회사코드'),
    'machineid': fields.String(required=True, description='자판기아이디')
})

model_vendingmachineinfo = api.model('vendingmachineinfo', {
    'firstclasscode': fields.String(required=True, description='회사코드'),
    'machineid': fields.String(required=True, description='자판기아이디')
})

model_color = api.model('rgb', {
    'red': fields.String(required=True, description='red'),
    'green': fields.String(required=True, description='green'),
    'blue': fields.String(required=True, description='blue')
})

#############################################################################################################################
#API : /vendingmachine/login
#############################################################################################################################
post_parser = reqparse.RequestParser()
post_parser.add_argument('login', type=list, help='login', location='json')
ns = api.namespace('login', description='token api')
@ns.route('/token')
@ns.doc(responses ={
    200: 'Success',
    400: 'Validation Error',
    500: 'Internal Server Error',
    600: 'Token Error',
    900: 'Exception Error'
})
class login(Resource):
    @ns.doc(body=model_login)     # @ns.doc(body=model, parser=post_parser)
    def post(self):
        """
            토큰정보 취득 유효시간 30분
            Sample
               - firstclasscode : K701(*)
               - machineid : 14(*)
               - {"firstclasscode" : "K701", "machineid": "14"}
        """
        try:
            json_data = request.json
            firstclasscode = json_data['firstclasscode']
            machineid = json_data['machineid']
            query_class = queryclass.sqlQuery()
            query_return = query_class.login(firstclasscode, machineid)
            
            if query_return == True:
                jwt_return = token_class.jwt_encode(firstclasscode, machineid)
                result = jwt_return
                return result, 200 
            else:
                result = 'Error'
                return result, 200 

        except KeyError:
            return {'result': 'ERROR_PARAMETER'}, 500

#############################################################################################################################
#API : /vendingmachine/vendingmachineinfo
#############################################################################################################################
post_parser = reqparse.RequestParser()
post_parser.add_argument('accesstoken', type=str, help='token', location='headers', required = True)
ns = api.namespace('vendingmachine', description='vendingmachine api')
@ns.route('/vendingmachineinfo')
@ns.doc(responses ={
    200: 'Success',
    400: 'Validation Error',
    500: 'Internal Server Error',
    600: 'Token Error',
    900: 'Exception Error'
})

# @ns.response(200, 'Found')
# @ns.response(404, 'Not found')
# @ns.response(500, 'Internal Error')

class goods(Resource):
    # @ns.marshal_with(schema_vendingMachineInfo)
    @ns.doc(body=model_vendingmachineinfo, parser=post_parser)
    def post(self):
        """
            자판기기본정보
            Sample
               - firstclasscode : K701(*)
               - machineid : 14(*)
               - {"firstclasscode" : "K701", "machineid": "14"}
        """
        try:
            json_data = request.json
            accesstoken = request.headers.get('accesstoken')
            firstclasscode = json_data['firstclasscode']
            machineid = json_data['machineid']

            jwt_return = token_class.jwt_decode(accesstoken)
            if jwt_return == True:
                result = jwt_return
            
            query_return = query_class.tableGoods(firstclasscode, machineid)
            result = query_return
            return result, 200

        except KeyError:
            return {'result': 'ERROR_PARAMETER'}, 500

        except jwt.ExpiredSignatureError:
            return {'message': 'EXPIRED_TOKEN'}, 600

        except jwt.DecodeError:
            return {'message': 'DECODE_ERROR'}, 600           

        except Exception as ex:   
            return {'message': ex}, 900

#############################################################################################################################
#API : /vendingmachine/color
#############################################################################################################################
post_parser = reqparse.RequestParser()
post_parser.add_argument('accesstoken', type=str, help='token', location='headers', required = True)
ns = api.namespace('test', description='API Server(Python)')
@ns.route('/color')

@ns.doc(responses ={
    200: 'Success',
    400: 'Validation Error',
    500: 'Internal Server Error',
    600: 'Token Error',
    900: 'Exception Error'
})

# @ns.response(200, 'Found')
# @ns.response(404, 'Not found')
# @ns.response(500, 'Internal Error')

class rgb(Resource):
    # @ns.marshal_with(schema_vendingMachineInfo)
    @ns.doc(body=model_color, parser=post_parser)
    def post(self):
        """
            color
            Sample
               - r : 0(*)
               - g : 0(*)
               - b : 0(*)
               - {"red" : "0", "green": "0", "blue": "0"}
        """
        try:
            json_data = request.json
            accesstoken = request.headers.get('accesstoken')
            red = json_data['red']
            green = json_data['green']
            blue = json_data['blue']

            jwt_return = token_class.jwt_decode(accesstoken)
            if jwt_return == True:
                result = jwt_return

            result = {"resultcode" : "s"}
            return result, 200

        except KeyError:
            return {'result': 'ERROR_PARAMETER'}, 500

        except jwt.ExpiredSignatureError:
            return {'message': 'EXPIRED_TOKEN'}, 600

        except jwt.DecodeError:
            return {'message': 'DECODE_ERROR'}, 600           

        except Exception as ex:   
            return {'message': ex}, 900            
#############################################################################################################################
# Web Service 
#############################################################################################################################
if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', port=5000)  # , debug=True)