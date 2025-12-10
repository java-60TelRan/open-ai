import json
from fastapi import HTTPException, Request
from logger import logger
from middleware.common import extractResponseBody, rebuildResponse


def isMatch(travelRequest: dict, travelResponse: dict)->bool:
    isCurrencyRequest = travelRequest["iscurrency"] 
    isCapitalRequest = travelRequest["iscapital"]
    isWeatherRequest = travelRequest["isweather"]
    hasCurrencyResponse = travelResponse.get("exchangeRate") is not None
    hasCapitalResponse = travelResponse.get("capitalTo") is not None
    hasWeatherResponse = travelResponse.get("weatherTo") is not None
    return isCapitalRequest == hasCapitalResponse and isCurrencyRequest == hasCurrencyResponse and isWeatherRequest == hasWeatherResponse
    
async def validation_middleware(request: Request, call_next):
    requestBody = await request.body() if request.method == "POST" else None
    travelRequest = json.loads(requestBody)
    async def receive():
        return {"type": "http.request", "body": requestBody}

    request = Request(request.scope, receive)
    logger.debug("validation middleware received dictionary %s", travelRequest)
    resp = await call_next(request)
    response_raw_body, response_body = await extractResponseBody(resp)
    if not isMatch(travelRequest, response_body):
        raise HTTPException(
            status_code=500,
            detail=f"request {travelRequest} doesn't match with response {travelResponse}"
        )
    logger.debug("validation middleware got response %s", response_body)
    return rebuildResponse(resp, response_raw_body)
    
    