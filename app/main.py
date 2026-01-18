from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import json
import update_excel

app = FastAPI()

# API endpoint
@app.get("/api/data")
def get_latest():
    with open("data/latest.json") as f:
        return json.load(f)

@app.get("/api/status")
def get_latest():
    with open("data/status.txt") as f:
        return f.read()

@app.get("/api/status-refresh")
def refresh():
    update_excel.update()
    return "Refreshed successfully"


# Serve frontend
app.mount("/", StaticFiles(directory="frontend", html=True))
