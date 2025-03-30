Project Name: Blog System
A full-stack blog system built using Django (backend) and React.js (frontend), with API integration
Features
✔️ List blogs with relevant details
✔️ View detailed information about a selected blog post
✔️ User authentication (if implemented)
✔️ Search and filter functionality (if implemented)
✔️ Likes and comments feature (if implemented)

🛠️ Tech Stack
Backend: Django, Django REST Framework

Frontend: React.js

Database: SQLite / PostgreSQL

Styling: CSS / Tailwind



🚀 Setup Instructions
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/Ishiptaa/Project-Blog-System.git
cd Project-Blog-System
2️⃣ Backend Setup (Django)
Install dependencies
bash
Copy
Edit
cd backend
python -m venv venv
source venv/bin/activate   # For Mac/Linux
venv\Scripts\activate      # For Windows
pip install -r requirements.txt
Apply Migrations
bash
Copy
Edit
python manage.py migrate
Run the Django Server
bash
Copy
Edit
python manage.py runserver
3️⃣ Frontend Setup (React.js)
Install dependencies
bash
Copy
Edit
cd frontend
npm install
Start the React Development Server
bash
Copy
Edit
npm start
