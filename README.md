# quotium-api

Returns a json response with some magical quotes on your property.

example: curl -i -H "Content-Type: application/json" -X POST -d '{"email":"read", "property_address":"5 my property address", "zip_code":14853,
 "number_bedrooms":5, "number_bathrooms":3, "square_footage":2500}' https://quotium-api.herokuapp.com/submit 
