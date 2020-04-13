from flask import Response, request
from flask_restful import Resource
from database.models import Marker, User
from flask_jwt_extended import jwt_required, get_jwt_identity


class MarkersApi(Resource):
    def get(self):
        markers = Marker.objects().to_json()
        return Response(markers, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        user_id = get_jwt_identity()
        body = request.get_json()
        user = User.objects.get(id=user_id)
        marker = Marker(**body, added_by=user)
        marker.save()
        user.update(push__markers=marker)
        user.save()
        id = marker.id
        return {'id': str(id)}, 200


class MarkerApi(Resource):
    @jwt_required
    def put(self, id):
        user_id = get_jwt_identity()
        marker = Marker.objects.get(id=id, added_by=user_id)
        body = request.get_json()
        Marker.objects.get(id=id).update(**body)
        return '', 200

    @jwt_required
    def delete(self, id):
        user_id = get_jwt_identity()
        marker = Marker.objects.get(id=id, added_by=user_id)
        marker.delete()
        return '', 200

    def get(self, id):
        markers = Marker.objects(id=id).to_json()
        return Response(markers, mimetype="application/json", status=200)


# @markers.route('/markers')
# def get_markers():
#     markers = Marker.objects().to_json()
#     return Response(markers, mimetype="application/json", status=200)

# @markers.route('/markers', methods=['POST'])
# def add_marker():
#     body = request.get_json()
#     marker =  Marker(**body).save()
#     id = marker.id
#     return {'id': str(id)}, 200

# @markers.route('/markers/<id>', methods=['PUT'])
# def update_marker(id):
#     body = request.get_json()
#     Marker.objects.get(id=id).update(**body)
#     return '', 200

# @markers.route('/markers/<id>', methods=['DELETE'])
# def delete_marker(id):
#     marker = Marker.objects.get(id=id).delete()
#     return '', 200

# @markers.route('/markers/<id>')
# def get_marker(id):
#     markers = Marker.objects.get(id=id).to_json()
#     return Response(markers, mimetype="application/json", status=200)
