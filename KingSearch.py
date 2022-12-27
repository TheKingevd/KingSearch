#!/usr/bin/python3

#BEM VINDO AO MENU DE LOGIN FEITO NA MERDA

#import
import os
import time

#cores
R = "\033[1;31m"
B = "\033[1;34m"
C = "\033[1;36m"
G = "\033[1;32m"
W = "\033[1;39m"
Y = "\033[1;33m"

#LOGIN
#instalação da db de consulta dados
def login():
    print(f"{W}[{Y}{W}]FAÇA SEU LOGIN!")
    usuario = input("INFORME O USUARIO: ")
    senha = input("INFORME SUA SENHA: ")
    print(f"{R}SENHA INVALIDA!")
    if senha == 'Dex14':
        os.system('clear')
        time.sleep(1)
        print(f"{G}Você Foi Autenticado Com Sucesso! Você Sera Redirecionado Ao Painel Em Segundos...")
        time.sleep(1)
        os.system("python3 main.py")
        os.system("python main.py")
login()
