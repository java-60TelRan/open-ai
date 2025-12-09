from pydantic import BaseModel
class TravelRequest(BaseModel):
    countryFrom: str
    countryTo: str
    iscapital: bool
    isweather: bool
    iscurrency: bool