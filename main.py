from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/maps", StaticFiles(directory="mapas"), name="static")
templates = Jinja2Templates(directory="./mapas")



@app.get('/map/basic', response_class=HTMLResponse)
async def map(request: Request):
    return templates.TemplateResponse("Map-Basic.html", context={"request": request, "id": 1})


@app.get('/map/hr', response_class=HTMLResponse)
async def map(request: Request):
    return templates.TemplateResponse("Map-Hr.html", context={"request": request, "id": 2})


@app.get('/map/level-affectation', response_class=HTMLResponse)
async def map(request: Request):
    return templates.TemplateResponse("Map-Affectation.html", context={"request": request, "id": 3})


#@app.get('/map/execute/{type_map}')
# async def map(type_map: str):
#     print(type_map)
#     if(type_map == 'basic'):
#        execute_script('basic')
#        return Response(status_code=202)
#     elif(type_map == 'hr'):
#         execute_script('hr')
#         return Response(status_code=202)
#     elif(type_map == 'affectation'):
#         execute_script('affectation')
#         return Response(status_code=202)
#     else:
#         return Response(status_code=404) 





