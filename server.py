from fastapi import FastAPI

app = FastAPI()


@app.get("/")  # @ decorator router
async def root():
    return {"message": "this is my simple FastAPI init"}


@app.get("/profile")  # another decorator router
async def profile():
    return {"name": "David Rodrigues da Silva"}


@app.post("/profile")  # endpoint ou route
async def signup():
    return {"message": "Perfil criado com sucesso!"}


@app.put("/profile")
async def update():
    return {"message": "Perfil atualizado com sucesso!"}


@app.delete("/profile")
async def delete():
    return {"message": "Perfil deletado com sucesso!"}


@app.get("/greetings/{nome}/")
async def greetings(nome: str):
    texto = f'Olá, {nome.capitalize()}, seja bem vindo!'
    return {"message": texto}