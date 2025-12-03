import json
import re
from system_rules import INNER_SYSTEM_CONTENT

def travelInfoProvider(countryFrom: str, countryTo: str, codeFrom: str):
    from chat_request import chatRequest
    messages: list[dict] = [
        {"role":"system", "content": INNER_SYSTEM_CONTENT},
        {"role":"user", "content": f"currency of {countryTo}"}
    ]
    resp = chatRequest(messages)
    regex:str = r"\{.*\}"
    match: re.Match = re.search(regex, resp, re.DOTALL)
    res = None
    if match:
        try:
            res = json.loads(match.group())
        except Exception:
            pass    
       
    
    return json.dumps({"countryFrom": countryFrom, "countryTo":countryTo,\
        "codeFrom":codeFrom, "codeTo": res["currency_code"], "exchangeRate":1})
 
TOOLS:dict = {
    "travelInfoProvider": travelInfoProvider
}