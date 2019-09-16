

# This can be the entry point to call other function such as AI inference

# This can also be a lambda function or the entrypoint to call other functions on your backend


# ie: entry -> this file -> trigger event

# entry via rest api -> middle-ware -> this file -> trigger event

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.middleware.cors import CORSMiddleware

from starlette.endpoints import HTTPEndpoint

app = Starlette()
app.add_middleware(
    CORSMiddleware, allow_origins=["*"], allow_headers=["*"], allow_methods=["*"]
)

@app.route("/")
async def homepage(request):
        return JSONResponse({"message": "Hello World!"})


@app.route("/hello/{name}")
class hello(HTTPEndpoint):
    async def get(self, request, name=None):
        name = request.path_params['name']
        msg = f"Hello, {name}" if name else "Hello!"
        return JSONResponse({"message": msg}, status_code=200)

