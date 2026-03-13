from flask import Flask
from controllers.teachers_controller import teachers_controller

app = Flask(__name__)
app.register_blueprint(teachers_controller)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
