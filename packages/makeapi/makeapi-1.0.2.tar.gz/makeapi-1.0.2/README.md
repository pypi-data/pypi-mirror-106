# makeapi
A small package, that allows you to make an API.

## Example

```py
import makeapi

request_handler = makeapi.MakeAPIRequestHandler
app = MakeAPI("localhost", 8000, request_handler)

# Currently, it only has get request method.

@app.get("/main")
def main(request : makeapi.Request):
    return makeapi.textresp("Hello!")

# Go to http://localhost:8000/main in your browser and you should see Hello!
```

## Example with path params

```py
import makeapi

request_handler = makeapi.MakeAPIRequestHandler
app = MakeAPI("localhost", 8000, request_handler)

@app.get("/params")
def params_route(request : makeapi.Request):
    param = request.args.get("hello")
    return textparam(param[0])

# Go to http://localhost:8000/params?hello=hi and it should show hi
```

Enjoy!
