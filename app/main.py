from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
""" 
@app.get("/recommend")
async def recommend(movie_name: str = Query(...), num_recommendations: int = Query(5)):
    recommendations = get_recommendations(movie_name, num_recommendations)
    return {"recommendations": recommendations}
 """