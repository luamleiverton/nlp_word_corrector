import string
import nltk

def separa_palavras(lista_tokens):
  '''split tokens in words removing special characters'''
  lista_palavras=[]
  for token in lista_tokens:
    if token.isalpha():
      lista_palavras.append(token)
  return lista_palavras

def normalizacao(lista_palavras):
  '''normalyzing words to lowercase'''
  lista_normalizada=[]
  for palavra in lista_palavras:
    lista_normalizada.append(palavra.lower())
  return lista_normalizada

def insere_letras(fatias):
  '''insert additional chars in each word'''
  novas_palavras = []
  letras = list(string.ascii_lowercase)
  caracteres = ['á','â','ã','é','ê','í','ó','ô','õ','ú','ç']
  for caracter in caracteres:
    letras.append(caracter)
  for E, D in fatias:
    for letra in letras:
      novas_palavras.append(E + letra + D)
  return novas_palavras

def gerador_palavras(palavra):
  '''generate words to complete missing chars '''
  fatias = []
  for i in range(len(palavra)+1):
    fatias.append((palavra[:i], palavra[i:]))
  palavras_geradas = insere_letras(fatias)
  return palavras_geradas

def probabilidade(palavras_geradas, lista_normalizada):
  '''calculate probability of correct word'''
  frequencia = nltk.FreqDist(lista_normalizada)
  total_palavras = len(lista_normalizada)
  return frequencia[palavras_geradas]/total_palavras

def corretor(palavra):
  '''select word with higher probability about token list'''
  palavras_geradas = gerador_palavras(palavra)
  palavra_correta = max(palavras_geradas, key=probabilidade)
  return palavra_correta

