from flask import Flask, render_template
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
     

@app.route("/")
def hello_world():
    todo = My_Todo(title ="First todo", desc = "this is my first todo")
    db.session.add(todo)
    db.session.commit()
    return render_template('index.html')

@app.route("/products")
def products():
    return "this is products page"

if __name__ =="__main__":
    app.run(debug=True) 