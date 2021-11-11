## Testing change
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

import os
import click

#
# These commands can be executed from the command line using
#
# flask rki-db <COMMAD>
# flask rki-db initdb
# flask rki-db dropdb

def register(app,db):
    print("Registering custom CLI commands")

    @app.cli.group()
    def rki_db():
        """Manage Template commands."""
        pass

    @rki_db.command()
    def initdb():
        ''' Create the SQL database. '''
        db.create_all()
        print('The SQL database has been created', 'green')

    @rki_db.command()
    def dropdb():
        ''' Delete the SQL database. '''
        print('Are you sure you want to lose all your SQL data? if yes type: CONFIRM')
        answer = input()
        if (answer == "CONFIRM"):
            db.drop_all()
            print('The SQL database has been deleted')
        else:
            print('Database deletion aborted...')
