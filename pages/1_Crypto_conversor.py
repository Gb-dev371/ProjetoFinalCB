import streamlit as st
from binance.client import Client

def get_crypto_price(crypto, currency):
    api_key = "sua_chave_de_api"
    api_secret = "sua_chave_secreta"
    client = Client(api_key, api_secret)

    symbol = f"{crypto}{currency}"
    ticker = client.get_ticker(symbol=symbol)

    if "lastPrice" in ticker:
        price = float(ticker["lastPrice"])
        return price
    else:
        return None

def main():
    st.title("Calculadora de Criptomoedas")

    crypto = st.selectbox("Selecione a Criptomoeda", ("BTC", "ETH", "LTC"))
    currency = st.radio("Selecione a Moeda", ("BRL", "USDT"))
    amount = st.number_input("Digite a Quantidade em Moeda Normal")

    if st.button("Calcular"):
        price = get_crypto_price(crypto, currency)

        if price is not None:
            total_crypto = amount / price

            st.write(f"O equivalente de {amount} {currency} em {crypto} é: {total_crypto} {crypto}")
        else:
            st.write("Erro ao obter a cotação da criptomoeda. Por favor, tente novamente mais tarde.")

if __name__ == "__main__":
    main()