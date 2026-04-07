from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from prometheus_fastapi_instrumentator import Instrumentator
import pandas as pd
import joblib

app = FastAPI()

# Prometheus
Instrumentator().instrument(app).expose(app)

# Load models
semantic_model = SentenceTransformer('all-MiniLM-L6-v2')
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Load data
df = pd.read_csv("data/processed_resume.csv")
df['skills'] = df['skills'].apply(eval)

class SearchRequest(BaseModel):
    resume_text: str
    skills: list[str]


def predict_role(text):
    vec = vectorizer.transform([text])
    return model.predict(vec)[0]


@app.get("/")
def home():
    return {"message": "Resume Screening API is running 🚀"}


@app.post("/search")
def search_candidates(request: SearchRequest):
    predicted_role = predict_role(request.resume_text)

    df_filtered = df[df['Category'] == predicted_role].copy()

    query_embedding = semantic_model.encode(request.resume_text)

    df_filtered['score'] = df_filtered['Resume'].apply(
        lambda text: cosine_similarity(
            [query_embedding],
            [semantic_model.encode(text)]
        )[0][0]
    )

    top = df_filtered.sort_values(by='score', ascending=False).head(5)

    results = top[['name', 'email', 'phone', 'skills', 'score']].to_dict(orient="records")

    return {
        "predicted_role": predicted_role,
        "top_candidates": results
    }