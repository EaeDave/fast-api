from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4

app = FastAPI()

class Animal(BaseModel):
    id: Optional[str] = None  # Valor padrão que será dado caso não seja informado o campo
    nome: str
    idade: int
    sexo: str
    cor: str
    
    
banco_dados: List[Animal] = []


@app.post("/animais")
async def cadastrar_animal(animal: Animal):
    animal.id = str(uuid4())
    banco_dados.append(animal)
    return {"message": "Animal cadastrado com sucesso!"}


@app.get("/animais")
async def listar_animais():
    return banco_dados


@app.get("/animais/{animal_id}")
async def listar_animal_por_id(animal_id: str):
    for animal in banco_dados:
        if animal.id == animal_id:
            return animal
    return {"erro": "id não encontrado no banco de dados."}


@app.delete("/animais/{animal_id}")
def remover_animal_por_id(animal_id: str):
    executar = False
    for index, animal in enumerate(banco_dados):
        if animal.id == animal_id:
            posicao = index
            executar = True
            break
        
    if executar:
        banco_dados.pop(posicao)
        return {"message": f"Animal {animal.nome} removido com sucesso!"}
    else:
        return {"message": "id não encontrado no banco de dados."}
    
   
