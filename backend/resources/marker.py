from flask import Response, request
from database.models import Marker
from flask_restful import Resource


class MarkersApi(Resource):
    def get(self):
        markers = Marker.objects().to_json()
        return Response(markers, mimetype="application/json", status=200)

    def post(self):
        body = request.get_json()
        marker = Marker(**body).save()
        id = marker.id
        return {'id': str(id)}, 200

class MarkerApi(Resource):
    def put(self, id):
        body = request.get_json()
        Marker.objects.get(id=id).update(**body)
        return '', 200

    def delete(self, id):
        marker = Marker.objects.get(id=id).delete()
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
