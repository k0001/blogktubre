from flask import Flask

app = Flask('blogktubre')


@app.route('/')
def index():
    return u"Hello"
