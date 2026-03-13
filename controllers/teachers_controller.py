from flask import Blueprint, jsonify, request, Response
import services.teachers_service as teachers_service

teachers_controller = Blueprint('teachers', __name__, url_prefix='/teachers')

@teachers_controller.route('', methods=['GET'])
def find_all() -> tuple[Response, int]:
    name: str = request.args.get('name', '', type=str)
    limit: int = request.args.get('limit', 10, type=int)
    page: int = request.args.get('page', 1, type=int)
    resultat = [teacher for teacher in teachers_service.teachers]
    if name:
        resultat = [teacher for teacher in resultat if teacher['name']==name]
    resultat = resultat[(page-1)*limit:((page-1)*limit)+limit]
    return jsonify(resultat), 200

@teachers_controller.route('', methods=['POST'])
def add_teacher() -> tuple[Response, int]:
    data = request.get_json()
    teachers_service.teachers.append({'id':len(teachers_service.teachers), 'name':data['name'], 'colleagues':data['colleagues']})
    return jsonify(data), 201