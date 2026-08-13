Markdown
# 🏋️ Fitness Tracker App

A full-stack web application built with **Django** for tracking personal workouts, daily activity, and fitness goals. Pre-configured for seamless serverless deployment on **Vercel**.

---

## ✨ Features

* **Workout & Activity Tracking:** Log daily exercise routines, sets, reps, and activity metrics.
* **Django Backend Architecture:** Structured with a dedicated project configuration (`fitness_project`) and application app module (`tracker`).
* **Vercel-Ready Deployment:** Includes `vercel.json` configuration for running Django as a serverless function on Vercel.

---

## 🛠️ Tech Stack

* **Framework:** Python / Django
* **Deployment & Hosting:** Vercel (via WSGI/ASGI serverless entry point)
* **Dependencies:** Managed via `requirements.txt`

---

## 📂 Repository Structure

```text
.
├── fitness_project/   # Core Django project settings and root routing
├── tracker/           # Application app (models, views, templates, routes)
├── .gitignore         # Version control exclusion rules
├── manage.py          # Django administrative CLI utility
├── requirements.txt   # Python project dependencies
└── vercel.json        # Vercel deployment configuration file
🚀 Getting Started Locally
Prerequisites
Python 3.x installed on your system

pip (Python package manager)

Installation & Setup
Clone the repository:

Bash
git clone [https://github.com/benluts256/fitness_tracker.git](https://github.com/benluts256/fitness_tracker.git)
cd fitness_tracker
Create and activate a virtual environment:

Bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
Install dependencies:

Bash
pip install -r requirements.txt
Apply database migrations:

Bash
python manage.py migrate
Run the local development server:

Bash
python manage.py runserver
Open http://127.0.0.1:8000/ in your browser to view the application.

🌐 Deploying to Vercel
This repository is already configured with a vercel.json file. To deploy:

Install the Vercel CLI (npm i -g vercel) or link your GitHub repository directly in the Vercel Dashboard.

Run vercel from the root directory or push updates to the main branch for automatic build trigger.

🤝 Contributing
Contributions and enhancements are welcome! Feel free to open issues or submit pull requests.
