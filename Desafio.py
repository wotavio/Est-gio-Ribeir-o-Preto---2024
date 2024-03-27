# 1)
n = 13
soma = 0
k = 0

while k < n:
    k += 1
    soma = soma + k

print(soma)

# O resultado final da soma será 91!


# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
num = int(input("Digite um número para verificar se está na sequência de Fibonacci: "))

a, b = 0, 1
while b < num:
    a, b = b, a + b

if b == num:
    print(f"{num} está na sequência de Fibonacci!")
else:
    print(f"{num} não está na sequência de Fibonacci.")

# 3) Descubra a lógica e complete o próximo elemento:



# a) 1, 3, 5, 7, (9)

# b) 2, 4, 8, 16, 32, 64, (128)

# c) 0, 1, 4, 9, 16, 25, 36, (49)

# d) 4, 16, 36, 64, (100)

# e) 1, 1, 2, 3, 5, 8, (13)

# f) 2,10, 12, 16, 17, 18, 19, (20)
    

# 4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.
# Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?
    
    # Resposta: Eu deixaria somente um dos três interruptores ligados e iria até a sala para verificar qual lâmpada está acesa. Depois desligaria o interruptor que estava ligado e ligaria o próximo na sequência. Então, voltaria até a sala das lâmpadas para verificar qual lâmpada está acesa com o novo interruptor ligado. Agora, só me restaria um interruptor, que deve controlar a última lâmpada!

# 5)
string = input("Digite aqui irmão: ")
caracteres = list(string)
inicio = 0
fim = len(caracteres) - 1

while inicio < fim:
    caracteres[inicio], caracteres[fim] = caracteres[fim], caracteres[inicio]
    inicio += 1
    fim -= 1

string_invertida = ''.join(caracteres)

print("String Original:", string)
print("String Invertida:", string_invertida)