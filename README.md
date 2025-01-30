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
- **Frontend**: [Next.js](https://nextjs.org/), [Shadcn](https://shadcn.dev/)
- **Backend**: [Flask](https://flask.palletsprojects.com/), [Flask-RESTx](https://flask-restx.readthedocs.io/)
- **Database**: SQLite3
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
   - Backend (Flask):
     ```bash
     cd backend
     pip install -r requirements.txt
     ```
   - Frontend (Next.js):
     ```bash
     cd frontend
     npm install
     ```

3. **Set up the Database**:
   - Create the necessary tables for students, courses, files, queries, and concepts in SQLite3.
   - Run database migrations if applicable.

4. **Configure Environment Variables**:
   - Add credentials for AI API access, Google Cloud Storage, and any other required configurations in `.env` files for the backend and frontend.

5. **Run the Application**:
   - Start the backend server:
     ```bash
     cd backend
     flask run
     ```
   - Start the frontend server:
     ```bash
     cd frontend
     npm run dev
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
├── backend/             # Flask backend for handling API requests
│   ├── app/
│   ├── models/          # Database models (students, courses, files, etc.)
│   ├── routes/          # Flask routes (e.g., concept generation, file upload)
│   └── main.py          # Entry point for the backend server
├── frontend/            # Next.js frontend for user interface
│   ├── pages/
│   ├── components/
│   └── utils/
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
