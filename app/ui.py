import streamlit as st
import requests

# API endpoint
API_URL = "http://127.0.0.1:8000/search"

st.set_page_config(page_title="Resume Screening System", layout="wide")

st.title("🚀 AI Resume Screening System")

st.write("Enter job requirement and skills to find best candidates")

# Input fields
resume_text = st.text_area("📝 Job Description / Requirement")

skills_input = st.text_input("💡 Required Skills (comma separated)")

# Convert skills
skills = [skill.strip().lower() for skill in skills_input.split(",") if skill]

# Button
if st.button("🔍 Find Candidates"):
    if resume_text and skills:
        response = requests.post(API_URL, json={
            "resume_text": resume_text,
            "skills": skills
        })

        if response.status_code == 200:
            data = response.json()

            st.success(f"🎯 Predicted Role: {data['predicted_role']}")

            st.subheader("🏆 Top Candidates")

            for candidate in data["top_candidates"]:
                st.write("----")
                st.write(f"👤 Name: {candidate['name']}")
                st.write(f"📧 Email: {candidate['email']}")
                st.write(f"📞 Phone: {candidate['phone']}")
                st.write(f"🛠 Skills: {', '.join(candidate['skills'])}")
                st.write(f"⭐ Score: {candidate['score']}")
        else:
            st.error("API Error ❌")
    else:
        st.warning("Please enter both text and skills")