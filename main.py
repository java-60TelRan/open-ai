from fastapi import Depends, FastAPI
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError

from auth.accounting import userStatistics
from auth.authentication import authentication
from auth.authorization import authAdmin
from exceptions.handlers import registerExceptionHandlers
from middleware.validation import validation_middleware
from models.travel_request import TravelRequest
from models.travel_response import TravelResponse
from service.travel_info_service import  travel_info
from logger import logger
app = FastAPI()
app.middleware("http")(validation_middleware)
registerExceptionHandlers(app)
@app.get("/travel/info", response_model=TravelResponse)
async def travelInfoGetHandler(countryFrom:str, countryTo:str|None = None,
                               cityTo: str|None = None , user = Depends(authentication)):
    try:
        travelRequest = TravelRequest(countryFrom=countryFrom, countryTo=countryTo, cityTo=cityTo,
                                    iscapital=True, iscurrency=True, isweather=True)
    except ValidationError as e:
        raise RequestValidationError(e.errors())    
    logger.debug("API GET endpoint travel/info: countryFrom: %s, %s, user: %s", countryFrom,
                 f"countryTo: {countryTo}" if countryTo else f"cityTo: {cityTo}", user["username"])
    user["count"] += 1
    return travel_info(travelRequest)
@app.post("/travel/info", response_model=TravelResponse)
async def travelInfoPostHandler(travelRequest: TravelRequest, user = Depends(authentication)):
    logger.debug("API POST endpoint travel/info: request: %s, user: %s", travelRequest, user["username"])
    user["count"] += 1
    return travel_info(travelRequest)
@app.get("/users/statistics")
def getUserStatistics(user = Depends(authAdmin)):
    return userStatistics()
    
   
