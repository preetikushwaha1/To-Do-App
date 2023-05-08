from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"   #initialize sql_alchemy
db = SQLAlchemy(app) 




class My_Todo(db.Model):
    sno = db.Column(db.Integer, primary_key =True)
    title = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(500), nullable = False)
    date_created = db.Column(db.DateTime,  default = datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

with app.app_context():        #add this to create table in instance folder
    db.create_all() 
     

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == "POST":
        title=request.form['title']
        desc = request.form['desc']
        print("titel=", title)
        print("desc=", desc)
        
        todo = My_Todo(title =title, desc = desc)
        db.session.add(todo)
        db.session.commit()
        allTodo = My_Todo.query.all()
        print(allTodo)
    return render_template('index.html', allTodo=allTodo)

@app.route("/show")
def products():
    allTodo = My_Todo.query.all()
    print(allTodo)
    
    return "this is productd page"

if __name__ =="__main__":
    app.run(debug=True) 