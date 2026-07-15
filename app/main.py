from fastapi import FastAPI, HTTPException
from app.schemas.cliente import Cliente
from app.models.cliente import clientes_db, proximo_id

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "BuffetFlow no ar"}

@app.post("/clientes")
def criar_cliente(cliente: Cliente):
    
    global proximo_id
    novo_cliente = cliente.model_dump()
    novo_cliente["id"] = proximo_id
    for cliente_existente in clientes_db:
        if cliente_existente['telefone'] == cliente.telefone:
            raise HTTPException(status_code=400, detail="Telefone já cadastrado")
            
    clientes_db.append(novo_cliente)
    proximo_id += 1
    return novo_cliente

@app.get("/clientes")
def listar_clientes() -> list[Cliente]:
    return clientes_db