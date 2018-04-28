#!/usr/bin/env python3
def pause():
	input("\n\nPressione enter para continuar...\n\n")

def mensagemFim():
	print("Valeu por usar o programa!")
	print("VAAIIIIIII!")

def imprimeTresLinhas():
	for i in range(1,4):
		print('esta e a linha ' + str(i))

def impreNoveLinhas():
	for i in range(1,4):
		imprimeTresLinhas()

def mensagemInicio():
	print("Este programa eh somente para mostrar como funciona o uso de functions")
	pause()

def linhaBranco():
	print()

def limpaTela():
	for i in range(1,26):
		linhaBranco()


mensagemInicio()
mensagemFim()
impreNoveLinhas()
#limpaTela()
#linhaBranco()

