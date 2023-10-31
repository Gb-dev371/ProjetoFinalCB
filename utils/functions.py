import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import openpyxl as opx


def create_dataframe(renda_total, gastos_essenciais, gastos_nao_essenciais, investimentos):
    # Calculando a renda restante
    gastos_total = sum([gasto[1] for gasto in gastos_essenciais + gastos_nao_essenciais + investimentos])
    renda_restante = renda_total - gastos_total
    
    # Criando um DataFrame com as informações dos gastos e renda restante
    data = {
        'Campo': [gasto_essencial[0] for gasto_essencial in gastos_essenciais] + [gasto_nao_essencial[0] for gasto_nao_essencial in gastos_nao_essenciais] + [investimento[0] for investimento in investimentos] + ['Renda Restante'],
        'Valor': [gasto_essencial[1] for gasto_essencial in gastos_essenciais] + [gasto_nao_essencial[1] for gasto_nao_essencial in gastos_nao_essenciais] + [investimento[1] for investimento in investimentos] + [renda_restante]
    }
    df = pd.DataFrame(data)
    return df


def create_grafico(renda_total, gastos_essenciais, gastos_nao_essenciais, investimentos):
    fig, ax = plt.subplots()
    df = create_dataframe(renda_total, gastos_essenciais, gastos_nao_essenciais, investimentos)
    ax.pie(df['Valor'], labels=df['Campo'], autopct='%1.1f%%')
    ax.set_title('Gráfico de Gastos')
    st.pyplot(fig)


def export_planilha(renda_total, gastos_essenciais, gastos_nao_essenciais, investimentos):
    df = create_dataframe(renda_total,gastos_essenciais,gastos_nao_essenciais,investimentos)
    file = df.to_excel("dados.xlsx",index = False)
    st.dataframe(df)
    st.success("Planilha exportada com sucesso!")


def create_usertable(c):
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')

def add_userdata(c, conn, username, password):
    c.execute('INSERT INTO userstable(username, password) VALUES (?,?)', (username, password))
    conn.commit()

def login_user(c, username, password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?', (username, password))
    data = c.fetchall()
    return data

def view_all_users(c):
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data