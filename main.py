from fastapi import FastAPI
from pydantic import BaseModel
import json
from difflib import SequenceMatcher

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("data/faqs.json", "r") as f:
    faqs = json.load(f)

class QueryRequest(BaseModel):
    query: str


def similarity(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def find_best_match(user_query):
    best_match = None
    best_score = 0

    for faq in faqs:
        score = similarity(user_query, faq["question"])
        if score > best_score:
            best_score = score
            best_match = faq

    return best_match, best_score


# 🧠 NEW: handle greetings + small talk
def handle_small_talk(query):
    q = query.lower()

    if any(word in q for word in ["hi", "hello", "hey"]):
        return "Hello 👋 How can I assist you today with your account or orders?"

    if "thank" in q:
        return "You're welcome 😊 Happy to help!"

    if "bye" in q:
        return "Goodbye 👋 Have a great day!"

    return None


@app.post("/ask")
def ask(request: QueryRequest):
    query = request.query.strip()

    small_talk = handle_small_talk(query)
    if small_talk:
        return {
            "answer": small_talk,
            "type": "small_talk"
        }

    match, score = find_best_match(query)

    if score < 0.4 or not match:
        return {
            "answer": "Sorry, I couldn't find that. Please contact customer support or rephrase your question.",
            "type": "fallback"
        }

    return {
        "answer": match["answer"],
        "type": "faq",
        "confidence": round(score, 2)
    }