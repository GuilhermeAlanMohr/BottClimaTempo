import re
from bott import newbot

#Cria um objeto da classe newbot
bott = newbot('roboClimaTempo')
#Chama o método climaTempo e envia um array com cidades como Strings
bott.capturaDadosClimaticos(["Porto Alegre","Rio de Janeiro","Belo Horizonte","São Paulo","Santa Maria","Salvador"])