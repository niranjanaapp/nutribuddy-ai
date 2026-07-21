import os
from dotenv import load_dotenv

from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel
from groq import Groq

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(title="AI Recipe Generator")

# Templates folder
templates = Jinja2Templates(directory="templates")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Request model
class RecipeRequest(BaseModel):
    ingredients: str

# Home Page
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

# Generate Recipe Endpoint
@app.post("/generate")
async def generate_recipe(data: RecipeRequest):
    try:

        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": """
You are an expert chef.

Generate a recipe using the ingredients provided.

Return in this format:

🍽 Recipe Name

📝 Ingredients

👨‍🍳 Instructions

⏱ Cooking Time

🥗 Nutritional Benefits
"""
                },
                {
                    "role": "user",
                    "content": data.ingredients
                }
            ],
            temperature=0.7,
            max_tokens=800
        )

        return {
            "response": completion.choices[0].message.content
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )