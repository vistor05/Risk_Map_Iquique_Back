from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from py import Datamining

app = FastAPI()
app.mount("/maps", StaticFiles(directory="mapas"), name="static")
templates = Jinja2Templates(directory="./mapas")

@app.get('/map', response_class=HTMLResponse)
async def map(request: Request):
    Datamining.execute_scripts()
    print("PASO")
    return templates.TemplateResponse("Map1.html", context={"request": request, "id": 1})



