from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    """Root function"""
    return "Welcome FastAPI"
