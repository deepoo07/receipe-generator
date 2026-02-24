# Recipe Generator Web App

A Flask-based web application that generates creative step-by-step recipes using the Groq API. Users can enter available ingredients and receive a named recipe with detailed cooking instructions.

---

## Features

- Accepts custom ingredient input
- Generates a recipe name
- Generates a funny version of the recipe name
- Provides step-by-step instructions
- Clean Bootstrap-based interface
- Deployable on Render (Free Tier)

---

## Tech Stack

- Python
- Flask
- Groq API
- Gunicorn
- Bootstrap (CDN)

---

## Project Structure

recipe-generator/
│
├── wepage.py
├── requirements.txt
├── Procfile
└── README.md

---

## Local Setup

1. Clone the repository

git clone https://github.com/deepoo07/recipe-generator.git
cd recipe-generator

2. Create virtual environment (recommended)

Windows:
python -m venv venv
venv\Scripts\activate

Mac/Linux:
python3 -m venv venv
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Set environment variable

Windows (PowerShell):
setx GROQ_API_KEY "your_api_key_here"

Mac/Linux:
export GROQ_API_KEY="your_api_key_here"

5. Run the application

python wepage.py

Open in browser:
http://127.0.0.1:5000

---

## Deployment (Render)

1. Push project to GitHub
2. Create New Web Service on Render
3. Select Free plan
4. Build Command:

pip install -r requirements.txt

5. Start Command:

gunicorn wepage:app

6. Add Environment Variable:

Key: GROQ_API_KEY  
Value: your_api_key_here

Deploy the service.

---

## Required Environment Variable

GROQ_API_KEY

---

## requirements.txt

flask
groq
gunicorn

---

## Notes

- Free Render instances may sleep after inactivity.
- First request after inactivity may take a few seconds.
- Never hardcode your API key in the source code.

---

## License

This project is created for portfolio purposes.
