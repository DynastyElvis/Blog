from app import create_app, db
from flask_script import Manager, Server



app = create_app()
manager = Manager(app)
manager.add_command('server',Server)


@manager.shell
def make_shell_context():
    return dict(db=db)

if __name__ == '__main__':
    manager.run()