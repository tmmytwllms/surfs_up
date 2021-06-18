#Import flask
from flask import Flask

#Create flask instance
app=Flask(__name__)

#Create the root
@app.route('/')
def hello_world():
    return 'Hello World'
    return 'Try /test'

@app.route('/test')
def hello_again():
    return "Hello again"