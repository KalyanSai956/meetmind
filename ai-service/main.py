from fastapi import FastAPI

app = FastAPI(title="MeetMind AI Service")

@app.get("/")
def root():
    return {
        "message":"MeetMind AI service is running"
    }
    
@app.get("/health")
def health():
    return {
        "status":"healthy"
    }