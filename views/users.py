from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from helpers.decorators import admin_required, auth_required
from implemented import user_service

user_ns = Namespace('users')


@user_ns.route('/')
class UsersView(Resource):
    @auth_required
    def get(self):
        data = user_service.get_all()
        users = UserSchema(many=True).dump(data)
        return users, 200

    def post(self):
        try:
            data = request.json
            username = data.get("username")
            if user_service.get_by_username(username):
                return "Пользователь с таким username уже существует", 400

            user_service.create(data)
        except TypeError or KeyError:
            return "Переданы неверные данные", 400

        return "Пользователь создан", 201


@user_ns.route('/<int:uid>')
class UserView(Resource):
    @auth_required
    def get(self, uid):
        user = user_service.get_one(uid)
        result = UserSchema().dump(user)
        return result, 200

    @admin_required
    def delete(self, uid):
        user_service.delete(uid)
        return "", 204
