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


@app.get("/quadrado/{numero}")  # route param
async def quadrado(numero:int):
    resultado = numero * numero
    return {"Message": f"O quadrado do número {numero} é = {resultado}"}


@app.get("/dobro")  # query string  localhost:8000/dobro?valor=8
async def dobro(value: int):
    dobro = f"O dobro de {value} é = {value * 2}"
    return {"message": dobro}


@app.get("/matematica")  # query string localhost:8000/matematica?num_1=5&num_2=5
async def somar(num_1:int = 0, num_2:int = 0):  # 0 now is a placeholder, a default value to param
    soma = num_1 + num_2
    return {"soma": f"A soma entre {num_1} + {num_2} é = {soma}"}