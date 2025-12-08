# HW#40
## Write FastAPI endpoints with validation and logging
### endpoint POST "/travel/info"
#### request body with following fields
- countryFrom (string, required)<br>
- countryTo (string, required)<br>
- iscapital (bool, required (true - a capital of the given countryTo should exist in a response, false - shouldn't exist))<br>
- isweather (bool, required (true - a string containing current values of temperature, humidity, condition, wind speed in the given countryTo should exist in a response, false - shouldn't exist))<br>
- iscurrency (bool, required (true - reponse should have fields related to currencies such as currencyCodeFrom, currencyCodeTo, currencyNameFrom, currencyNameTo, exchangeRate))
#### reponse body with following fields
- countryFrom (string, required)<br>
- countryTo (string, required)<br>
- capitalTo (string, optional (should exist only if iscapital in request is True, validation of it should be done in a middleware functionality))<br>
- weather (string, optional (should exist only if isweather in request is True, validation of it should be done in a middleware functionality))<br>
- currencyCodeFrom (string with length 3 symbols, optional (should exist only if iscurrency in request is True, validation of it should be done in a middleware functionality) )
- currencyCodeFrom (string with length 3 symbols, optional (should exist only if iscurrency in request is True, validation of it should be done in a middleware functionality) )
- currencyNameFrom (string , optional (should exist only if iscurrency in request is True, validation of it should be done in a middleware functionality) )
- currencyNameTo (string , optional (should exist only if iscurrency in request is True, validation of it should be done in a middleware functionality) )
- exchangeRate (float , optional (should exist only if iscurrency in request is True, validation of it should be done in a middleware functionality) )
### endpoint GET "/travel/info"
#### reponse body with following fields
- countryFrom (string, required)<br>
- countryTo (string, required)<br>
- capitalTo (string, required)<br>
- weather (string, required)<br>
- currencyCodeFrom (string with length 3 symbols, required )
- currencyCodeFrom (string with length 3 symbols, required)
- currencyNameFrom (string , required)
- currencyNameTo (string , required )
- exchangeRate (float , required )





