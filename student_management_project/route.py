from flask import Flask,render_template,redirect,request
from student import Student
from flask_sqlalchemy import SQLAlchemy


app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mssql+pyodbc://localhost\\SQLEXPRESS/StudentRecord?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes'
app.config['SQLALCHEMY _TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)



## CLASS For mapping the data getting from user to 
 ##database
class Record (db.Model):
    __tablename__='RECORD'
    name=db.Column('NAME', db.String(50), nullable=False )
    age=db.Column('AGE', db.Float,nullable=False)
    cls=db.Column('CLASS',db.String,nullable=False)
    maths=db.Column ('MATHS_MARKS',db.Float,nullable=False)
    science=db.Column('SCIENCE_MARKS',db.Float,nullable=False)
    english=db.Column('ENGLISH_MARKS',db.Float,nullable=False)
    id=db.Column('ID',db.Integer, primary_key=True)
    

@app.route('/')
def welcome():
    return render_template('index.html')


## add new student

@app.route('/add')
def add():
    return render_template('index.html')

@app.route("/submit",methods=['POST'])
def submit():
    if request.method=="POST":
        name=request.form['name']
        age=float(request.form['age'])
        cls=request.form['student_class']
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        english=float(request.form['english'])

  
    

    obj = Student(name, age, cls, maths, science, english)
    print(obj.get_details())


    ##saving data to database

    new_record=Record(
        name=obj.get_name(),
        age=obj.get_age(),
        cls=obj.get_student_class(),
        maths=obj.get_maths(),
        science=obj.get_science(),
        english=obj.get_english())
    
    db.session.add(new_record)
    db.session.commit()
    return render_template('display.html')  

@app.route('/admin', methods=['GET'])
def admin():
    if request.method=='GET':
        students=Record.query.all()
        return render_template('admin.html',students=students)

@app.route('/update/<int:id>',methods=['POST'])
def update(id):
    students=Record.query.get(id)
    students.name=request.form['name']
    students.age=request.form['age']
    students.cls=request.form['student_class']
    students.maths=request.form['maths']
    students.science=request.form['science']
    students.english=request.form['english']

    ## saving the changes:
    db.session.commit()

    return redirect('/admin')


@app.route('/delete/<int:id>',methods=['POST'])
def delete(id):
    student=Record.query.get(id)
    db.session.delete(student)
    db.session.commit()
    return redirect('/admin')





if __name__=='__main__':
    app.run(debug=True)