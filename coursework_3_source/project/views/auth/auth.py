from flask import request
from flask_restx import Resource, Namespace
from project.setup.api.models import user
from project.container import auth_service, user_service

auth_ns = Namespace('auth')

@auth_ns.route('/register')
class AuthsView(Resource):
    @auth_ns.marshal_with(user, as_list=True, code=200, description='OK')
    def post(self):
        data = request.json

        if data.get('email') and data.get('password'):
            return user_service.create_user(data.get('email'), data.get('password')), 201

        else:
            return 'Someone else', 401

@auth_ns.route('/login/')
class LoginView(Resource):


    @auth_ns.response(404, 'Not Found')
    def post(self):
        data = request.json

        if data.get('email') and data.get('password'):
            return user_service.check(data.get('email'), data.get('password')), 201

        else:
            return 'Someone else', 401

    @auth_ns.response(404, 'Not Found')
    def put(self):
        data = request.json

        if data.get('access_token') and data.get('refresh_token'):
            return user_service.update_token(data.get('refresh_token')), 201

        else:
            return 'Someone else', 401
