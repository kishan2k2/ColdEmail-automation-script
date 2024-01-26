from flask import Flask, render_template, request
from proj import unique_requirements
from script import generate_cold_email
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/form', methods = ['GET', 'POST'])
def form():
    if request.method == 'POST':
        company_name = request.form.get('company_name')
        company_domain = request.form.get('company_domain')
        person_name = request.form.get('person_name')
        projects = request.form.get('projects')  # Assuming projects is a textarea or similar
        skills_requirements = request.form.getlist('skills_requirements')
        # print(skills_requirements)
        email = request.form.get('email')
        email_content = generate_cold_email(company_name, company_domain, person_name, projects, skills_requirements, email)
        # flash('Email sent successfully!', 'success')
        return render_template('response.html', message=email_content)
    return render_template('form.html', skills = unique_requirements)


@app.route('/response')
def response():
    render_template('response.html')

if(__name__ == '__main__'):
    app.run(debug=True)