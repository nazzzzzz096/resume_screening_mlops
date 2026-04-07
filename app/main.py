from fastapi import FastAPI
from pydantic import BaseModel
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import joblib


# Initialize app
app = FastAPI()
semantic_model = SentenceTransformer('all-MiniLM-L6-v2')
# Load model & data ONCE 
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

df = pd.read_csv("data/processed_resume.csv")
df['skills'] = df['skills'].apply(eval)

# Request schema
class SearchRequest(BaseModel):
    resume_text: str
    skills: list[str]


def predict_role(text):
    vec = vectorizer.transform([text])
    return model.predict(vec)[0]


def calculate_match_score(candidate_skills, required_skills):
    return len(set(candidate_skills) & set(required_skills))


@app.get("/")
def home():
    return {"message": "Resume Screening API is running 🚀"}


@app.post("/search")
def search_candidates(request: SearchRequest):
    # Step 1: Predict role
    predicted_role = predict_role(request.resume_text)

    # Step 2: Filter candidates
    df_filtered = df[df['Category'] == predicted_role].copy()

    # Encode query
    query_embedding = semantic_model.encode(request.resume_text)

# Compute similarity
    df_filtered['score'] = df_filtered['Resume'].apply(
    lambda text: cosine_similarity(
        [query_embedding],
        [semantic_model.encode(text)]
    )[0][0]
)

    # Step 4: Get top candidates
    top = df_filtered.sort_values(by='score', ascending=False).head(5)

    # Step 5: Return response
    results = top[['name', 'email', 'phone', 'skills', 'score']].to_dict(orient="records")

    return {
        "predicted_role": predicted_role,
        "top_candidates": results
    }