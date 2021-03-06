import docker
import argparse
from datetime import datetime

def logando(mensagem, e, logfile='docker-cli.log'):
	data_atual = datetime.now().strtime('%d%m%Y %H:%M')
	with open('docker-cli.log', 'a') as log:
		texto = "%s \t %s \t %s \n" % (data_atual, mensagem, str(e))
		log.write(texto)

def criar_containers(args):
	try:
		client = docker.from_env()
		executando = client.containers.run(args.imagem, args.comando, detach=True)
		return(executando)
	except docker.errors.ImageNotFound as e:
		logando('Erro: Essa imagem nao existe!', e)
	except docker.errors.NotFound as e:
		logando('Erro: Esse comando não existe!', e)
	except Exception as e:
		logando('Erro: Favor verificar  comando executado', e)
	finally:
		print('Comando executado!')



#client = docker.from_env()
#client.containers.run("nginx", detach=True)
#client.containers.list()

def listar(args):
	"""Listando os container e suas respectivas imagens"""
	get_all = client.containers.list()
	for cada_container in get_all:
		conectando = client.containers.get(cada_container.id)
		print("O container %s utilza a imagem %s e ele esta rodando o comando %s" % (conectando.short_id, conectando.attrs['Config']['Image'], conectando.attrs['Config']['Cmd']))

parser = argparse.ArgumentParser(description="Meu CLI docker fodao feito durante a aula do HPD.")
subparser = parser.add_subparsers()

listar_opt = subparser.add_parser('listar')
listar_opt.set_defaults(func=listar)

criar_opt = subparser.add_parser('criar')
criar_opt.add_argument('--imagem', required=True)
criar_opt.add_argument('--comando', required=False)
criar_opt.set_defaults(func=criar_containers)


cmd = parser.parse_args()
cmd.func(cmd)

#container()
