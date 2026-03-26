#OBJETOS É BASICAMENTO O VALOR ARMAZENADO PELA VARIAVEL 

idade = 25

# O objeto int responde a métodos:
print(idade.bit_length()) # Quantos bits são necessários para representar 25 (5 bits)
print(type(idade))        # Retorna a classe: <class 'int'>
numeros = [1, 2, 3]


# 'mensagem' é a variável, "Olá Python" é o objeto
mensagem = "Olá Python"
print(mensagem.upper())     
print(mensagem.split(' '))   
print(len(mensagem))        
texto = "Explorando"
print(dir(texto)) # Mostra uma lista de tudo que uma string pode fazer (upper, lower, split, etc.)