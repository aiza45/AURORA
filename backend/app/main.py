from fastapi import FastAPI

app = FastAPI(
    title="AURORA",
    description="Enterprise Multi-Agent Intelligence Platform",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to AURORA 🚀"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "version": "0.1.0"
    }