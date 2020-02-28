from flask import Flask, render_template, url_for, request, redirect
from flask_mysqldb import MySQL
from datetime import datetime


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'utotest.database.windows.net'
app.config['MYSQL_USER'] = 'deviloid'
app.config['MYSQL_PASSWORD'] = 'Akki_sql123'
app.config['MYSQL_DB'] = 'utodb'
mysql = MySQL(app)

class Model(mysql.Model):
    id = mysql.Column(mysql.Integer, primary_key=True)
    content1 = mysql.Column(mysql.String(200), nullable=False)
    date_created = mysql.Column(mysql.DateTime, default=datetime.utcnow)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=='POST':
        task_content = request.form['content']
        cur = mysql.connection.cursor()
        new_task = cur.execute("INSERT INTO Model(content1) VALUES (%s)", (content1))
        try:
            mysql.connection.add(new_task)
            mysql.connection.commit()
            mysql.close()
            return redirect('/')
        except:
            return 'There was an issue adding your input.'

    else:
        tasks = cur.execute("SELECT * FROM Model ORDER BY date_created")
        return render_template('index.html', tasks = tasks)

# @app.route('/delete/<int:id>')
# def delete(id):
#     task_to_delete = Model.query.get_or_404(id)
#     try:
#         mysql.connection.delete(task_to_delete)
#         mysql.connection.commit()
#         return redirect('/')
#     except:
#         return 'There was a problem deleting that task.'

# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# def update(id):
#     task = Model.query.get_or_404(id)
#     if request.method == 'POST':
#         task.content = request.form['content']
#         try:
#             mysql.connection.commit()
#             return redirect('/')
#         except:
#             'There was an issue updating your task.'
#     else:
#         return render_template('update.html', task = task)


if __name__ == "__main__":
    app.run(debug=True)