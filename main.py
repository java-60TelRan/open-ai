from fastapi import FastAPI

from exceptions.handlers import registerExceptionHandlers
from middleware.logging import logging_middleware
from models.travel_request import TravelRequest
from models.travel_response import TravelResponse
from service.travel_info_service import travel_full_info, travel_info

app = FastAPI()
app.middleware("http")(logging_middleware)
registerExceptionHandlers(app)
@app.get("/travel/info")
async def travelInfoGetHandler(countryFrom:str, countryTo:str):
    return travel_full_info(countryFrom, countryTo)
@app.post("/travel/info")
async def travelInfoPostHandler(travelRequest: TravelRequest):
    return travel_info(travelRequest)
    
   
