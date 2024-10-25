from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI example"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello, {name}!"}


@app.get("/items")
async def list_items(skip: int = 0, limit: int = 10):
    items = [f"Item {i}" for i in range(20)]
    return {"items": items[skip : skip + limit]}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
