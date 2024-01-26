import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import configparser
from proj import projects
config = configparser.ConfigParser()
config.read('config.ini')

def send_email(subject, body, to_email, sender_email, sender_password):
    # Set up MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))
    # Connect to the SMTP server using SSL on port 465
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        # Login with your sender email and password (use application-specific password if required)
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, to_email, message.as_string())


def generate_cold_email(company_name, company_domain, person_name, project=projects, skills_requirements=None, email=None):
    # Greeting
    email_content = f"Dear {person_name},\n\n"

    # Opening statement
    email_content += f"I hope this email finds you well. My name is Kishan, and I recently came across internship oppurtunity at {company_name}."

    # Personal Information
    email_content += "\n\nThis is a brief summary about me. I am currently in my sixth semester at MAIT IPU, specializing in Python development with a focus on TensorFlow, Flask, NLP, NumPy, and Pandas."
    

    # Additional Information
    email_content += "\n\nI also have a strong command over Data Structures and Algorithms, having solved 300+ questions on LeetCode and achieved 2 stars on CodeChef."
    
    # Resume
    email_content += "\n\nThis is my resume https://drive.google.com/file/d/1D_NAq7gTkcIxDnyuCjQB-v4rfXZltY-l/view?usp=sharing"

    # Contact Information
    email_content += "\n\nYou can reach me at:\nPhone: +91 8448876965\nEmail: payadikishan@gmail.com"

    # Portfolio Link
    email_content += "\n\nTo view me in a more sophisticated way, please visit my portfolio: [Kishan's Portfolio](https://kishan2k2.github.io/Portfolio/)\n"

    # Filter projects based on skills_requirements
    matching_projects = []
    if skills_requirements:
        matching_projects = [project for project in projects if any(req in project["requirements"] for req in skills_requirements)]

    # Extract skills from matching projects
    matching_skills = [skill for project in matching_projects for skill in project["requirements"]]

    # Deduplicate skills
    unique_skills_requirements = set(matching_skills)
    # print(unique_skills_requirements)
    # Adding a line about matching skill requirements
    if matching_projects:
        email_content += f"\n\nThese projects match these [{', '.join(unique_skills_requirements)}] skills required for the job:"
        
    email_content += "But this is not all you can view more on my website and my resume "

    # Adding project details to the email content
    for project in matching_projects:
        email_content += f"\n\n{project['name']} [Link: {project['link']}]\n"
        email_content += f"● Description-: {project['description']}\n"
        email_content += f"● Roles and responsibilities-: {project['roles_responsibilities']}\n"
        email_content += f"● Skills used-: {project['skills_used']}\n"
        email_content += f"● Result-: {project['result']}\n"

    # Closing statement
    email_content += "\n\nI am excited about the prospect of contributing to the innovative work at your company. Thank you for considering my application."
    
    if email:
        subject = f"Regarding internship oppurtunity at {company_name}"
        sender_email = "payadikishan@gmail.com"
        # sender_password = os.environ.get("password")
        # print(sender_password)
        # sender_password = sender_password.strip('"')
        sender_password = config.get('Credentials', 'sender_password')
        # print(sender_email, sender_password)
        send_email(subject, email_content, email, sender_email, sender_password)

    return email_content


# Example usage:
company_name = "Your company"
company_domain = "Your companys' Domain"
person_name = "You"
skills_requirements = ["react", "research", "game development"]
email = "payadikishan@gmail.com"

cold_email = generate_cold_email(company_name, company_domain, person_name, projects, skills_requirements, email)
# print(cold_email)

