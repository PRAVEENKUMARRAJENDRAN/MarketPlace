from flask import Flask,render_template

#__name__ is a built in function that references to the python file
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/about/<username>')
def about(username):
    return f'<h1>{username} king</h1>'  

@app.route('/market')
def market_page():
    item_list = [
        { 'id':1,'name':'Phone','barcode':'||2349068','price':'500'},
        { 'id':2,'name':'Laptop','barcode':'||2349456','price':'500'},
    ]
    return render_template('market.html',items = item_list)