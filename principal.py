import time
import random
import math
import sys

pessoas = [ ('Lisbon', 'LIS'),
            ('Madrid', 'MAD'),
            ('Paris', 'CDG'),
            ('Dublin', 'DUB'),
            ('Brussels', 'BRU'),
            ('London', 'LHR')]

pessoas[3] # tupla

('Dublin', 'DUB')

destino = 'FCO' #Roma

voos = {('BRU', 'FCO'): ['15:44', '18:55', 382]}

voos
    {('BRU', 'FCO') : ['15:44', '18:55', 382]}

voos [('BRU', 'FCO')]
    ('15:44', '18:55', 382)

voos ={}
for linha in open('/content/flights.txt'):
    print (linha)
    print (linha.split(','))
    origem, destino, partida, chegada, preco = linha.split(',')
    print(origem, destino, partida, chegada, preco)
