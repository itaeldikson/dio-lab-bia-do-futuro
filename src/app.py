import json
import pandas as pd
import requests
import streamlit as st

# =========== Configuração ===========

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss"


# =========== CARREGAR DADOS ===========

perfil = json.load(open('./data/perfil_investidor.json'))
transacoes = pd.read_csv('./data/transacoes.csv')
historico = pd.read_csv('./data/historico_atendimento.csv')
produtos = json.load(open('./data/produtos_financeiros.json'))

# =========== MONTAR CONTEXTO ===========

contexto = f"""

CLIENTE: {perfil['nome']}, {perfil['idade']} anos, perfil {perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMONIO: R$ {perfil['patrimonio_total']} | RESERVA: R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTO ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONIVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}

"""

# =========== SYSTEM PROMPT ===========

SYSTEM_PROMPT = """ Você é ITA um agente financeiro inteligente especializado em Financas .

OBJETIVO:
Ensinar conceitos de Financas pessoais de forma simples, usando os dados do cliente como exemplo praticos.

REGRAS:
1. NUNCA recomende investimentos especificos - apenas explique como fuciona;
2. Use os dados fornecidos para dar exemplos personalizados.
3. Linguagem simples, como se explicasse para um amigo;
4. se não souber algo, admita: "nao tenho essa informação, mas posso explicar...";
5. Sempre pergunte se o cliente entendeu;
6. responda com resposta sucinta e direta.
"""

# =========== CHAMAR OLLAMA ===========

def perguntar (msg):
    prompt =f"""
    {SYSTEM_PROMPT}
    
    CONTEXTO DO CLIENTE:
    {contexto}
    
    Pergunta: {msg}"""
    
    r = requests.post(OLLAMA_URL, json={"model": MODELO, "prompt": prompt, "stream": False})
    return r.json()['response']


# =========== Interface ===========

st.title(" 💰 Ita, Seu gestor financeiro!")

if pergunta := st.chat_input("sua duvida sobre finanças..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(perguntar(pergunta)) 

