from flask import Flask, render_template

app = Flask('blogktubre')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html', page_title=u"Contact")
