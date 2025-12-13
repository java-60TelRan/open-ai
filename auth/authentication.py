from fastapi import HTTPException, Header

from auth.accounting import API_KEYS


async def authentication (x_api_key = Header(..., alias="X-API-KEY")) -> dict:
    user: dict = API_KEYS.get(x_api_key)
    if not user:
        raise HTTPException (status_code=401, detail="Authentication Error")
    return user
     