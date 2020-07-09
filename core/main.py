from flask import Blueprint, jsonify
from .seed_geo import coordinates
from .extensions import mongo 

main = Blueprint('main', __name__)

@main.route('/seed', methods=['GET'])
def index():
    try:
        coordinates_collection = mongo.db.coordinates
        for item in coordinates():
            coordinates_collection.insert({'location' : item.name, 'lat' : str(item.geo_location['lat']), 'lng': str(item.geo_location['lng'])})
        return '<h1>Registros adicionados com sucesso!</h1>'
    except Exception as exp:
        return jsonify({"error": str(exp)})


@main.route('/list', methods=['GET'])
def list():
    try:
        cursor = mongo.db.coordinates.find()
        data = [{"location": item["location"], "lat": item["lat"], "lng": item["lng"]} for item in cursor]
        return jsonify({"data": data})

    except Exception as exp:
        return jsonify({"error": str(exp)})


@main.route('/list/<page_num>', methods=['GET'])
def list_paginate(page_num):
    try:
        page_size = 10
        skips = page_size * (int(page_num) - 1)
        cursor = mongo.db.coordinates.find().skip(skips).limit(page_size)
        data = [{"location": item["location"], "lat": item["lat"], "lng": item["lng"] }  for item in cursor]
        return jsonify({"data": data})
    except Exception as exp:
        return jsonify({"error": str(exp)})
