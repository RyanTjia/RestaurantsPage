# Flask Project Template
A Flask boilerplate code to kickstart project for class and for individual project assessment.

*Author:* [Dr. Christoforos Christoforou](https://www.researchgate.net/profile/Christoforos-Christoforou-4)

## Application structure.
- The main logic of the application is implemented in the `app` module (folder).
- All static content (currently only a custom css file) is stored under the `static` folder.
- The `templates` file stores the html templates for the application layout and specific views. It is suggested that views for each blueprint are organized in their own subfolder within the `templates` folder. The project starting code includes a bootstrap layout.
- The `models.py` script contains the SQLAlchemy code. The starting code onlcudes only one model for the sample application.
- Forms and routes are organized within each blueprint's folder. The starting application includes the `main` blueprint and its corresponding forms and routes specified in  `app/main/forms.py` and `app/main/routes.py` respectively.
- `config.py` includes all the parameter configuration for the application.
- `manage.py` include management commands for creating and dropping the database.

The starting application file is `app.py`

## Setup

### Managing the Virtual environment.
- The application uses the `pipenv` virtual environment. Make sure you have the pipenv installed on your machine. You can check out to install the package at (https://pypi.org/project/pipenv/).

- Before running the sample application you need to activate the virtual environment py issuing the command in the terminal
```shell
  pipenv shell
```
- To install all the package listed in the Pipfile, type
```shell
  pipenv install
```
- To install any additional package you might need for your application you can type
```  
  pipenv install package-name

```
for example, the command, `pipnv install flask_sqlalchemy` install the flask_sqlalchemy package in the virtual environment.


### Managing the database.
For this project, the database management is handled in the `manage.py` file. This script allows you to initialize the database and drop the database. To create a new database run the command
```
  python manage.py initdb
```
initdb will create a database that includes tables for all the models (defined in your `models.py` file). Every time you modify your `models.py` file, you would need to re-create the database to reflect the new schema. Creating a database will create a file called `app.db` in your root folder.  Notice that you need to run these


### Managing the database - updated

When using Flask 2.0 and above, the database management is handled via flask.cli module. To initialize the database and drop the database. To create a new database run the command
```
  flask rki-db initdb
```

### Managing the applications.
- Before running the applications you need to make sure you activated the virtual environment (i.e. by executing `pipenv shell`) and created the database (i.e. by running `python manage.py initdb`).

- Once the virtual enviroment is active, and the database is created, you can run the application either by typing `flask  run` or `python manage.py runserver`.

- Notice: You might also need to set up the FLASK_APP environment variable to point to your application. For example, by typing `export FLASK_APP=app.py` on mac or `set FLASK_APP=app.py` in windows, while you are in the virtual environemnt.


## Libraries Used
- Packages installed in virtual environment include.
  - pipenv install `flask_sqlalchemy`
  - pipenv install `Flask-Bootstrap4`
  - pipenv install `Flask-WTF`
  - pipenv install `Flask-Script`

## License
This code is provided as a starting project code for the CUS1166 course only.  

Copyright ?? 2021 Christoforos Christoforou.
<div style="font-size:10px">
  <p>Copyright Statement: This problem set is part the of Dr. Christoforos Christoforou's instruction materials. You may not, nor may you knowingly allow others to reproduce or distribute lecture notes, course materials or any of their derivatives without the instructor's express written consent. The materials provided by the instructor of this course, including this problem set, are for the use of the students enrolled in the course for the sole purpose of personal use and study, and should not be used in any other way. Materials are presented in an educational context for personal use and study and should not be shared, distributed, disseminated or sold in print ??? or digitally ??? outside the course without permission.</p>
</div>
