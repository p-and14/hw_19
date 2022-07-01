import sqlalchemy
from flask import request
from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from implemented import director_service
from helpers.decorators import auth_required, admin_required

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        rs = director_service.get_all()
        res = DirectorSchema(many=True).dump(rs)

        return res, 200

    @admin_required
    def post(self):
        try:
            req_json = request.json
            director_service.create(req_json)
        except TypeError:
            return "Переданы неправильные ключи"

        return "Режиссёр добавлен", 201


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    @auth_required
    def get(self, rid):
        r = director_service.get_one(rid)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200

    @admin_required
    def put(self, did):
        req_json = request.json
        req_json["id"] = did
        try:
            director_service.update(req_json)
        except AttributeError:
            return f"Режиссёр с ID: {did} не найден"

        return "", 204

    @admin_required
    def delete(self, did):
        try:
            director_service.delete(did)
        except sqlalchemy.orm.exc.UnmappedInstanceError:
            return f"Режиссёр с ID: {did} не найден"

        return "", 204
