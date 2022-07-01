import sqlalchemy
from flask import request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from helpers.decorators import auth_required, admin_required
from implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        rs = genre_service.get_all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200

    @admin_required
    def post(self):
        try:
            req_json = request.json
            genre_service.create(req_json)
        except TypeError:
            return "Переданы неправильные ключи"

        return "Жанр добавлен", 201


@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    @auth_required
    def get(self, rid):
        r = genre_service.get_one(rid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200

    @admin_required
    def put(self, gid):
        req_json = request.json
        req_json["id"] = gid
        try:
            genre_service.update(req_json)
        except AttributeError:
            return f"Режиссёр с ID: {gid} не найден"

        return "", 204

    @admin_required
    def delete(self, gid):
        try:
            genre_service.delete(gid)
        except sqlalchemy.orm.exc.UnmappedInstanceError:
            return f"Режиссёр с ID: {gid} не найден"

        return "", 204
