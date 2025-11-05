# ========================================
# Epok Service – hanterar kursmoduler
# ========================================
from flask import Blueprint, jsonify
import json, os

bp = Blueprint('epok', __name__, url_prefix='/epok')

# Returnerar alla moduler för en given kurskod
@bp.route('/modul/<kurskod>', methods=['GET'])
def get_moduler(kurskod):
    path = os.path.join('data', 'moduler.json')
    with open(path, encoding='utf-8') as f:
        moduler = json.load(f)
    return jsonify(moduler.get(kurskod, []))
