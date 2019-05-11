from flask import *



@app.route('/')
def index():
    return render_template('index.html')