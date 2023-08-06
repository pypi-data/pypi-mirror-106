# makeapi
A small package, that allows you to make an API.

## Example

```py
import makeapi

request_handler = makeapi.MakeAPIRequest
app = MakeAPI("localhost", 8000, request_handler) # localhost is your local computer

# Currently, it only has get request method.

@app.get("/main")
def main(request : makeapi.Request):
    return makeapi.textresp("Hello!")
    
app.run()    

# Go to http://localhost:8000/main in your browser and you should see Hello!
```

## Example with path params

```py
import makeapi

request_handler = MakeAPIRequest
app = MakeAPI("localhost", 8000, request_handler)

# you can only have 1 parameter.

@app.get("/params")
def params_route(request : makeapi.Request):
    params = request.args
    return jsonresp(params)    

app.run()

# Go to http://localhost:8000/params?hello=hi and it should show {"hello": "hi"}
```

Enjoy!
