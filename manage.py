from flask_script import Manager
from flask import Flask
from app import blueprint

app = Flask(__name__)
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

@manager.command
def run():
    app.run(debug=True)

if __name__ == '__main__':
    manager.run()