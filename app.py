from flask import Flask, render_template

from controllers.courses_controller import courses_controller
from controllers.gives_controller import gives_controller
from controllers.teachers_controller import teachers_controller
from services import teachers_service

app = Flask(__name__)
app.register_blueprint(teachers_controller)
app.register_blueprint(courses_controller)
app.register_blueprint(gives_controller)


@app.route('/')
def index():  # put application's code here
    return render_template("index.html", teachers = teachers_service.teachers)


if __name__ == '__main__':
    app.run()
