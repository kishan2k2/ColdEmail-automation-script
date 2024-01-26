projects = [
    {
        "name": "HyperParameter Tuning of Genetic Algorithm",
        "link": "https://drive.google.com/file/d/1Az2eOHyyDzIxtIFbNO93JbRG7oGpxThO/view?usp=sharing, ProjectLink: https://github.com/kishan2k2/HyperParameter-Tuning-of-genetic-algorithm",
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
# Extracting unique requirements
unique_requirements = set()
for project in projects:
    unique_requirements.update(project.get("requirements", []))

# Displaying the unique requirements
# print("Unique Requirements:")
# for requirement in unique_requirements:
# 