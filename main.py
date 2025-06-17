from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="Documentación Risk Map Iquique",
    openapi_tags=[
        {
            "name": "Map",
            "description": "Vistas de mapas en formato HTML para los distintos mapas del sistema Risk Map Iquique."
        }
    ]
)

app.mount("/maps", StaticFiles(directory="mapas"), name="static")
templates = Jinja2Templates(directory="./mapas")


@app.get(
    '/map/basic',
    response_class=HTMLResponse,
    tags=["Map"],
    summary="Mapa básico",
    description="Devuelve un template HTML del mapa básico."
)
async def map_basic(request: Request):
    return templates.TemplateResponse("Map-Basic.html", context={"request": request, "id": 1})


@app.get(
    '/map/hr',
    response_class=HTMLResponse,
    tags=["Map"],
    summary="Mapa HR",
    description="Devuelve un template HTML del mapa con filtros de horas."
)
async def map_hr(request: Request):
    return templates.TemplateResponse("Map-Hr.html", context={"request": request, "id": 2})


@app.get(
    '/map/level-affectation',
    response_class=HTMLResponse,
    tags=["Map"],
    summary="Mapa por nivel de afectación",
    description="Devuelve un template HTML del mapa con filtros por nivel de afectación."
)
async def map_affectation(request: Request):
    return templates.TemplateResponse("Map-Affectation.html", context={"request": request, "id": 3})


# if __name__ == "__main__":
#     import os
#     import uvicorn
#     port = int(os.environ.get("PORT", 8000))  # Render define esta variable
#     uvicorn.run("main:app", host="0.0.0.0", port=port)



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





