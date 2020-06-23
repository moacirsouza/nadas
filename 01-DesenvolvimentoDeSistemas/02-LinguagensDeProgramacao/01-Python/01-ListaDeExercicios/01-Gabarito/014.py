print("""
014) Escreva um programa que converta uma temperatura digitada em °C
e converta para °F. 
""")

celsius = float(input('Digite a temperatura em Celsius (°C) para \
convertê-la em Fahrenheit (°F): '))

fahrenheit = ((9*celsius)/5)+32 # Muitos parêntesis?

print('{}°C equivalem a {}°F'.format(celsius,fahrenheit))
