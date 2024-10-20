import streamlit as st
import pandas as pd
import numpy as np

dados = pd.read_csv(r'https://raw.githubusercontent.com/torvess/credit_score_07-10-2024/refs/heads/main/dados/df_clean.csv')

st.write('## Simulador de avaliação de crédito')

st.write('### Idade')
input_idade = float(st.slider('Selecione sua idade', 18, 100))

st.write('### Nível de escolaridade')
input_grau_esc = st.selectbox('Qual é o seu grau de escolaridade?', sorted(dados['Grau_escolaridade'].unique()))

st.write('### Estado civil')
input_est_civil = st.selectbox('Qual é seu estado civil?', sorted(dados['Estado_civil'].unique()))

st.write('### Tamanho da família')
input_membros_familia = float(st.slider('Selecione quantos membros tem na sua familia', 1, 20))

# perguntas com resposta binária vou criar um dicionario para usar em todas as perguntas
dict_input_bin = {'Sim':1, 'Não':0}

st.write('### Carro próprio')
input_carro_proprio = st.radio('Você possui um automóvel?', ['Sim', 'Não'])
input_carro_proprio = dict_input_bin.get(input_carro_proprio)

st.write('### Casa própria')
input_casa_propria = st.radio('Você possui uma casa?', ['Sim', 'Não'])
input_casa_propria = dict_input_bin.get(input_casa_propria)

st.write('### Tipo de residência')
input_tipo_moradia = st.selectbox('Qual é o seu tipo de moradia?', sorted(dados['Moradia'].unique()))

st.write('### Categoria de renda')
input_categoria_renda = st.selectbox('Qual é a sua categoria de renda?', sorted(dados['Categoria_de_renda'].unique()))

st.write('### Ocupação')
input_ocupacao = st.selectbox('Qual é a sua ocupação?', sorted(dados['Ocupacao'].unique()))

st.write('### Experiência')
input_tempo_experiencia = float(st.slider('Qual é o seu tempo de experiência?', 0, 30))

st.write('### Rendimentos')
input_rendimentos = float(st.number_input('Digite o seu rendimento anual (em reais) e pressione "ENTER" para confirmar', 0, ))

st.write('### Telefone corporativo')
input_telefone_trabalho = st.radio('Você possui um telefone corporativo?', ['Sim', 'Não'])
input_telefone_trabalho = dict_input_bin.get(input_telefone_trabalho)

st.write('### Telefone Fixo')
input_telefone = st.radio('Você possui um telefone', ['Sim', 'Não'])
input_telefone = dict_input_bin.get(input_telefone)

st.write('### E-mail')
input_email = st.radio('### Você possui um e-mail?', ['Sim', 'Não'])
input_email = dict_input_bin.get(input_email)

novo_cliente = [0,
                input_carro_proprio,
                input_casa_propria,
                input_telefone_trabalho,
                input_telefone,
                input_email,
                input_membros_familia,
                input_rendimentos,
                input_idade,
                input_tempo_experiencia,
                input_categoria_renda,
                input_grau_esc,
                input_est_civil,
                input_tipo_moradia,
                input_ocupacao,
                0
                ]