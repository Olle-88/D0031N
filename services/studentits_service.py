from flask import Blueprint, jsonify
import json, os

bp = Blueprint('studentits', __name__, url_prefix='/studentits')

@bp.route('/personnummer/<anvnamn>', methods=['GET'])
def get_personnummer(anvnamn):
    path = os.path.join('data', 'studenter.json')
    with open(path, encoding='utf-8') as f:
        studenter = json.load(f)
    if anvnamn in studenter:
        return jsonify({"personnummer": studenter[anvnamn]})
    return jsonify({"fel": "Student finns ej"}), 404
