from flask import Blueprint, jsonify, request, Response
import services.gives_service as gives_service

gives_controller = Blueprint('gives', __name__, url_prefix='/gives')