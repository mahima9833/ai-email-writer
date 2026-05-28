from dotenv import load_dotenv
import os

from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from groq import Groq

# Load env FIRST
load_dotenv()

# NOW you can use os safely
print("KEY =", os.getenv("GROQ_API_KEY"))

# Create FastAPI app
app = FastAPI()

# Initialize Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# HTML UI
HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Email Writer</title>
    <style>
        body {
            font-family: Arial;
            margin: 40px;
        }

        textarea {
            width: 500px;
        }

        pre {
            background: #f4f4f4;
            padding: 20px;
            white-space: pre-wrap;
        }
    </style>
</head>
<body>

    <h1>AI Email Writer</h1>

    <form method="post">

        <textarea
            name="topic"
            rows="6"
            placeholder="Enter email topic"
        ></textarea>

        <br><br>

        <select name="tone">
            <option value="formal">Formal</option>
            <option value="friendly">Friendly</option>
            <option value="professional">Professional</option>
        </select>

        <br><br>

        <button type="submit">
            Generate Email
        </button>

    </form>

    <hr>

    <pre>{email}</pre>

</body>
</html>
"""

# Home page
@app.get("/", response_class=HTMLResponse)
async def home():
    #return HTML_PAGE.format(email=generate_email)
    return HTMLResponse(HTML_PAGE.replace("{email}", ""))

# Generate email
@app.post("/", response_class=HTMLResponse)
async def generate_email(
    topic: str = Form(...),
    tone: str = Form(...)
):

    prompt = f"""
    Write a {tone} email about:
    {topic}

    Make it professional and clear.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_tokens=500
    )

    email = response.choices[0].message.content

    return HTMLResponse(HTML_PAGE.replace("{email}", email))