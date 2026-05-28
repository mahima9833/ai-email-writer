Project NAme - AI Email Writer (Groq + FastAPI)

An AI-powered email generator web app built using Python, FastAPI, and Groq LLM (Llama 3).
It generates professional emails instantly based on user input and tone selection.

🚀 Live Features
1 Generate professional emails from simple prompts
2 Select tone: Formal / Friendly / Professional
3 Fast responses using Groq LLM API
4 Simple web UI (HTML + FastAPI backend) and Powered by Llama 3 model
🛠️ Tech Stack
Python.
FastAPI,
Groq API, HTML/CSS 🌐
dotenv
📁 Project Structure
ai-email-writer/
│
├── main.py
├── .env
├── requirements.txt
├── .gitignore
└── venv/ (ignored)
⚙️ Installation & Setup
cd ai-email-writer
2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install dependencies
pip install fastapi uvicorn groq python-dotenv python-multipart
4️⃣ Add API key

Create .env file:

GROQ_API_KEY=your_api_key_here

Get API key from:
Groq Console

5️⃣ Run the project
python -m uvicorn main:app --reload

Open in browser:

http://127.0.0.1:8000
🧠 How it works
User enters email topic + tone
FastAPI sends request to Groq API
Llama 3 model generates email
Response is shown in browser
