import pandas as pd

def calculate_match_score(candidate_skills, required_skills):
    """Calculate how well a candidate matches required skills"""
    return len(set(candidate_skills) & set(required_skills))


def find_top_candidates(df, required_skills, top_n=5):
    """Return top matching candidates"""
    df['score'] = df['skills'].apply(
        lambda skills: calculate_match_score(skills, required_skills)
    )
    
    return df.sort_values(by='score', ascending=False).head(top_n)


if __name__ == "__main__":
    df = pd.read_csv("data/processed_resume.csv")

    # IMPORTANT: convert string → list
    df['skills'] = df['skills'].apply(eval)

    # Example HR requirement
    required_skills = ['python', 'machine learning', 'nlp']

    top_candidates = find_top_candidates(df, required_skills)

    print(top_candidates[['name', 'skills', 'score']])