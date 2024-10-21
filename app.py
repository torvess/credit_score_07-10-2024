#Importação das bibliotecas
import streamlit as st
import pandas as pd
# import numpy as np
from sklearn.model_selection import train_test_split
from utils import DropFeatures, OneHotEncodingNames, OrdinalFeature, MinMaxWithFeatNames
from sklearn.pipeline import Pipeline
import joblib
from joblib import load

#carregando os dados
dados = pd.read_csv(r'https://raw.githubusercontent.com/torvess/credit_score_07-10-2024/refs/heads/main/dados/df_clean.csv')

############################# Streamlit ############################
st.markdown('<style>div[role="listbox"] ul{background-color: #6e42ad}; </style>', unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; '> Formulário para Solicitação de Cartão de Crédito 🤑</h1>", unsafe_allow_html = True)

st.warning('Preencha o formulário com todos os seus dados pessoais e clique no botão **ENVIAR** no final da página.')

# Idade
st.write('### Idade')
input_idade = float(st.slider('Selecione sua idade', 18, 100))

# Grau de escolaridade
st.write('### Nível de escolaridade')
input_grau_esc = st.selectbox('Qual é o seu grau de escolaridade?', sorted(dados['Grau_escolaridade'].unique()))

# Estado civil
st.write('### Estado civil')
input_est_civil = st.selectbox('Qual é seu estado civil?', sorted(dados['Estado_civil'].unique()))

# Número de membros da família
st.write('### Tamanho da família')
input_membros_familia = float(st.slider('Selecione quantos membros tem na sua familia', 1, 20))

# perguntas com resposta binária vou criar um dicionario para usar em todas as perguntas
dict_input_bin = {'Sim':1, 'Não':0}

# Carro próprio
st.write('### Carro próprio')
input_carro_proprio = st.radio('Você possui um automóvel?', ['Sim', 'Não'])
input_carro_proprio = dict_input_bin.get(input_carro_proprio)

# Casa própria
st.write('### Casa própria')
input_casa_propria = st.radio('Você possui uma casa?', ['Sim', 'Não'])
input_casa_propria = dict_input_bin.get(input_casa_propria)


# Moradia
st.write('### Tipo de residência')
input_tipo_moradia = st.selectbox('Qual é o seu tipo de moradia?', sorted(dados['Moradia'].unique()))

# Situação de emprego
st.write('### Categoria de renda')
input_categoria_renda = st.selectbox('Qual é a sua categoria de renda?', sorted(dados['Categoria_de_renda'].unique()))

# Ocupação
st.write('### Ocupação')
input_ocupacao = st.selectbox('Qual é a sua ocupação?', sorted(dados['Ocupacao'].unique()))

# Tempo de experiência
st.write('### Experiência')
input_tempo_experiencia = float(st.slider('Qual é o seu tempo de experiência?', 0, 30))

# Rendimentos
st.write('### Rendimentos')
input_rendimentos = float(st.number_input('Digite o seu rendimento anual (em reais) e pressione "ENTER" para confirmar', 0, ))

# Telefone trabalho
st.write('### Telefone corporativo')
input_telefone_trabalho = st.radio('Você possui um telefone corporativo?', ['Sim', 'Não'])
input_telefone_trabalho = dict_input_bin.get(input_telefone_trabalho)

# Telefone fixo
st.write('### Telefone Fixo')
input_telefone = st.radio('Você possui um telefone', ['Sim', 'Não'])
input_telefone = dict_input_bin.get(input_telefone)

# Email 
st.write('### E-mail')
input_email = st.radio('### Você possui um e-mail?', ['Sim', 'Não'])
input_email = dict_input_bin.get(input_email)

# Lista de todas as variáveis:
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

# Separando os dados em treino e teste
def data_split(df, test_size):
    SEED=1561651
    treino_df, teste_df = train_test_split(df, test_size=test_size, random_state=SEED)
    return treino_df.reset_index(drop=True), teste_df.reset_index(drop=True)

treino_df, teste_df = data_split(dados, 0.2)

#Criando novo cliente
cliente_predict_df = pd.DataFrame([novo_cliente], columns=teste_df.columns)

#Concatenando novo cliente ao dataframe dos dados de teste
teste_novo_cliente = pd.concat([teste_df, cliente_predict_df], ignore_index=True)

#Pipeline
def pipeline_teste(df):

    pipeline = Pipeline([
        ('feature_dropper', DropFeatures()),
        ('OneHotEncoding', OneHotEncodingNames()),
        ('ordinal_feature', OrdinalFeature()),
        ('min_max_scaler', MinMaxWithFeatNames()),
    ])
    df_pipeline = pipeline.fit_transform(df)
    return df_pipeline

#Aplicando a pipeline
teste_novo_cliente = pipeline_teste(teste_novo_cliente)

#retirando a coluna target
cliente_pred = teste_novo_cliente.drop(['Mau'], axis=1)

#Predições 
if st.button('Enviar'):
    model = joblib.load('modelo/xgb.joblib')
    final_pred = model.predict(cliente_pred)
    if final_pred[-1] == 0:
        st.success('### Parabéns! Você teve o cartão de crédito aprovado')
        st.balloons()
    else:
        st.error('### Infelizmente, não podemos liberar crédito para você agora!')

