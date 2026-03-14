from flask import Blueprint, jsonify, request, Response
import services.courses_service as courses_service

courses_controller = Blueprint('courses', __name__, url_prefix='/api/courses')

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

@courses_controller.route('/<int:course_id>', methods=['GET'])
def access_by_id(course_id: int) -> tuple[Response, int]:
    coursesSelected = [course for course in courses_service.courses if course['id'] == course_id]

    return jsonify(coursesSelected), 200

@courses_controller.route('/<int:course_id>', methods=['DELETE'])
def delete_course(course_id: int) -> tuple[Response, int]:
    i: int = 0
    while i != course_id and i <= courses_service.cgid:
        i += 1

    if i <= courses_service.cgid:
        courses_service.courses.pop(i)
    else:
        print("neuille")

    return jsonify(courses_service.courses), 200

@courses_controller.route('/<int:course_id>', methods=['PUT'])
def update_course(course_id: int) -> tuple[Response, int]:
    data = request.get_json()

    i: int = 0
    while i != course_id and i <= courses_service.cgid:
        i += 1

    if i <= courses_service.cgid:
        courses_service.courses[i] = {
            'id': courses_service.courses[i]['id'], 'name': data['name']
        }

    return jsonify(courses_service.courses), 200