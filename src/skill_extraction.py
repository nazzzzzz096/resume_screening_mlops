import pandas as pd

# Predefined skills list
SKILLS = [
    'python', 'machine learning', 'sql', 'deep learning',
    'nlp', 'tableau', 'power bi', 'excel', 'tensorflow'
]

def extract_skills(text):
    """Extract skills from resume text"""
    text = text.lower()
    found_skills = [skill for skill in SKILLS if skill in text]
    return list(set(found_skills))


def process_dataset(file_path):
    """Load dataset and extract skills"""
    df = pd.read_csv(file_path)
    df['skills'] = df['Resume'].apply(extract_skills)
    return df

if __name__ == "__main__":
    df = process_dataset("data/Enhanced_Resume_Data.csv")
    
    # SAVE UPDATED DATASET
    df.to_csv("data/processed_resume.csv", index=False)
    
    print(df[['name', 'skills']].head())