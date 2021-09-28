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


from flask import Flask, current_app

from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

## from flask_migrate  import Migrate
## from flask_login import LoginManager

# Instanciate modules used in the project.

db = SQLAlchemy()

## migrate = Migrate()
## login = LoginManager()


def create_app(config_class=Config):

    app = Flask(__name__)

    # load configuration parameters from Config class
    app.config.from_object(config_class)

    # Initialize app for db and migrate modules.
    db.init_app(app)

    bootstrap = Bootstrap(app)
    ##migrate.init_app(app,db)
    ##login.init_app(app)


    # Added the autho blueprint
    ##from app.auth import bp as auth_routes_bp
    ##app.register_blueprint(auth_routes_bp,url_prefix='/auth')


    # Added the main app.

    from app.main import bp as main_routes_bp
    app.register_blueprint(main_routes_bp)

    return app;
