import json
from fastapi import Request, Response
from logger import logger
from middleware.common import extractResponseBody, rebuildResponse


async def logging_middleware(request: Request, call_next):
    # logger.debug("request body %s", request.body() if request.method ==
    #              "POST" else "Method GET doesn't have body in request")
    resp: Response = await call_next(request)
    body, json_body = await extractResponseBody(resp)

    logger.debug("RESPONSE raw=%s json=%s", body, json_body)

    # 5. Rebuild the response (CRITICAL!)
    return rebuildResponse(resp, body)


