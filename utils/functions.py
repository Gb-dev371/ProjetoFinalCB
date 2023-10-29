import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def create_dataframe(renda_total, gastos_essenciais, gastos_nao_essenciais, investimentos):
    # Criando um DataFrame com as informações
    data = {
        'Tipo de Gasto': ['Renda Total'] + [gasto_essencial[0] for gasto_essencial in gastos_essenciais] + [gasto_nao_essencial[0] for gasto_nao_essencial in gastos_nao_essenciais] + [investimento[0] for investimento in investimentos],
        'Valor': [renda_total] + [gasto_essencial[1] for gasto_essencial in gastos_essenciais] + [gasto_nao_essencial[1] for gasto_nao_essencial in gastos_nao_essenciais] + [investimento[1] for investimento in investimentos]
    }
    df = pd.DataFrame(data)
    return df


def create_grafico(renda_total, gastos_essenciais, gastos_nao_essenciais, investimentos):
    fig, ax = plt.subplots()
    df = create_dataframe(renda_total, gastos_essenciais, gastos_nao_essenciais, investimentos)
    ax.pie(df['Valor'], labels=df['Tipo de Gasto'], autopct='%1.1f%%')
    st.pyplot(fig)


def create_tabela(renda_total, gastos_essenciais, gastos_nao_essenciais, investimentos):
    df = create_dataframe(renda_total, gastos_essenciais, gastos_nao_essenciais, investimentos)
    st.dataframe(df)


def export_planilha(renda_total, gastos_essenciais, gastos_nao_essenciais, investimentos):
    df = create_dataframe(renda_total, gastos_essenciais, gastos_nao_essenciais, investimentos)
    df.to_excel("financeup_planilha.xlsx", index=False)
    st.success("Planilha exportada com sucesso!")