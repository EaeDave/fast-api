from fastapi import FastAPI

app = FastAPI()


@app.get("/")  # @ decorator router
async def root():
    return {"message": "this is my simple FastAPI init"}


@app.get("/profile")  # another decorator router
async def profile():
    return {"name": "David Rodrigues da Silva"}
    