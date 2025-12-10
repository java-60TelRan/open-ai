from fastapi import FastAPI

from exceptions.handlers import registerExceptionHandlers
from middleware.validation import validation_middleware
from models.travel_request import TravelRequest
from models.travel_response import TravelResponse
from service.travel_info_service import travel_full_info, travel_info

app = FastAPI()
app.middleware("http")(validation_middleware)
registerExceptionHandlers(app)
@app.get("/travel/info", response_model=TravelResponse)
async def travelInfoGetHandler(countryFrom:str, countryTo:str):
    return travel_full_info(countryFrom, countryTo)
@app.post("/travel/info", response_model=TravelResponse)
async def travelInfoPostHandler(travelRequest: TravelRequest):
    return travel_info(travelRequest)
    
   
