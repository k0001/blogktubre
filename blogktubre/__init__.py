from flask import Flask, render_template

app = Flask('blogktubre')


@app.route('/')
def index():
    return render_template('index.html')
