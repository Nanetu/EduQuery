# EduQuery

EduQuery is an AI-powered personalized learning assistant designed to support university students in their academic journey. The platform provides targeted study suggestions, concept explanations, question-answering capabilities, and quiz generation. EduQuery aims to ease students' transition into university academics, enhance study support, and help students better prepare for exams through institution-specific knowledge.

## Table of Contents
- [Features](#features)
- [Project Goals](#project-goals)
- [Tech Stack](#tech-stack)
- [Setup](#setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## Features
- **Personalized Study Guide**: Recommends study materials and concepts based on user queries and course content.
- **Institution-Specific Knowledge**: Leverages unique academic resources and data tailored to support students at specific institutions.
- **AI-Powered Concept Generation**: Uses a fine-tuned language model to generate explanations, summaries, and answers for student queries.
- **File Upload and Management**: Allows students to upload and manage course PDFs, enabling the app to pull relevant information.
- **Quiz Generation**: Automatically creates quizzes and practice questions based on study content, helping students test their knowledge.
- **Continuous Learning and Feedback**: Adapts to students' learning progress and offers tailored suggestions across different academic years.

## Project Goals
EduQuery aims to:
1. Provide university students with an intuitive, AI-driven study tool to improve their academic experience.
2. Address common challenges students face, such as finding relevant study materials, understanding difficult concepts, and preparing for exams.
3. Demonstrate to investors the feasibility and scalability of EduQuery as a valuable educational tool.

## Tech Stack
- **Frontend**: [React.js](https://react.dev/), [Shadcn](https://shadcn.dev/)
- **Backend**: [Django](https://www.djangoproject.com/), [Django REST Framework (DRF)](https://www.django-rest-framework.org/)
- **Database**: SQLite3 (for development), PostgreSQL (recommended for production)
- **AI API**: Fine-tuned GPT model for generating responses and concept explanations
- **Cloud Storage**: Google Cloud Storage or Google Drive (for temporary PDF storage during demo)

## Setup
To get started with EduQuery locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Nanetu/EduQuery.git
   cd EduQuery
   ```

2. **Install dependencies**:
   - Backend (Django):
     ```bash
     cd backend
     python -m venv venv
     source venv/bin/activate  # For Windows: venv\Scripts\activate
     pip install -r requirements.txt
     ```
   - Frontend (React.js):
     ```bash
     cd frontend
     npm install
     ```

3. **Set up the Database**:
   - Apply migrations to set up the database schema:
     ```bash
     cd backend
     python manage.py migrate
     ```

4. **Configure Environment Variables**:
   - Backend: Add API keys and database settings to a `.env` file in the `backend` folder.
   - Frontend: Add environment variables (e.g., API endpoints) to a `.env` file in the `frontend` folder.

5. **Run the Application**:
   - Start the Django backend server:
     ```bash
     cd backend
     python manage.py runserver
     ```
   - Start the React frontend server:
     ```bash
     cd frontend
     npm start
     ```

6. **Access the Application**:
   - Open [http://localhost:3000](http://localhost:3000) in your browser to view the application.

## Usage
EduQuery is designed for students to:
1. **Upload PDFs**: Upload course files for AI-based content analysis.
2. **Ask Questions**: Type queries into the study guide page to receive personalized study material.
3. **View Suggested Concepts**: Receive concept explanations and study tips based on uploaded files and queried content.
4. **Take Quizzes**: Generate quizzes on specific topics to reinforce learning.

## Project Structure
```
EduQuery/
├── backend/             # Django backend for handling API requests
│   ├── core/            # Core application settings
│   ├── apps/            # Custom Django apps (students, courses, files, etc.)
│   ├── static/          # Static files
│   ├── templates/       # HTML templates (if any)
│   └── manage.py        # Entry point for the Django backend
├── frontend/            # React.js frontend for user interface
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/    # API service integration
│   │   └── utils/
│   └── package.json     # Frontend dependencies
├── .env                 # Environment variables (not committed)
└── README.md            # Project README
```

## Contributing
We welcome contributions from the community! To contribute:
1. Fork the repository and create a new branch for your feature or bug fix.
2. Make changes and ensure code quality.
3. Submit a pull request detailing your changes.

Please follow our coding guidelines and ensure that all tests pass before submitting your PR.

## Acknowledgments
Special thanks to UbuntuNet Alliance for the sponsorship and opportunity to develop EduQuery as part of the girls' initiative. 
