from fastapi import FastAPI

app = FastAPI(title="Task Workflow API")

@app.get("/health")
def health_check():
    return {"status": "ok"}
