#this code is for small flask app
from flask import Flask, render_template
app = Flask(__name__)

#jobs
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/health')
def health():
    return 'Server is up and running'
