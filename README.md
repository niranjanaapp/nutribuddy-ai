# 🍎 NutriBuddy AI — Smart Recipe & Nutrition Guide

NutriBuddy AI is a lightweight, responsive web application designed to reduce food waste and promote healthy eating. Users can type in whatever ingredients they currently have in their kitchen, and the app instantly utilizes the advanced **Llama 3.3 70B** model via the **Groq SDK** to generate a custom recipe along with its nutritional breakdown.

---

## ✨ Features
* **Instant Recipe Generation:** Enter raw ingredients and instantly get back full cooking instructions.
* **Nutrition-Focused:** Every recipe comes with a tailored breakdown of nutritional benefits.
* **Minimalist UI:** A clean, modern user interface built from scratch using pure HTML and CSS.
* **High-Performance Backend:** Powered by FastAPI with cross-origin resource sharing (CORS) enabled.

---

## 🛠️ Tech Stack
* **Backend:** Python, FastAPI
* **AI Integration:** Groq SDK (`llama-3.3-70b-versatile`)
* **Frontend:** HTML5, CSS3, JavaScript (Fetch API)
* **Environment Management:** Python-dotenv

---

## 🚀 How to Run Locally

### 1. Prerequisites
Make sure you have Python installed on your computer.

### 2. Setup & Installation
Clone or download this folder, open your terminal inside the project directory, and run:
```bash
pip install fastapi[standard] groq python-dotenv