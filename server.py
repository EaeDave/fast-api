from fastapi import FastAPI

app = FastAPI()


@app.get("/")  # @ decorator
async def root():
    return {"message": "this is my simple FastAPI init"}
    