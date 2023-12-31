﻿# ProjetoFinalCB

FinanceUp, uma plataforma de gestão financeira na qual é possível controlar seus gastos e ganhos financeiros, vizualizar planilha e gráficos de gastos e simular investimentos. Tudo com o intuito de facilitar sua gestão no dia a dia.

Para rodar a aplicação:
- git clone
- python -m venv .venv (adiciona o ambiente virtual)
- pip install -r requirements.txt
- streamlit run Finance_up.py (rode no terminal)

Futuras melhorias:
- Adicionar o simulador de investimentos
- Melhorar o conversor cripto

Menu:
- Gestão de gastos/ganhos
    . Renda
    . Gastos essenciais
    . Gastos não-essenciais
    . Investimentos

- Simulador de investimentos
    . CDB
    . LCI
    . LCA
    . Tesouro direto
    . Tesouro IPCA+
    . Poupança
    . Ideias: valor inicial, mensal

- Conversor
    . Para cripto
    . Para moedas fiduciárias

- Informações úteis
    . Vizualização de gráfico e planilha !important
    . Gastos históricos


Organização de tarefas:
- Gabriel: interface
- Renan: conversor cripto
- Estrela: gráfico
- Alan: planilha
- Luiz Gustavo: simulador de investimento

Tarefas:
- gerar planilha
- gerar gráfico
- fazer a interface gráfica:
    . tela de login
    . menu
    . seção de gestão
    . seção de simulador de investimentos
    . seção de conversor
- fazer o conversor de cripto

Sugestão de bibliotecas:
- matplotlib
- pandas
- streamlit

Como seria na prática a gestão de ganhos/gastos:

Inserir despesas diárias: alimentação, transporte, entretenimento
Calcular total de gastos
Mostrar gráficos com informações úteis (médias diárias/mensais/anuais)
