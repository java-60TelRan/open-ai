API_KEYS = {
    "token-admin": {"role": "admin", "username":"admin", "count":0},
    "token-vasya": {"role": "user", "username":"Vasya", "count":0},
    "token-sara": {"role": "user", "username":"Sara", "count":0},
    
}
def userStatistics():
    return {user["username"]:user["count"] for user in API_KEYS.values() }
def incrementUsage(user: dict):
    user["count"] += 1