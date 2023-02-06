from flask import Flask,render_template

#__name__ is a built in function that references to the python file
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def hello_world():
    return render_template('home.html')

@app.route('/about/<username>')
def about(username):
    return f'<h1>{username} king</h1>'  