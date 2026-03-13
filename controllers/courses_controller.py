from flask import Blueprint, jsonify, request, Response
import services.courses_service as courses_service

courses_controller = Blueprint('courses', __name__, url_prefix='/courses')

@courses_controller.route('', methods=['GET'])
def find_all() -> tuple[Response, int]:
    name: str = request.args.get('name', '', type=str)
    limit: int = request.args.get('limit', 10, type=int)
    page: int = request.args.get('page', 1, type=int)
    resultat = [course for course in courses_service.courses]
    if name:
        resultat = [course for course in resultat if course['name'] == name]
    resultat = resultat[(page - 1) * limit:((page - 1) * limit) + limit]
    return jsonify(resultat), 200

@courses_controller.route('', methods=['POST'])
def add_course() -> tuple[Response, int]:
    data = request.get_json()

    courses_service.courses.append({'id': courses_service.cgid, 'name': data['name']})
    courses_service.cgid += 1

    return jsonify(data), 201