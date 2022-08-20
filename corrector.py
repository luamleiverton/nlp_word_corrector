import nltk
nltk.download('punkt')
import string
from word_processing import *

with open("artigos.txt", "r") as f:
  artigos = f.read()

palavras_separadas = nltk.tokenize.word_tokenize(artigos)
lista_palavras = separa_palavras(palavras_separadas)
lista_normalizada = normalizacao(lista_palavras)
lista_sem_repeticao = set(lista_normalizada)
palavras_geradas = gerador_palavras('lgica')

corretor('lgica')

