import fastapi

global count
app = fastapi.FastAPI()


class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name
        
@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request, exc):
    return fastapi.responses.JSONResponse(
        status_code=418,
        content={"message": f"Oops! the Developer {exc.name} did something. There goes a rainbow..."},
    )


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/unicorn")
async def unicorn():
    raise UnicornException(name="Bobby")


