from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello_world(name=None):
    url_for('static', filename='assets/css/style.css')
    return render_template('index_test.html', guestname=name)

@app.route('/blog')
def blog():
    return 'This is my first Blog!'