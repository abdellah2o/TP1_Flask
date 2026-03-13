from flask import Blueprint, jsonify, request, Response
from services import gives_service, teachers_service

gives_controller = Blueprint('gives', __name__, url_prefix='/gives')

@gives_controller.route('', methods=['GET'])
def find_all() -> tuple[Response, int]:
    teacher: int = request.args.get('teacher', -1, type=int)
    course: int = request.args.get('course', -1, type=int)
    limit: int = request.args.get('limit', 10, type=int)
    page: int = request.args.get('page', 1, type=int)
    resultat = [give for give in gives_service.gives]
    if teacher >= 0 and course >= 0:
        resultat = [give for give in resultat if (give['teacher_id'] == teacher and give['course_id'] == course)]
    else:
        if teacher >= 0:
            resultat = [give for give in resultat if give['teacher_id'] == teacher]
        if course >= 0:
            resultat = [give for give in resultat if give['course_id'] == course]
    resultat = resultat[(page - 1) * limit:((page - 1) * limit) + limit]
    return jsonify(resultat), 200


@gives_controller.route('', methods=['POST'])
def add_gives() -> tuple[Response, int]:
    data = request.get_json()

    gives_service.gives.append({
        'teacher_id': data['teacher_id'],
        'course_id': data['course_id'],
        'date': data['date'],
        'duration': data['duration']
    })

    return jsonify(gives_service.gives), 201

@gives_controller.route('/<int:teacher_id>/<int:course_id>/<string:date>', methods=['DELETE'])
def delete_gives(teacher_id: int, course_id: int, date: str) -> tuple[Response, int]:
    for i, give in enumerate(gives_service.gives):
        if give['teacher_id'] == teacher_id and give['course_id'] == course_id and give['date'] == date:
            gives_service.gives.pop(i)

    return jsonify(gives_service.gives), 200

@gives_controller.route('/<int:teacher_id>/<int:course_id>/<string:date>', methods=['PUT'])
def update_gives(teacher_id: int, course_id: int, date: str) -> tuple[Response, int]:
    data = request.get_json()

    for i, give in enumerate(gives_service.gives):
        if give['teacher_id'] == teacher_id and give['course_id'] == course_id and give['date'] == date:
            gives_service.gives[i] = {
                'teacher_id': data['teacher_id'],
                'course_id': data['course_id'],
                'date': data['date'],
                'duration': data['duration']
            }

    return jsonify(gives_service.gives), 200

@gives_controller.route('/<string:year>', methods=['GET'])
def access_by_year(year: str) -> tuple[Response, int]:
    gives_selected = [give for give in gives_service.gives if give['date'][:4] == year]

    return jsonify(gives_selected), 200

@gives_controller.route('/<int:course_id>/<string:date>/teacher', methods=['GET'])
def find_by_course(course_id: int, date: str) -> tuple[Response, int]:
    teacher = {}

    for give in gives_service.gives:
        if give['course_id'] == course_id and give['date'] == date:
            for i in range(len(teachers_service.teachers)):
                if teachers_service.teachers[i]['id'] == give['teacher_id']:
                    teacher = teachers_service.teachers[i]

    return jsonify(teacher), 200