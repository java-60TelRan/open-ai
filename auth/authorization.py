from fastapi import Depends, HTTPException

from auth.authentication import authentication


async def authAdmin(user = Depends(authentication)):
    if user["role"] != "admin":
        raise HTTPException(status_code=403,
                            detail="Access Denied")
    return user    