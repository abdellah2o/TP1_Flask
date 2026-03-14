from flask import Flask, render_template

from controllers.courses_controller import courses_controller
from controllers.gives_controller import gives_controller
from controllers.teachers_controller import teachers_controller
import services

app = Flask(__name__)
app.register_blueprint(teachers_controller)
app.register_blueprint(courses_controller)
app.register_blueprint(gives_controller)


@app.route('/')
def index():  # put application's code here
    data = [{'Hello': 'World'}]

    return render_template("index.html", data=data)

@app.route('/teachers')
def teachers():
    data = services.teachers_service.teachers

    return render_template("teachers.html", data=data, jsfile="teachers.js")

@app.route('/courses')
def courses():
    data = services.courses_service.courses

    return render_template("index.html", data=data)

@app.route('/gives')
def gives():
    data = services.gives_service.gives

    return render_template("index.html", data=data)


if __name__ == '__main__':
    app.run()
