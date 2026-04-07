
# 🚀 AI Resume Screening System (MLOps Project)

## 📌 Project Overview

This project implements a **simplified MLOps pipeline** for a machine learning-based resume screening system.
It combines **machine learning, API development, containerization, CI/CD, and monitoring** into a complete production-ready workflow.

The system allows HR users to input job requirements and automatically retrieves the most relevant candidates based on:

* Job role prediction (ML model)
* Semantic similarity (NLP)
* Candidate ranking

---

## 🧠 Key Features

* ✅ Resume classification using **TF-IDF + Logistic Regression**
* ✅ Semantic search using **Sentence Transformers**
* ✅ REST API built with **FastAPI**
* ✅ Interactive UI using **Streamlit**
* ✅ Dockerized application for portability
* ✅ CI pipeline with **GitHub Actions + pytest**
* ✅ Monitoring with **Prometheus**

---

## 🏗️ Project Architecture

```
User Input (UI)
      ↓
Streamlit Frontend
      ↓
FastAPI Backend
      ↓
ML Model (Role Prediction)
      ↓
Semantic Search (Embeddings)
      ↓
Top Candidate Results
```

---

## 📂 Project Structure

```
resume-screening-mlops/
│
├── app/
│   ├── main.py          # FastAPI backend
│   └── ui.py            # Streamlit frontend
│
├── src/
│   ├── model_training.py
│   ├── skill_extraction.py
│   └── pipeline.py
│
├── data/
│   ├── Enhanced_Resume_Data.csv
│   └── processed_resume.csv
│
├── tests/
│   └── test_api.py      # Pytest tests
│
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── Dockerfile
├── start.sh
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/resume-screening-mlops.git
cd resume-screening-mlops
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run Backend (FastAPI)

```
uvicorn app.main:app --reload
```

### 4️⃣ Run UI (Streamlit)

```
streamlit run app/ui.py
```

---

## 🐳 Docker Setup

### Build Docker Image

```
docker build -t resume-screening .
```

### Run Container

```
docker run -p 8000:8000 -p 8501:8501 resume-screening
```

### Access Application

* API Docs → http://localhost:8000/docs
* UI → http://localhost:8501

---

## ☁️ Cloud Deployment (AWS EC2)

1. Launch EC2 instance (Ubuntu)
2. Install Docker
3. Pull image from Docker Hub:

```
docker pull yourusername/resume-screening
```

4. Run container:

```
docker run -d -p 80:8501 yourusername/resume-screening
```

### 🌐 Live Application

👉 http://your-ec2-ip

---

## 🔄 CI Pipeline (GitHub Actions)

* Automated testing using **pytest**
* Runs on every push to `main`

### Run tests locally:

```
pytest
```

---

## 📊 Monitoring (Prometheus)

Metrics endpoint:

```
http://localhost:8000/metrics
```

Tracks:

* Request count
* Response time
* API performance

---

## 🧪 Sample API Request

### POST `/search`

```json
{
  "resume_text": "Looking for Python developer with NLP experience",
  "skills": ["python", "nlp"]
}
```

### Response

```json
{
  "predicted_role": "Python Developer",
  "top_candidates": [
    {
      "name": "John Doe",
      "email": "john@example.com",
      "phone": "1234567890",
      "skills": ["python", "nlp"],
      "score": 0.92
    }
  ]
}
```

---

## 🧠 Technologies Used

* Python
* scikit-learn
* Sentence Transformers
* FastAPI
* Streamlit
* Docker
* GitHub Actions (CI)
* Prometheus

---

## 🎯 Key Learnings

* End-to-end ML system design
* Model deployment with Docker
* CI/CD pipeline setup
* API development and integration
* Handling dependency/version issues
* Monitoring ML systems

---

## 🚀 Future Improvements

* Add resume upload (PDF parsing)
* Use database instead of CSV
* Optimize semantic search performance
* Add authentication & user roles
* Deploy with Kubernetes

---

## 👩‍💻 Author

**Nazina N**

* Data Science & MLOps Enthusiast
* LinkedIn: https://www.linkedin.com/in/nazina2001

---

## 📌 Note

Model files (`.pkl`) are included for inference.
Ensure matching library versions for reproducibility.

---
