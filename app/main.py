from fastapi import FastAPI

app = FastAPI(title="Task Workflow API")

@app.get("/health")
def health_check():
    return {"status": "ok"}

from app.api.routes import auth

app.include_router(auth.router)