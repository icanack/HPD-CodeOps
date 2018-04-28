#!/usr/bin/env python3
import argparse
import subprocess

def criar(args):
	"""Cria o diretorio desejado"""
	diretorio = args.nome
	print(diretorio)
	subprocess.call(['mkdir', args.nome])
	for i in range(1,40):
	  subprocess.call(['touch', str(i)], cwd=args.nome)

def listar(args):
	"""Lista o diretorio desejado"""
	subprocess.call(['ls', args.nome])


#def desligar(args):
#	subprocess.call(['reboot', args.nome])

def list_interface(args):
	"""Lista a interface desejada"""
	subprocess.call(['ifconfig', args.interface])



parser = argparse.ArgumentParser(description="Comando para criar e listar diretorios durante a aula.")

subparser = parser.add_subparsers()

criar_dir = subparser.add_parser('criar')
criar_dir.add_argument('--nome', required=True)
criar_dir.set_defaults(func=criar)

listar_dir = subparser.add_parser('listar')
listar_dir.add_argument('--nome', required=True)
listar_dir.set_defaults(func=listar)

listar_interface = subparser.add_parser('network')
listar_interface.add_argument('--interface', required=True)
listar_interface.set_defaults(func=list_interface)


cmd = parser.parse_args()
cmd.func(cmd)



