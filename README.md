# HW#41
## Update class TravelRequest
### there should be only one out of the following fields
countryTo<br>
cityTo<br>
#### add custom validation for previous requirement
#### update logic of creating TravelResponse
if there is cityTo in request, response should contain both countryTo and cityTo<br>
if there is cityTo in request, weather result should be for cityTo and currency code / name should be for countryTo<br>
if there is countryTo in request, response should contain only countryTo and weather result should be for capitalTo
### there should be introduced authentication / authorization
#### introduce API_KEYS
two users with role "user" and different "username" values<br>
one admin with role "admin" and "username" as "admin"<br>
#### introduce dependency function for roles "user" and "admin"
request POST "/travel/info" - dependency for role "user"<br>
request GET "/travel/info" - dependency for role "user"<br>
request GET "/users/statistics (new request) - dependency for role "admin"
## Add new request
request GET "/users/statistics" returns dictionary with a username as the key and count of requests done by the appropriate user of any role




