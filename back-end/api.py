from fastapi import FastAPI
from funcoes import listar_produtos, atualizar_produtos, deletar_produtos, inserir_produtos

# python -m uvicorn api:app --reload

app = FastAPI(title="Estoque de Produtos HARDWARE")

@app.get("/")
def home():
    return {"mensagem": "Bem-Vindo ao Estoque de Produtos HARWARE"}

@app.post("/produtos")
def criar_produtos(nome: str, categoria: str, preco: float, quantidade: int):
    inserir_produtos(nome, categoria, preco, quantidade)
    return { "mensagem": "Produto adicionado com sucesso!"}
