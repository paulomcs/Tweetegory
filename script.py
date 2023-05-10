# Importação das Bibliotecas Necessarias
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import nltk
import spacy
import string
import re

# Downloads necessários
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords


pln = spacy.load("pt_core_news_sm")

# Leitura do arquivos com tweets já processados
with open("tweets_Todos_processados.txt", 'r', encoding='unicode_escape') as base_original:
    tweets_Todos_processados = base_original.readlines()


# StopWords da Biblioteca Spacy
stop_words_spacy = spacy.lang.pt.stop_words.STOP_WORDS

# StopWords da Biblioteca 
stop_words_nltk = stopwords.words('portuguese')

# Lista com todos os caracteres que foram julgados indesejaveis
caracteres_indesejaveis = ['—', 'de o', 'de a', 'a o', 'em o', 'em a', 'rt', '“', '”', '‘', '’', 'em', '):', 'R$']

# simulando o tweet inserido pelo usuário
tweet_usuario = "@joao_omotinha: Real Madrid x Machester City vai ser um belo jogo #champions"

# Funcao que ira processar o tweet do usuario
# Atenção: muito a melhorar, mas ja ajudou bastante
def processamento_texto(texto):
  # Letra minúscula
  texto = texto.lower()
  # Remove menções (@)
  #texto = re.sub(r'@\S+', '', texto)              
  texto = re.sub(r"@[A-Za-z0-9$-_.&+]+", ' ', texto)
  # Remove links
  #texto = re.sub(r'http\S+', '', texto)
  texto = re.sub(r"https?://[A-Za-z0-9./-]+", " ", texto)
  # Remove hastags
  texto = re.sub(r'#\S+', '', texto)
  # Remove Emojis
  emoji_pattern = re.compile("["u"\U0001F600-\U0001F64F"u"\U0001F300-\U0001F5FF"u"\U0001F680-\U0001F6FF"u"\U0001F1E0-\U0001F1FF"u"\U00002702-\U000027B0"u"\U000024C2-\U0001F251""]+", flags=re.UNICODE)
  texto = emoji_pattern.sub(r'', texto)
  # Numerais Ordinais
  regex_numerais_ordinais = re.compile(r'\b\d+(?:º|ª)\b')
  texto = regex_numerais_ordinais.sub('', texto)
  # Números com vírgula
  textp = re.sub(r'\b\d+,\d+\b', ' ', texto)
  # Espaços em Branco
  texto = re.sub(r" +", ' ', texto)
  # RT
  texto = texto.replace("rt ", " ")

  #Lematização
  documento = pln(texto)
  lista = []
  for token in documento:
    lista.append(token.lemma_)
  
  # StopWords e Pontuações
  lista = [palavra for palavra in lista if palavra not in stop_words_spacy and palavra not in stop_words_nltk and palavra not in string.punctuation and palavra not in caracteres_indesejaveis]

  # Transforma em String removendo dígitos numéricos
  lista = ' '.join([str(elemento) for elemento in lista if not elemento.isdigit()])

  return lista

# tweet do usuario processado
tweet_usuario_processado = processamento_texto(tweet_usuario)

# concatena base anterior com tweet do usuário
tweets_Todos_processados.append(tweet_usuario_processado)


# Construicao da representacao TF-IDF
vetor_palavras = TfidfVectorizer()
palavras_vetorizadas = vetor_palavras.fit_transform(tweets_Todos_processados)

# Realizacao do agrupamento
kmeans_tweets = KMeans(n_clusters=5, n_init=15)
kmeans_tweets.fit(palavras_vetorizadas)

# Lista com os rotulos (grupos) dos tweets
rotulos = kmeans_tweets.labels_

# Pega o rotulo do tweets do usuario
rotulo_usuario = rotulos[-1]

# Criacao de um dataframe de 2 colunas (Tweets,Rotulos)
dataframe = pd.DataFrame({'Tweets': tweets_Todos_processados, 'Cluster': rotulos})

# Lista com os tweets que foram agrupados no mesmo cluster que o tweet do usuario
tweets_agrupados = dataframe.loc[dataframe['Cluster'] == rotulo_usuario]['Tweets'].tolist()

# Imprime o cluster do usuario
print(rotulo_usuario)

# Imprime os tweets que fazem parte do cluster do usuario
print(tweets_agrupados)