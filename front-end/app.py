import streamlit as st
import requests
import pandas as pd

#URL da API FastAPI
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Estoque HARDWARE",page_icon="⚙")
st.title("Estoque de Produtos HARDWARE ⚙")

#Menu lateral
menu = st.sidebar.radio("Navegação", ["Catálogo", "Adicionar Produto", "Atualizar Produto", "Remover"])

if menu == "Catálogo":
    st.subheader("Todos os Produtos Disponíveis")
    response = requests.get(f"{API_URL}/produtos")
    if response.status_code == 200:
        produtos = response.json().get("produtos", [])
        if produtos:
                st.dataframe(produtos)
        else:
            st.error("Nenhum produto disponível")   
    else:
        st.error("Erro ao acessar a API")

elif menu == "Adicionar Produto":
    st.subheader("Adicionar Produtos")
    nome_produto = st.text_input("Digite o nome do produto: ")
    categoria_produto = st.text_input("Digite a categoria do produto: ")
    preco_produto = st.number_input("Digite o preço do produto:", max_value=10000, min_value=0, step=10)
    quantidade_produto = st.number_input("Digite a quantidade do produto: ", max_value=100, min_value=0, step=1)
    
    if st.button("Salvar"):
        dados = {"nome": nome_produto, "categoria": categoria_produto, "preco": preco_produto, "quantidade": quantidade_produto}
        response = requests.post(f"{API_URL}/produtos", params=dados)
        if response.status_code == 200:
            st.success("produto adicionado com sucesso!")
        else:
             st.error("Erro ao adicionar o produto")

elif menu == "Atualizar Produto":
    st.subheader("Atualizar Produto")
    id_produto = st.number_input("Digite o ID do produto: ", min_value=1)
    novo_preco = st.number_input("Digite o novo preço do produto:", max_value=10000, min_value=0, step=10)
    nova_quantidade = st.number_input("Digite a nova quantidade do produto: ", max_value=100, min_value=0, step=1)
    
    if st.button("Salvar"):
        dados = { "preco": novo_preco, "quantidade": nova_quantidade}
        response = requests.put(f"{API_URL}/produtos/{id_produto}", params=dados)
        if response.status_code == 200:
            st.success("produto atualizado com sucesso!")
        else:
             st.error("Erro ao atualizar o produto")

elif menu == "Remover":
    st.subheader("Remover Produto")
    id_produto = st.number_input("Digite o ID do produto: ", min_value=1)
    if st.button("Buscar Produto"):
        response = requests.get(f"{API_URL}/produtos/{id_produto}")
        if response.status_code == 200:
            produto = response.json()
            st.dataframe(pd.DataFrame([produto]))

            confirmar = st.checkbox("Confirmar remoção do produto")

            if confirmar:
                try:
                    delete_response = requests.delete(f"{API_URL}/produtos/{id_produto}")
                    if delete_response.status_code == 200:
                        st.success("Produto removido com sucesso!")
                    else:
                        st.error(f"Erro ao remover o produto: {delete_response.text}")
                except Exception as erro:
                    st.error(f"Erro ao remover o produto: {erro}")
        else:
            st.error("Produto não encontrado")