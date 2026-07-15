from pydantic import BaseModel
from typing import Optional


class Cliente(BaseModel):
    nome: str
    telefone: str 
    email: Optional[str] = None
    origem: Optional[str] = None 

