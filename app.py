from flask import Flask, render_template, url_for, request, redirect
from flask_mysqldb import MySQL
from datetime import datetime


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'utotest.database.windows.net'
app.config['MYSQL_USER'] = 'deviloid'
app.config['MYSQL_PASSWORD'] = 'Akki_sql123'
app.config['MYSQL_DB'] = 'utodb'
mysql = MySQL(app)

class Todo(mysql.Model):
    __tablename__ = 'Model'
    id = mysql.Column(mysql.Integer, primary_key=True)
    content1 = mysql.Column(mysql.String(200), nullable=False)
    date_created = mysql.Column(mysql.DateTime, default=datetime.utcnow)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=='POST':
        task_content = request.form['content']
        new_task = Todo(content = task_content)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your input.'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks = tasks)


if __name__ == '__main__':
    app.run()