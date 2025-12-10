import json
from fastapi import Request, Response
from logger import logger


async def logging_middleware(request: Request, call_next):
    logger.debug("request body %s", request.body() if request.method == "POST" else "Method GET doesn't have body in request")
    resp: Response = await call_next(request)
    body = b""
    async for chunk in resp.body_iterator:
        body += chunk

    # 4. Try JSON parse
    try:
        json_body = json.loads(body)
    except Exception:
        json_body = None

    logger.debug("RESPONSE raw=%s json=%s", body, json_body)

    # 5. Rebuild the response (CRITICAL!)
    return Response(
        content=body,
        status_code=resp.status_code,
        headers=dict(resp.headers),
        media_type=resp.media_type,
    )
    
    