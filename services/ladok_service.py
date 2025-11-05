# ============================================
# Ladok Service – registrerar och visar resultat
# ============================================

from flask import Blueprint, request, jsonify
import json, os

bp = Blueprint('ladok', __name__, url_prefix='/ladok')

# Hjälpfunktion: läsa JSON-filen med fail-safe
def las_fil(path):
    """Läser JSON-fil och returnerar innehållet. Skapar ny fil om den saknas."""
    try:
        if not os.path.exists(path):
            with open(path, 'w', encoding='utf-8') as f:
                json.dump([], f, ensure_ascii=False, indent=2)
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        # Om filen är korrupt, starta om som tom lista
        return []

# Hjälpfunktion: skriva till JSON-fil
def skriv_fil(path, data):
    """Sparar JSON-data till fil."""
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# ============================================
# POST /ladok/resultat – registrerar nytt resultat
# ============================================
@bp.route('/resultat', methods=['POST'])
def registrera_resultat():
    data = request.get_json()
    path = os.path.join('data', 'resultat.json')

    # Fail-safe: kontrollera att alla fält finns
    obligatoriska_falt = ['personnummer', 'kurskod', 'modul', 'datum', 'betyg']
    for f in obligatoriska_falt:
        if f not in data or not data[f]:
            return jsonify({"status": f"fel – saknar fält: {f}"}), 400

    resultat = las_fil(path)
    resultat.append(data)
    skriv_fil(path, resultat)

    return jsonify({"status": "registrerad"}), 201


# ============================================
# GET /ladok/resultat – visar alla resultat
# ============================================
@bp.route('/resultat', methods=['GET'])
def visa_resultat():
    path = os.path.join('data', 'resultat.json')
    resultat = las_fil(path)
    return jsonify(resultat), 200


# ============================================
# DELETE /ladok/resultat/rensa – rensar all data
# ============================================
@bp.route('/resultat/rensa', methods=['DELETE'])
def rensa_resultat():
    path = os.path.join('data', 'resultat.json')
    skriv_fil(path, [])
    return jsonify({"status": "alla resultat raderade"}), 200
