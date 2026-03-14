from flask import Blueprint, jsonify, request, Response
import services.teachers_service as teachers_service

teachers_controller = Blueprint('teachers', __name__, url_prefix='/api/teachers')


@teachers_controller.route('', methods=['GET'])
def find_all() -> tuple[Response, int]:
    name: str = request.args.get('name', '', type=str)
    limit: int = request.args.get('limit', 10, type=int)
    page: int = request.args.get('page', 1, type=int)
    resultat = [teacher for teacher in teachers_service.teachers]
    if name:
        resultat = [teacher for teacher in resultat if teacher['name'] == name]
    resultat = resultat[(page - 1) * limit:((page - 1) * limit) + limit]
    return jsonify(resultat), 200


@teachers_controller.route('', methods=['POST'])
def add_teacher() -> tuple[Response, int]:
    data = request.get_json()

    teachers_service.teachers.append(
        {'id': teachers_service.tgid, 'name': data['name'], 'colleagues': data['colleagues']}
    )
    teachers_service.tgid += 1

    return jsonify(data), 201


@teachers_controller.route('/<string:teacher_name>', methods=['GET'])
def access_by_name(teacher_name: str) -> tuple[Response, int]:
    teachers_selected = [teacher for teacher in teachers_service.teachers if teacher['name'] == teacher_name]

    return jsonify(teachers_selected), 200


@teachers_controller.route('/<int:teacher_id>', methods=['GET'])
def access_by_id(teacher_id: int) -> tuple[Response, int]:
    teachers_selected = [teacher for teacher in teachers_service.teachers if teacher['id'] == teacher_id]

    return jsonify(teachers_selected), 200


@teachers_controller.route('/<int:teacher_id>/colleagues', methods=['GET'])
def find_colleagues(teacher_id: int) -> tuple[Response, int]:
    teachers_selected = [teacher for teacher in teachers_service.teachers if
                         teacher['id'] in teachers_service.teachers[teacher_id]['colleagues']]

    return jsonify(teachers_selected), 200


@teachers_controller.route('/<int:teacher_id>', methods=['DELETE'])
def delete_teacher(teacher_id: int) -> tuple[Response, int]:
    i: int = 0
    while i != teacher_id and i <= teachers_service.tgid:
        i += 1

    if i <= teachers_service.tgid:
        teachers_service.teachers.pop(i)
    else:
        print("neuille")

    return jsonify(teachers_service.teachers), 200


@teachers_controller.route('/<int:teacher_id>', methods=['PUT'])
def update_teacher(teacher_id: int) -> tuple[Response, int]:
    data = request.get_json()

    i: int = 0
    while i != teacher_id and i <= teachers_service.tgid:
        i += 1

    if i <= teachers_service.tgid:
        teachers_service.teachers[i]['name'] = data['name']
        teachers_service.teachers[i]['colleagues'] = data['colleagues']

    return jsonify(teachers_service.teachers), 200
