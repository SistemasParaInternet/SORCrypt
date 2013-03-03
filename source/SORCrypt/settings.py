#coding: utf-8

"""
Modulo responsavel pelas configuracoes globais do software.
"""

# Host (Ip do Servidor), PORTA (Porta do Servidor), LISTEN (maquinas)
HOST_NOMES = '127.0.0.1'
HOST_FUNCOES = '127.0.0.1'
PORTA_NOMES = 4353
PORTA_FUNCOES = 3355
LISTEN = 5

# Tipos de Requisicoes do Cliente. Nao alterar.
SOMA = 'SOMA'
PRODUTO = 'PROD'
DIVISAO = 'DIVI'
FATORIAL = 'FATO'
PORCENTAGEM = 'PORC'
FUNCOES = 'FUNC'

# Tamanho das Mensagens de requisicao.
TAM_MSG = 6

SERVIDORES = '../arquivo/nomes.txt'
