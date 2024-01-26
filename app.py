from flask import Flask, render_template
from project import unique_requirements
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('form.html', skills = unique_requirements)

@app.route('/form', methods = ['GET', 'POST'])
def form():
    return render_template('form.html')

@app.route('/response')
def response():
    render_template('response.html')

if(__name__ == '__main__'):
    app.run(debug=True)