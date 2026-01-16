import streamlit as st
import random as rd
import dados

with st.form("Formulario de filmes:"):
    st.title("Filmes")

    nome = st.text_input("Coloque o nome de um filme:")

    ano_do_filme = st.number_input("Coloque o ano do filme:", min_value=2000, max_value=2026)

    nota_do_filme = st.slider("Coloque a nota do filme", min_value=0, max_value=10)

    if st.form_submit_button("Adicionar na tabela de filmes"):
        dados.inseri_dados(nome, ano_do_filme, nota_do_filme)
        st.write("Filme adicionado com sucesso!")


if st.checkbox("Quero alterar filmes da tabela, CLIQUE AQUI"):
    option = st.number_input("Digite o número de id para atualizar um filme:",format="%0.0f")
    
    nome = st.text_input("Coloque o nome do novo filme:")

    ano_do_filme = st.number_input("Coloque o ano do novo filme:", min_value=2000, max_value=2026)

    nota_do_filme = st.slider("Coloque a nota do novo filme", min_value=0, max_value=10)

    if st.button("Atualizar dados"):
        dados.update_dados(option, nome, ano_do_filme, nota_do_filme)

dados_dos_filmes = dados.ler_dados()

for dado in dados_dos_filmes:
    id, nome, ano, nota = dado
    
    dicionario_de_filmes = {
        "id":[f"{id}"],
        "Nome do filme":[f"{nome}"],
        "Ano do filme":[f"{ano}"],
        "Nota do filme":[f"{nota}"]
    }

    st.table(dicionario_de_filmes)
 
option = st.number_input("Digite o número de id para deletar um filme:",format="%0.0f")

if st.button("Deletar"):
    dados.deletar_dados(option)
    st.write("Filme apagado com sucesso!")