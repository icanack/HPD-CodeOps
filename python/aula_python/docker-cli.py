import docker
import argparse

client = docker.from_env()
client.containers.run("nginx", detach=True)
client.containers.list()

def container():
	"""Listando os container e suas respectivas imagens"""
	get_all = client.containers.list()
	for cada_container in get_all:
		conectando = client.containers.get(cada_container.id)
		print("O container %s utilza a imagem %s e ele esta rodando o comando %s" % (conectando.short_id, conectando.attrs['Config']['Image'], conectando.attrs['Config']['Cmd']))

parser = argparse.ArgumentParser(description="Meu CLI docker fodao feito durante a aula do HPD.")
subparser = parser.add_subparsers()

listar_opt = subparser.add_parser('listar')
listar_opt.set_defaults(func=listar)

cmd = parser.parse.args()

cmd.func(cmd)

#container()
