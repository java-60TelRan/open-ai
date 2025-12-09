from pydantic import BaseModel, Field
class BaseTravelResponse(BaseModel):
    countryFrom: str
    countryTo: str
class TravelResponseOptional(BaseExceptionGroup):
    capitalTo: str | None = None
    weat