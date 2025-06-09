"""
Before running this app ensure that 'uvicorn' is first installed
"""

from fastapi import FastAPI, HTTPException
from planet_info import planets
from other import help_text
from other import about_text

app = FastAPI(title="Solar System API")


@app.get("/planets/{name}")
async def get_planet_info(name: str):
    name = name.lower()
    if name not in planets:
        raise HTTPException(status_code=404, detail="Planet not found")
    return planets[name]

@app.get("/planets/{name}/{attribute}")
async def get_planet_attribute(name: str, attribute: str):
    name = name.lower()
    attribute = attribute.lower()
    if name not in planets:
        raise HTTPException(status_code=404, detail="Planet not found")
    planet = planets[name]
    if attribute not in planet:
        raise HTTPException(status_code=404, detail=f"Attribute '{attribute}' not found for planet '{name}'")
    return {attribute: planet[attribute]}

@app.get("/planets")
async def list_planets():
    return list(planets.keys())

@app.get("/help")
async def display_help():
    return help_text

@app.get("/about")
async def display_about():
    return about_text