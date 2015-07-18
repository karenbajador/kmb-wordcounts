from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

import os
os.environ['APP_SETTINGS'] = 'config.DevelopmentConfig'
os.environ['DATABASE_URL'] = 'postgresql://localhost/wordcount_dev'

print('os.environ[''APP_SETTINGS'']: %s' % os.environ['APP_SETTINGS'])
print('os.environ[''DATABASE_URL'']: %s' % os.environ['DATABASE_URL'])


from app import app, db
app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()