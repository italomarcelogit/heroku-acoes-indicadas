import yfinance as yf
import streamlit as st
import pandas as pd
from datetime import date, datetime, timedelta

st.set_page_config(layout="wide", page_title="Ações Indicadas")
st.write("""
# Ações indicadas para julho 2021
As ações preferidas dos analistas para comprar em julho ***(por infoMoney - Bruna Furlani)***! """)
tickerSymbol = st.radio('Ticker', ['VALE3', 'B3SA3', 'BBDC4', 'RDOR3', 'BPAC11'])
tickerSymbol = f"{tickerSymbol}.SA"
hoje = datetime.today()
antes30 = hoje - timedelta(30)
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d',
                              start=antes30.strftime("%Y-%m-%d"),
                              end=hoje.strftime("%Y-%m-%d"))
c1, c2 = st.beta_columns(2)
with c1:
    st.write(f"** Valor (close): {tickerSymbol} **")
    st.line_chart(tickerDf.Close)
with c2:
    st.write(f"** Volume: {tickerSymbol} **")
    st.line_chart(tickerDf.Volume)
st.write('https://www.infomoney.com.br/onde-investir/as-acoes-preferidas-dos-analistas-para-comprar-em-julho/')