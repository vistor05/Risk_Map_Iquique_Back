from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from py import Datamining

app = FastAPI()
app.mount("/maps", StaticFiles(directory="mapas"), name="static")
templates = Jinja2Templates(directory="./mapas")

@app.get('/map/{id}', response_class=HTMLResponse)
async def map(request: Request, id:int ): #Aqui se insertará algun parametro
    Datamining.execute_scripts()
    if (id ==1):
        return templates.TemplateResponse("Map1.html", context={"request": request, "id": 1})
    elif (id == 2):
        return templates.TemplateResponse("Map2.html", context={"request": request, "id": 2})
    else:
        return templates.TemplateResponse("Map3.html", context={"request": request, "id": 3})



