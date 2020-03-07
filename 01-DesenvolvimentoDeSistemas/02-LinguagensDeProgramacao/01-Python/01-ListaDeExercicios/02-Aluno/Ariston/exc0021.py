print("""
\033[1;37;44m 021) \033[m Crie um programa em PYTHON que: Faça um programa em Python que abra e reproduza o Áudio de um arquivo MP3.
""")

musica = "d:\\Users\\Ariston\\Music\\Beam_Me_Up.mp3"

import playsound
print('Para sair da reprodução, pressione CTRL+C')
playsound.playsound(musica)