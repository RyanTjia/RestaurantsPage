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


#from flask import url_for
from app import db




class Task(db.Model):

    task_id = db.Column(db.Integer, primary_key=True)
    task_desc = db.Column(db.String(128), index=True)
    task_status = db.Column(db.String(128))
