#OBJETOS É BASICAMENTO O VALOR ARMAZENADO PELA VARIAVEL 

# 'idade' aponta para um objeto inteiro
idade = 25

# O objeto int responde a métodos:
print(idade.bit_length()) # Quantos bits são necessários para representar 25 (5 bits)
print(type(idade))        # Retorna a classe: <class 'int'>

# 'numeros' é a variável, [1, 2, 3] é o objeto
numeros = [1, 2, 3]

# Métodos que o objeto lista responde:
numeros.append(4)      # Adiciona um elemento: [1, 2, 3, 4]
numeros.reverse()      # Inverte a ordem: [4, 3, 2, 1]
print(numeros)


# 'mensagem' é a variável, "Olá Python" é o objeto
mensagem = "Olá Python"

# Métodos que o objeto string responde:
print(mensagem.upper())      # Converte para maiúsculas: 'OLÁ PYTHON'
print(mensagem.split(' '))   # Divide em uma lista: ['Olá', 'Python']
print(len(mensagem))         # Função que retorna o tamanho (10)

texto = "Explorando"
print(dir(texto)) # Mostra uma lista de tudo que uma string pode fazer (upper, lower, split, etc.)