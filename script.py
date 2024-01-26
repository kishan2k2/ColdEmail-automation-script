# Projects with requirements
projects = [
    {
        "name": "HyperParameter Tuning of Genetic Algorithm",
        "link": "https://drive.google.com/file/d/1Az2eOHyyDzIxtIFbNO93JbRG7oGpxThO/view?usp=sharing, https://github.com/kishan2k2/HyperParameter-Tuning-of-genetic-algorithm",
        "description": "Tuned hyperparameters namely survival threshold, Elitism, activation function, fitness criterion, population size. Using Flappy Bird game as a testbed.",
        "roles_responsibilities": "My main role was to code the program, did the data analysis for the interpretation of results. Contributed in writing of research paper. Represented our project in front of the panel.",
        "skills_used": "Pythonic development, game development, Data Science, Statistics, Intensive research.",
        "result": "Shortlisted in Elsevier publication, Scopus and Crossref during ICDAM and HINWEIS conference.",
        "requirements": ["research", "game-development", "data-science", "python", "algorithm", "hyperparameter-tuning"]
    },
    {
        "name": "Face Recognition Attendance Software",
        "link": "https://github.com/kishan2k2/FaceRecognicing-Attendance-System",
        "description": "Developed an attendance software which recognizes faces in real-time using a web interface and maintains the database of students' profiles and attendance.",
        "roles_responsibilities": "Conducted research to find the most optimal way for face detection and recognition. Coded the entire program.",
        "skills_used": "Python, Flask framework, ScikitLearn KnearestNeighbour, Web Development HTML CSS.",
        "result": "Created a beautiful and clean UI website capable of detecting, recognizing and maintaining the database of students and daily attendance.",
        "requirements": ["python", "web-development", "open-cv", "flask", "algorithm"]
    },
    {
        "name": "Free Movies",
        "link": "https://kishan2k2.github.io/MovieDhundo/",
        "description": "Developed a React-based free movie website using OMDB and VidSrc API. Created a seamless and visually appealing app for watching movies.",
        "roles_responsibilities": "Full-stack web development, React for UI, GitHub for version control and hosting, Integration of OMDB and VidSrc API, Postman testing for API reliability.",
        "skills_used": "React, API integration, testing, full-stack development.",
        "result": "Successfully built a beautiful and functional movie website, providing users with an enjoyable movie-watching experience.",
        "requirements": ["react", "api", "web-development", "api-testing"]
    },
    {
        "name": "Movie Recommendation System",
        "link": "https://github.com/kishan2k2/MovieRecomendationSystem",
        "description": "Developed a movie recommendation system utilizing the TMDB dataset. Employed various preprocessing tools to clean and prepare the data. Created vector embedding for each movie using a bag of words. For recommendation, I used cosine similarity on the vectors.",
        "roles_responsibilities": "Data preprocessing and cleaning, Research on creating vector embedding, Research on the best metric to find similar vectors.",
        "skills_used": "Data preprocessing, Research.",
        "result": "Created a movie recommendation system with astonishing accuracy.",
        "requirements": ["data-preprocessing", "research", "recomendation-system", "api", "vector-database"]
    },
    {
        "name": "Emotion Reconition-NLP mega project",
        "link": "https://github.com/kishan2k2/Emotion_prediction",
        "description": "Developed an Emotion Recognition Model employing both Traditional ML algorithms and Neural Network architectures. The project includes the use of Naïve Bayes, Random Forest, Logistic Regression, SVM, CNN, RNN, LSTM, biLSTM, and Transfer Learning with pre-trained models like BERT, RoBERTa, and DistilBERT.",
        "roles_responsibilities": "Dataset preparation and preprocess, Research about all the different ways to do text classification. Tuning the models. Implementing the algorithms. Hosting the website.",
        "skills_used": "Data preprocessing, Research, algorithms, DeepLerning, LLM, hosting, gradio",
        "result": "Created a movie recommendation system with astonishing accuracy.",
        "requirements": ["data-preprocessing", "research", "algorithm", "deep-learning", "LLM"]
    }
]


def generate_cold_email(company_name, company_domain, person_name, projects, skills_requirements=None):
    # Greeting
    email_content = f"Dear {person_name},\n\n"

    # Opening statement
    email_content += f"I hope this email finds you well. My name is Kishan, and I recently came across {company_name}."

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

    return email_content

# Example usage:
company_name = "Your company"
company_domain = "Your companys' Domain"
person_name = "You"
skills_requirements = ["react", "research", "game development"]

cold_email = generate_cold_email(company_name, company_domain, person_name, projects, skills_requirements)
print(cold_email)

