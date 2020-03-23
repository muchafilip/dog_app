from .marker import MarkersApi, MarkerApi

def initialize_routes(api):
    api.add_resource(MarkersApi, '/api/markers')
    api.add_resource(MarkerApi, '/api/markers/<id>')
