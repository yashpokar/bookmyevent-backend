from event import create_app
from event import config
from flask_migrate import MigrateCommand
from flask_script import Manager, Server

app = create_app(config.DevelopmentConfig)
manager = Manager(app)

manager.add_command("runserver", Server(host=app.config['HOST'], port=app.config['PORT']))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()
