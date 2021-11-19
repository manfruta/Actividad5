from flask import Flask, request, jsonify, Response, render_template
from flask.wrappers import Response
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util
from bson.json_util import loads, dumps
from bson.objectid import ObjectId

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/myDatabase"

mongo = PyMongo(app)

@app.route('/PDF', methods=['POST'])
def PDF():

    username = request.json['username']
    password = request.json['password']
    ipee = request.json['ipee']
    So = request.json['So']
    version = request.json['version']
    if username and password and ipee and So and version:
        hashed_password = generate_password_hash(password)
        id = mongo.db.PDF.insert(
            {'username': username,'password': hashed_password, 'ipee': ipee, 'So': So, 'version': version}
        )
        response = {
            'id': str(id),
            'username': username,
            'password': hashed_password,
            'ipee': ipee,
            'So': So, 
            'version': version
        }
        return response
    else:
        return not_found()

    return {'message': 'received'}


@app.route('/PDFe', methods=['GET'])
def get_PDF():
    PDF = mongo.db.PDF.find()
    response = json_util.dumps(PDF)
    #return Response(response, mimetype='aplication/json')
    return response

@app.route('/tablita', methods=['GET'])
def get_user():
    user = mongo.db.PDF.find()
    json = dumps(user)
    guardar = loads(json)
    dato = []
    for i in guardar:
        ayuda = []
        ayuda.append(i['username'])
        ayuda.append(i['password'])
        ayuda.append(i['ipee'])
        ayuda.append(i['So'])
        ayuda.append(i['version'])
        dato.append(ayuda)
    return render_template('tabla.html', dato = dato)   


@app.errorhandler(404)
def not_found(error=None):
    response = jsonify({
        'message': 'Resource Not Found: '+ request.url,
        'status': 404
    })
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run(debug=True)