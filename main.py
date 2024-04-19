from flask import Flask, render_template, request, redirect, url_for
import sys
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from models import Base
from models import Category, Task


engine = create_engine("mysql+mysqldb://pld_test:pld_test_pwd@localhost/pld_test_db", pool_pre_ping=True)
Session = sessionmaker(bind=engine)
session = Session()

app = Flask('__name__')
@app.route('/', strict_slashes=False, methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        name = request.form["name"]
        desciription = request.form["desciription"]
        date = request.form["deadline"]
        category_id = request.form["category"]
        task = Task(name=name, desc=desciription, deadline=date, category_id=category_id)
        session.add(task)
        session.commit()
        return redirect(url_for('index'))
    else:
        tasks = session.query(Task).order_by(Task.id)
        category = session.query(Category).order_by(Category.id)
        return render_template("index.html", tasks=tasks, category=category)
    
@app.route('/delete/<id>', strict_slashes=False)
def delete(id):
    session.query(Task).where(Task.id == id).delete()
    session.commit()
    return redirect(url_for('index'))


    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)