import streamlit as st
from utils.functions import *
import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()


def login():
    """ Simple Login App """
    menu = ["Login", "SignUp"]
    choice = st.sidebar.selectbox("", menu)

    if choice == "Login":
        st.sidebar.header("Sign in")
        username = st.sidebar.text_input("User name")
        password = st.sidebar.text_input("Password", type="password")

        if st.sidebar.button("Login"): 
            create_usertable(c)
            result = login_user(c, username, password)
            if result:
                st.sidebar.success(f"Logged in as {username}.")
            else:
                st.sidebar.warning("Incorrect Username/Password")

    elif choice == "SignUp":
        st.sidebar.subheader("Create new account")
        new_user = st.sidebar.text_input("Username")
        new_password = st.sidebar.text_input("Password", type='password')

        if st.sidebar.button("SignUp"):
            create_usertable(c)
            add_userdata(c, conn, new_user, new_password)
            st.sidebar.success("You have successfully created a valid account. Now login with your account.")
    

def main():

    st.set_page_config(
    page_title="Finance Up",
    page_icon="👋",
    )

    login()
    
    st.title("FinanceUp - Gerenciamento Financeiro")

    renda_total = st.number_input("Informe sua renda total:", min_value=0.0)
    
    # Gastos essenciais  
    num_gastos_essenciais = st.number_input("Quantos gastos essenciais você tem?", min_value=0, max_value=10, value=0)
    gastos_essenciais = []
    for i in range(num_gastos_essenciais):
        nome_gasto_essencial = st.text_input(f"Informe o nome do gasto {i+1}:")
        valor_gasto_essencial = st.number_input(f"Informe o valor do gasto {i+1}:", min_value=0.0)
        gastos_essenciais.append((nome_gasto_essencial, valor_gasto_essencial))

    
    # Gastos não-essenciais
    num_gastos_nao_essenciais = st.number_input("Quantos gastos não-essenciais você tem?", min_value=0, max_value=10, value=0)
    gastos_nao_essenciais = []
    for i in range(num_gastos_nao_essenciais):
        nome_gasto_nao_essencial = st.text_input(f"Informe o nome do gasto não essencial {i+1}")
        valor_gasto_nao_essencial = st.number_input(f"Informe o valor do gasto não-essencial {i+1}:", min_value=0.0)
        gastos_nao_essenciais.append((nome_gasto_nao_essencial, valor_gasto_nao_essencial))

    
    # Investimentos
    num_investimentos = st.number_input("Quantos investimentos você quer fazer?:", min_value=0, max_value=10, value=0)
    investimentos = []
    for i in range(num_investimentos):
        nome_investimento = st.text_input(f"Informe o nome do investimento {i+1}:")
        valor_investimento = st.number_input(f"Informe o valor do investimento {i+1}:", min_value=0.0)
        investimentos.append((nome_investimento, valor_investimento))


    # Gerando um gráfico com as informações
    st.subheader("Gráfico de Gastos")
    button_grafico = st.button("Gerar gráfico")
    if button_grafico:
        create_grafico(renda_total, gastos_essenciais, gastos_nao_essenciais, investimentos)
        

    # Exportanto planilha
    st.subheader("Exportar para Planilha")
    if st.button("Exportar"):
        export_planilha(renda_total, gastos_essenciais, gastos_nao_essenciais, investimentos)


if __name__ == '__main__':
    main()