#!/usr/bin/python3
#KingSearch Consultas, Script De Consultas Feita em Python

#cores
R = "\033[1;31m"
B = "\033[1;34m"
C = "\033[1;36m"
G = "\033[1;32m"
W = "\033[1;39m"
Y = "\033[1;33m"


def desenho():
    print('''────────────────████
───────────────█░░███
───────────────█░░████
────────────────███▒██─────████████
──────████████─────█▒█──████▒▒▒▒▒▒████
────███▒▒▒▒▒▒████████████░░████▒▒▒▒▒███
──██▒▒▒▒░▒▒████░░██░░░░██░░░░░█▒▒▒▒▒▒▒███
─██▒▒░░░░▒██░░░░░█▒░░░░░██▒░░░░░░░▒▒▒▒▒▒█
██▒░░░░░▒░░░░░░░░░▒░░░░░░░▒▒░░░░░░░▒▒▒▒▒██
█░░░░░░▒░░░██░░░░░░░░░░░░░██░░░░░░░░▒▒▒▒▒█
█░░░░░░░░█▒▒███░░░░░░░░░█▒▒███░░░░░░░▒▒▒▒█
█░░░░░░░████████░░░░░░░████████░░░░░░▒▒▒▒█
█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒█
██░░░█░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█░▒▒▒▒█
─█░░░░██░█░░░░░░░░░░░░░░░░░░░░░░░███▒▒▒▒▒█
─█▒▒░░░░█████░░░█░░░░██░░░██░░████░▒▒▒▒▒▒█
─██▒▒░░░░░█████████████████████░░░▒▒▒▒▒▒██
──██▒▒▒▒░░░░░██░░░███░░░██░░░█░░░▒▒▒▒▒▒██
───███▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒█████
─────███▒▒▒▒▒▒░░░░░░░░░░░░░▒▒▒▒▒▒████
────────██████████████████████████''')
#print(f"{R}oi")


#importação
import os 
import time

#Menu
print(f"{G}")
desenho()
print("")
print(f"{G}================================================{G}")
print(f"{W}Bem Vindo Ao Menu Da KingSearch, Escolha Uma Das Opções Abaixo")
print(f"{G}01 - {W} CONSULTA CPF {G}[ON]")
print(f"{G}02 - {W} CONSULTA NOME {G}[ON]")
print(f"{G}03 - {W} CONSULTA TELEFONE {G}[ON]")
print(f"{G}04 - {W} CONSULTA EMAIL {R}[OFF]")
print(f"{G}99 - {G} TELEGRAM DO DONO")
print(f"{G}================================================{G}")
next = input(f"{W} >> ")
if next == '01':
    print("BEM VINDO A DB DE CONSULTA CPF")
    cpf = input("INFORME O CPF : ")
    print('''CONSULTA REALIZADA COM SUCESSO!
    NOME: JEYSICA PALOMA MEDEIROS DOS SANTOS
    CPF : 07616427499
    SEXO : F - FEMININO
    MAE : LUCINEIDE MEDEIROS DOS SANTOS
    PAI : NADA ENCONTRADO
    ESTADO CIVIL : SOLTEIRA
    OBITO : NAO
    ESTADO : PB
    MUNICIPIO : JOAO PESSOA
    BAIRRO : ROGER
    CEP : 58020200
    NUMERO : 26
    TELEFONES:
    (83)982072076
    (83)984345267''')
    print("")
    input("Deseja Realizar outra consulta? [y/n]")
if next == '02':
    print("BEM VINDO A DB DE CONSULTA NOME")
    input("INFORME O NOME COMPLETO: ")
if next == '03':
    print("BEM VINDO A DB DE CONSULTA VIA TELEFONE")
    input("INFORME NUMERO : ")
if next == '04':
    print(f"{R}CONSULTA eMAIL OFF")


