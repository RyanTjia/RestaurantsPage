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


# Get access to the os .
import os

# Get the absolute path of the current file.
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    # flask-SQLAlchemy extension takes the location of the
    # application's database from the SQLALCHEMY_DATABASE_URI configuration variable.

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir,'app.db')

    # Disable Track notifications feature from Flask-SQLAlchemy

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a-secret-key-for-cus1166'
