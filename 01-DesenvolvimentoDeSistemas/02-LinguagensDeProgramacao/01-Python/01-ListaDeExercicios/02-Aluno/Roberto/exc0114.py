print("""
114) Crie um código em Python que teste se o site pudim está acessível pelo computador usado.
""")
import urllib 
import urllib.request

try:
    site = urllib.request.urlopen('http://www.robertomendonca.com.br')
except urllib.error.URLError:
    print('O site robertomendonca não está acessível no momento')
else:
    print('Consegui acessar o site robertomendonca com sucesso!')
    