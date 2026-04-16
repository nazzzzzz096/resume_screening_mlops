import streamlit as st
import requests
import time

# API endpoint
API_URL = "http://127.0.0.1:8000/search"

st.set_page_config(page_title="Resume Screening System", layout="wide")

st.title("🚀 AI Resume Screening System")

st.write("Enter job requirement and skills to find best candidates")

# -------------------- Input --------------------
resume_text = st.text_area("📝 Job Description / Requirement")
skills_input = st.text_input("💡 Required Skills (comma separated)")

skills = [skill.strip().lower() for skill in skills_input.split(",") if skill]

# -------------------- API Call Function --------------------
def call_api(payload, retries=5, delay=2):
    for attempt in range(retries):
        try:
            response = requests.post(API_URL, json=payload, timeout=10)
            return response
        except requests.exceptions.RequestException as e:
            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise e

# -------------------- Button --------------------
if st.button("🔍 Find Candidates"):
    if not resume_text or not skills:
        st.warning("Please enter both text and skills")
    else:
        payload = {
            "resume_text": resume_text,
            "skills": skills
        }

        try:
            with st.spinner("🔄 Processing..."):
                response = call_api(payload)

            # -------------------- Handle Response --------------------
            if response.status_code == 200:
                data = response.json()

                if "error" in data:
                    st.error(f"Server Error: {data['error']}")
                else:
                    st.success(f"🎯 Predicted Role: {data['predicted_role']}")

                    st.subheader("🏆 Top Candidates")

                    if not data["top_candidates"]:
                        st.info("No matching candidates found.")
                    else:
                        for candidate in data["top_candidates"]:
                            st.write("----")
                            st.write(f"👤 Name: {candidate['name']}")
                            st.write(f"📧 Email: {candidate['email']}")
                            st.write(f"📞 Phone: {candidate['phone']}")
                            st.write(f"🛠 Skills: {', '.join(candidate['skills'])}")
                            st.write(f"⭐ Score: {round(candidate['score'], 4)}")

            else:
                st.error(f"API Error ❌ (Status Code: {response.status_code})")

        except requests.exceptions.ConnectionError:
            st.error("🚫 Cannot connect to backend. Please try again in a few seconds.")

        except requests.exceptions.Timeout:
            st.error("⏳ Request timed out. Backend might be busy.")

        except Exception as e:
            st.error(f"Unexpected error: {str(e)}")