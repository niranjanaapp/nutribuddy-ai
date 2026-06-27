import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from groq import Groq

# 1. Load the secret API key from our .env file
load_dotenv()

# 2. Build our FastAPI brain app
app = FastAPI(title="NutriBuddy AI Backend")

# 3. Allow our frontend webpage to talk to this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 4. Connect to Groq AI
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# 5. Define what the incoming data looks like
class RecipeRequest(BaseModel):
    ingredients: str

# 6. Create the endpoint your instructor requested (/generate)
@app.post("/generate")
async def generate_recipe(data: RecipeRequest):
    try:
        # Ask the AI to act like a professional chef
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system", 
                    "content": "You are NutriBuddy, a helpful and friendly culinary chef and nutritionist. The user will give you a list of ingredients. Respond with a quick, easy recipe name, step-by-step instructions, and a short note on the nutritional benefits."
                },
                {"role": "user", "content": f"Create a recipe using these ingredients: {data.ingredients}"}
            ],
            temperature=0.7,
            max_tokens=800
        )
        return {"response": completion.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))