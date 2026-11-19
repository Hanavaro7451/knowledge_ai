import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title="knowladge_ai",
    version="0.1",
    description="A simple web app for knowladge_ai",
    docs_url="/docs",
    redoc_url="/redoc",
    debug=True,
)

@app.get("/api/v1/health")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)