## Copyright , Dr. Christoforos Chrsitoforou.
## All rights reserved
##
## This code is part the of Dr. Christoforos Christoforou's instruction materials.
##
## You may not, nor may you knowingly allow others to reproduce or distribute lecture notes,
## course materials or any of their derivatives without the instructor's express written consent.

## The materials provided by the instructor of this course, including this problem set,
## are for the use of the students enrolled in the course for the sole purpose of personal use
## and study, and should not be used in any other way.
##
## Materials are presented in an educational context for personal use and study and should not be shared,
## distributed, disseminated or sold in print — or digitally — outside the course without permission.
##
## Use and moditication of this code is permitted for students enrolled in Dr. Christoforou's course
## for the purpose of the Course provided  the above copyright notice is retained in all source files.
##


#from flask.ext.script import Manager, prompt_bool, Shell, Server
from flask_script import Manager, prompt_bool, Shell, Server

from app import db, models, create_app

#from app import create_app

app = create_app()



manager = Manager(app)


def make_shell_context():
    return dict(app=app)


@manager.command
def initdb():
    ''' Create the SQL database. '''
    db.create_all()
    print('The SQL database has been created', 'green')


@manager.command
def dropdb():
    ''' Delete the SQL database. '''
    if prompt_bool('Are you sure you want to lose all your SQL data?'):
        db.drop_all()
        print('The SQL database has been deleted')


manager.add_command('runserver', Server())
manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
