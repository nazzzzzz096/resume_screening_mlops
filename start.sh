#!/bin/sh

echo "Starting FastAPI..."
uvicorn app.main:app --host 0.0.0.0 --port 8000 &
UVICORN_PID=$!

echo "Waiting for FastAPI to initialize..."
sleep 10

if ! kill -0 $UVICORN_PID 2>/dev/null; then
    echo "❌ FastAPI failed to start"
    exit 1
fi

echo "Starting Streamlit..."
streamlit run app/ui.py --server.port 8501 --server.address 0.0.0.0

wait