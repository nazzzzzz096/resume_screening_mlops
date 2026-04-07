import pandas as pd
import joblib

# Load model + vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def predict_role(text):
    vec = vectorizer.transform([text])
    return model.predict(vec)[0]


def calculate_match_score(candidate_skills, required_skills):
    return len(set(candidate_skills) & set(required_skills))


def get_top_candidates(resume_text, required_skills):
    # Step 1: Predict role
    predicted_role = predict_role(resume_text)

    # Step 2: Load processed data
    df = pd.read_csv("data/processed_resume.csv")
    df['skills'] = df['skills'].apply(eval)

    # Step 3: Filter by role
    df_filtered = df[df['Category'] == predicted_role].copy()

    # Step 4: Match skills
    df_filtered['score'] = df_filtered['skills'].apply(
        lambda skills: calculate_match_score(skills, required_skills)
    )

    # Step 5: Return top candidates
    top = df_filtered.sort_values(by='score', ascending=False).head(5)

    return predicted_role, top[['name', 'skills', 'score']]


if __name__ == "__main__":
    resume = "Looking for Python developer with NLP and ML experience"
    skills = ['python', 'nlp', 'machine learning']

    role, candidates = get_top_candidates(resume, skills)

    print("Predicted Role:", role)
    print(candidates)