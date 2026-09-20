import streamlit as st
import pandas as pd
from layout import render_page

#Importa os dados
df = pd.read_excel('dados/BASE_BUENOS_DRIVERS.xlsx', sheet_name='BASE_NUMERICA')

st.set_page_config(page_title="Painel", layout="wide")
render_page(df)