from .marker import MarkersApi, MarkerApi
from .auth import SignupApi, LoginApi


def initialize_routes(api):
    api.add_resource(MarkersApi, '/api/markers')
    api.add_resource(MarkerApi, '/api/markers/<id>')
    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')
