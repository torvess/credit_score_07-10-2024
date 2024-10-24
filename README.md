### Data Science aplicado em finanças! 

### Notebooks 📓



### Dados 🎲

Os dados foram obtidos no [Kaggle](https://www.kaggle.com/datasets/rikdifos/credit-card-approval-prediction). Temos as seguintes tabelas: 

- [clientes_cadastrados.csv](https://github.com/alura-tech/alura-tech-pos-data-science-credit-scoring-streamlit/blob/main/dados/clientes_cadastrados.csv): contém informações pessoais dos clientes
- [clientes_aprovados.csv](https://github.com/alura-tech/alura-tech-pos-data-science-credit-scoring-streamlit/blob/main/dados/clientes_aprovados.csv): é o arquivo que contém todos os registros de pagamento/padrão de cada cliente.


### Objetivo 🎯
Construir um modelo de aprendizado de máquina para prever se um cliente é 'bom' ou 'mal' pagador, para saber se ele terá um cartão de crédito aprovado ou não. Após obter o melhor modelo, uma aplicação será criada no Streamlit! Bora criar uma aplicação?! 


### Desenvolvimento 

#### 1- Utilizei um notebook para leitura e análise exploratória dos dados, criei a variável target, treinei e testei modelos de classificação para avaliar qual o modelo com melhor desempenho.

#### 2- Criei um arquivo utils.py e defini a classe que serviu de Pipeline para o app no streamlit que serviu como deploy do modelo

#### 3- Desenvolvi um app online com Streamlit para que seja possível responder perguntas e avaliar se irá ou não receber limite.
