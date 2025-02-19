from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette.requests import Request


app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/habitaciones", response_class=HTMLResponse)
async def habitaciones(request: Request):
    return templates.TemplateResponse("habitaciones.html", {"request": request})

@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/nosotros", response_class=HTMLResponse)
async def nosotros(request: Request):
    return templates.TemplateResponse("nosotros.html", {"request": request})

@app.get("/caracteristicas", response_class=HTMLResponse)
async def caracteristicas(request: Request):
    return templates.TemplateResponse("caracteristicas.html", {"request": request})

@app.get("/testimonios", response_class=HTMLResponse)
async def testimonios(request: Request):
    return templates.TemplateResponse("testimonios.html", {"request": request})

@app.get("/subscribirse", response_class=HTMLResponse)
async def subscribirse(request: Request):
    return templates.TemplateResponse("subscribirse.html", {"request": request})


@app.exception_handler(404)
async def not_found(request, exc):
    return templates.TemplateResponse("404.html", {"request": request})

from fastapi import Request

@app.get("/crear-cuenta", response_class=HTMLResponse)
async def crearcuenta(request: Request):
    # Obtener los parámetros de la URL
    checkin = request.query_params.get('checkin', '')
    checkout = request.query_params.get('checkout', '')
    habitaciones = request.query_params.get('habitaciones', '')
    huespedes = request.query_params.get('huespedes', '')
    return templates.TemplateResponse("crear-cuenta.html", {
        "request": request,
        "checkin": checkin,
        "checkout": checkout,
        "habitaciones": habitaciones,
        "huespedes": huespedes
    })
