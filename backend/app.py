from flask import Flask
from database.db import initialize_db
from flask_restful import Api
from resources.routes import initialize_routes

app = Flask(__name__)
api = Api(app)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb+srv://filo123:drobcek123Drobcek@cluster0-hluxw.gcp.mongodb.net/test?retryWrites=true&w=majority'
}

initialize_db(app)
initialize_routes(api)
#app.register_blueprint(markers)

app.run()














# from flask import Blueprint, request, Flask, Response
# from database.db import initialize_db
# from database.models import Marker

# uri ='mongodb+srv://filo123:drobcek123Drobcek@cluster0-hluxw.gcp.mongodb.net/test?retryWrites=true&w=majority'
# @main.route('/markers')
# def get_events():
#     markers = Marker.objects().to_json()
#     return Response(markers, mimetype="application/json", status=200)

# +@app.route('/markers')
# +def get_markers():
# +    markers = Marker.objects().to_json()
# +    return Response(markers, mimetype="application/json", status=200)


# @main.route('/event', methods=['POST'])
# def add_event():
#     event = mongo.db.event

#     lat = request.json['lat']
#     lon = request.json['lon']

#     event_id = event.insert({'lat': lat, 'lon': lon})
#     new_event = event .find_one({'_id': event_id})

#     output = {'lat': new_event['lat'], 'lon': new_event['lon']}

#     return jsonify({'result': output})


# @main.route('/event/<id>', methods=['GET'])
# def get_event():
#     pass


# @main.route('/event/<id>/img', methods=['GET', 'POST'])
# def image():
#     if 'image' in request.files:
#         image = request.files['image']  # binary data
#         mongo.save_file(image.filename, image)
#         mongo.db.users.insert({'username': request.form.get()})
