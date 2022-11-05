from application.databse import db 

class Student(db.Model):
  __tablename__ = 'student_table'
  student_id = db.Column(db.Integer(), autoincrement=True,primary_key=True)
  roll_number = db.Column(db.String(), unique=True, nullable=False)
  first_name = db.Column(db.String(), unique=True, nullable=False)
  last_name = db.Column(db.String())
  class_name = db.Column(db.String(), unique=True, nullable=False)
  stay_type = db.Column(db.String(), unique=True, nullable=False)
  email_id = db.Column(db.String(), unique=True, nullable=False)
  login_id = db.Column(db.String(), unique=True, nullable=False)
  password = db.Column(db.String(), unique=True, nullable=False)
  photo = db.Column(db.Blob(), nullable=False)

class Instructor(db.Model):
  __tablename__ = 'instructor_table'
  class_name = db.Column(db.String(), primary_key=True)
  instructor_1_name = db.Column(db.String(), unique=True, nullable=False)
  instructor_1_mail = db.Column(db.String(), unique=True, nullable=False)
  instructor_2_name = db.Column(db.String(), unique=True, nullable=False)
  instructor_3_name = db.Column(db.String())
  instructor_3_mail = db.Column(db.String())
  dept_name = db.Column(db.String(), unique=True, nullable=False)