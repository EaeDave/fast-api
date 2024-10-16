from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

app = FastAPI()

class Animal(BaseModel):
    id: Optional[int] = None  # Valor padrão que será dado caso não seja informado o campo
    nome: str
    idade: int
    sexo: str
    cor: str
    
    
banco_dados: List[Animal] = []


@app.post("/animais")
async def cadastrar_animal(animal: Animal):
    animal.id = uuid4()
    banco_dados.append(animal)
    return {"message": "Animal cadastrado com sucesso!"}


@app.get("/animais")
async def listar_animais():
    return banco_dados