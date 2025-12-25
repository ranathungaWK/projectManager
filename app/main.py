from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title = "project manager mock application")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       
    allow_credentials=True,
    allow_methods=["*"],        
    allow_headers=["*"],        
)

from app.api import auth , projects, reports , tasks


app.include_router(auth.router)
app.include_router(projects.router)
app.include_router(tasks.router)
app.include_router(reports.router)



@app.get("/")
def home():
    return {"message" : "welcome !"}