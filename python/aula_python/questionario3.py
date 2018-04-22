#!/usr/bin/env python
print('Qual o seu nome?')
nome = input()
print('Qual a sua idade?')
idade = input()
print('Seja muito bem-vindo ao treinamento, %s' % nome) # INTERPOLANDO
print('Ja esta ficando velhor hein, ' + str(idade) + ' anos ja esta no final da vida!') # CONCATENANDO
print('Qual o seu sexo, %s?' % nome)
sexo = input()
print('Fiquei surpreso %s, nao me parece do sexo %s' % (nome, sexo)) # PYTHON 3.5
#print(f"Fiquei surpreso {nome}, nao me parece do sexo {sexo}") # PYTHON 3.6 pra cima
print("apenas testando as variaveis do nome {} e do sexo {}".format(nome, sexo))
print("apenas testando as variaveis do nome {nome} e do sexo {sexo}".format(nome="Godofredo", sexo="Alienigena"))
valor = 10
print("O valor do pao eh: %.2f " % valor) 
