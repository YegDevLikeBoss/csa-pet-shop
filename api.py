from flask import Flask, jsonify
import pymongo

app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["pet-shop"]
mycol = mydb["pets"]

@app.route('/petshop/api/v1.0/allpets', methods=['GET'])
def get_pets():
    ret = []
    for x in mycol.find({}, {'_id': False}):
        ret.append(x)
    return jsonify(ret)

@app.route('/petshop/api/v1.0/pet_id/<int:pet_id>', methods=['GET'])
def get_pet_by_id(pet_id):
    ret = []
    for x in mycol.find({'pet_id': pet_id}, {'_id': False, 'pet_id': False}):
        ret.append(x)
    return jsonify(ret)

@app.route('/petshop/api/v1.0/pet_type/<string:pet_type>', methods=['GET'])
def get_pet_by_type(pet_type):
    ret = []
    for x in mycol.find({'type': pet_type}, {'_id': False, 'type': False}):
        ret.append(x)
    return jsonify(ret)

if __name__ == '__main__':
    app.run(debug=True)