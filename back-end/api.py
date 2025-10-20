from fastapi import FastAPI
from funcoes import listar_produtos, atualizar_produtos, deletar_produtos, inserir_produtos, buscar_produtos

# python -m uvicorn api:app --reload

app = FastAPI(title="Estoque de Produtos HARDWARE")

@app.get("/")
def home():
    return {"mensagem": "Bem-Vindo ao Estoque de Produtos HARWARE"}

@app.post("/produtos")
def criar_produtos(nome: str, categoria: str, preco: float, quantidade: int):
    inserir_produtos(nome, categoria, preco, quantidade)
    return { "mensagem": "Produto adicionado com sucesso!"}

@app.get("/produtos")
def exibir_produtos():
    produtos = listar_produtos()
    lista = []
    for linha in produtos:
        lista.append({"id": linha[0],
            "nome": linha[1],
            "categoria": linha[2],
            "preco": linha[3],
            "quantidade": linha[4]
            })
        
    return {"produtos": lista}

@app.put("/produtos/{id_produto}")
def update_produtos(id_produto: int,  novo_preco: float, nova_quantidade: int):
    atualizar_produtos(id_produto, novo_preco, nova_quantidade)
    produtos = buscar_produtos(id_produto)
    if produtos:
        atualizar_produtos(id_produto, novo_preco, nova_quantidade)
        return { "mensagem": "Produto atualizado com sucesso!"}
    else:
        return { "erro": "Produto não encontrado"}


@app.delete("/produtos")
def remover_produtos(id_produto: int):
    deletar_produtos(id_produto)
    produtos = buscar_produtos(id_produto)
    if produtos:
        deletar_produtos(id_produto)
        return { "mensagem": "Produto removido com sucesso!"}
    else:
        return { "erro": "Produto não encontrado!"}