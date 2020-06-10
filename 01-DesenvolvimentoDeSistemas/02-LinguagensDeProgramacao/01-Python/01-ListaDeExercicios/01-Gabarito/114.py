print("""
114) Crie um código em Python que teste se o site pudim está acessível pelo
computador usado.
""")

import urllib.request

site = 'http://www.pudim.com.br'

try:
    urllib.request.urlopen(site)
except urllib.error.URLError:
    print('Em todos esses anos nesta Indústria Vital, essa é a primeira \
vez que isso me acontece. -Smedley')
else:
    print('Funcionou!')
