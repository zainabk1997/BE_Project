from flask import Flask
from flaskext.mysql import MySQL
from flask import Flask,request, render_template



mysql = MySQL()
app= Flask(__name__)
app.secret_key = 'key'

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'safety'
app.config['MYSQL_DATABASE_DB'] = 'plantdb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
 


@app.route("/")
@app.route("/welcome")
def hello():
    return render_template('welcome.html')


@app.route("/add")
def add():
    cursor= mysql.connect().cursor()
    cursor.execute('SELECT wateradded FROM plantdb1 ORDER BY plant_id DESC LIMIT 1')
    data = cursor.fetchone()
    datax= ''.join((data))
    datax2= int(datax)
    return render_template('add.html', water=datax2)

@app.route("/level")
def level():
    cursor= mysql.connect().cursor()
    cursor.execute('SELECT waterlevel FROM plantdb1 ORDER BY plant_id DESC LIMIT 1')
    data1 = cursor.fetchone()
    data11= ''.join((data1))
    data2= int(data11)
    # if data2<50:
    #     flash(u'Waterlevel too low, refill container!', 'Warning') 
    #     return redirect(url_for('hello'))
    # else:
    return render_template('level.html', waterlevel=data2)

if __name__ == "__main__":
    app.run(debug=True)