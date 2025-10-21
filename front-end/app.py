import streamlit as st
import requests

#URL da API FastAPI
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Estoque HARDWARE",page_icon="⚙")
st.title("Estoque de Produtos HARDWARE ⚙")

#Menu lateral
menu = st.sidebar.radio("Navegação", ["Catálogo", "Adicionar Produto", "Atualizar Produto", "Deletar"])
