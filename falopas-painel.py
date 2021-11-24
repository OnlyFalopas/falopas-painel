#!/bin/python3
import os
try:
        from requests import get
except:
        os.system('pip install requests')
from webbrowser import open
import time
from sys import argv, executable

vd = '\033[0;36m'
cl = '\033[1;97m'

#josh passou aqui 😎👍
#dio colou aqui tbm

def op():
        open('https://chat.whatsapp.com/FhFvqBpRYCV6tsmaBSMclT')

def clear():
    os.system('cls||clear')
def ent():
    input('\nEnter para continuar')
    reiniciar()
def banner():
    os.system('cat banner | lolcat')
def reiniciar():
    os.execv(executable, ['python3'] + argv)

clear()
banner()
print('\n')
print ("=" * 40)
 #menu
print(f"""
{cl}❮ {vd}1{cl} ❯ CONSULTAR DDD
{cl}❮ {vd}2{cl} ❯ CONSULTAR CEP
{cl}❮ {vd}3{cl} ❯ CONSULTAR CPF
{cl}❮ {vd}4{cl} ❯ CONSULTAR IP
{cl}❮ {vd}5{cl} ❯ CONSULTAR TELEFONE
{cl}❮ {vd}6{cl} ❯ CONSULTAR NOME
{cl}❮ {vd}7{cl} ❯ CONSULTAR CNPJ
{cl}❮ {vd}8{cl} ❯ CONSULTAR COVID
{cl}❮ {vd}0{cl} ❯ CONSULTAR PLACA

{cl}❮ {vd}D{cl} ❯ DEV'S
{cl}❮ {vd}S{cl} ❯ SAIR...
   """ )
print ("=" * 40)
#####$
def ip():
        clear()
        ip=input(f"""\n╭┈ • DIGITE O IP (enter para consultar seu ip)
┆
╰┈ •• ❥ """)
        clear()
        print('')
        r = get(f'https://ipwhois.app/json/{ip}').json()
        clear()
        for i in r:
                if r[i] != '':
                        print(f'{vd}{i}{cl}: {r[i]}')
        print("\n© ® OnlyFalopa Dev's")
        ent()

def cep():
        clear()
        cep = int(input(f"""{cl}\n╭┈ • DIGITE O CEP (exemplo: 59112500)
┆
╰┈ •• ❥ """))
        clear()
        request = get(f'https://viacep.com.br/ws/{cep}/json/')
        data = request.json()
        for item in data:
                if data[item] != '':
                        print(f'{vd}{item}{cl}: {data[item]}')
        print("\n© ® OnlyFalopa Dev's")
        ent()

def cpf():
  clear()
  cpf = int(input(f""" {cl}\n╭┈ • DIGITE O CPF (exemplo:
  07068213868)
┆
╰┈ •• ❥ """))
  cpff = get(f"http://ghostcenter.xyz/api/cpf/{cpf}")
  mat = cpff.json()
  for item in mat: print(item,':',mat[item])

def tell():
        clear()
        print(f"{cl}CONSULTA TELEFONE APENAS PARA VERSÕES VIP'S")
        print("\n© ® OnlyFalopa Dev's")
        time.sleep(2)
        op()
        reiniciar()

def covid():
        clear()
        ata = input("""\n╭┈ • DIGITE O ESTADO (exemplo: sp)
┆
╰┈ •• ❥ """)
        clear()
        sp = get(f"https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/{ata}").json()
        for item in sp:
                if sp[item] != '':
                        print(f'{vd}{item}{cl}: {sp[item]}')
        print("\n© ® OnlyFalopa Dev's")
        ent()

def placa():
        clear()
        plc = input(""""\n╭┈ • DIGITE A PLACA (exemplo: mmp1345)
┆
╰┈ •• ❥ """).strip().upper()
        clear()
        r = get(f'https://apicarros.com/v1/consulta/{plc}/json', verify=False).json()
        print('='*40)
        a = 0
        for i in r:
                if a == 0:
                        clear()
                if r[i] != '':
                        print(f'{vd}{i}{cl}: {r[i]}')
                a += 1
        print("\n© ® OnlyFalopa Dev's")
        print('='*40)
        ent()

def cnpj():
        clear()
        cnpj = input("""\n╭┈ • DIGITE O CNPJ (exemplo: 45039237000114)
┆
╰┈ •• ❥ """)
        pj = get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj}/').json()
        clear()
        for i in pj:
                if pj[i] != '':
                        if type(pj[i]) == dict:
                                print(f'{vd}{i}{cl}⤵')
                                for c in pj[i]:
                                        print(f'{vd}{c}{cl}: {pj[i][c]}')
                        elif type(pj[i]) == list:
                                print(vd,i+'⤵')
                                for ite in pj[i]:
                                        for ij in ite:
                                                print(f'{vd}{ij}{cl}: {ite[ij]}')
                        elif type(pj[i]) == str or int or float or bool:
                                print(f'{vd}{i}{cl}: {pj[i]}')
        ent()

def devs():
        clear()
        print("""
╭┈┈┈┈┈┈┈•
┆ OnlyFalopas Dev's
┆
┆•• Spyware
┆•• MrDiniz
┆•• Swag Baby
┆•• Ghosthype
┆•• Josh washington
┆•• Dio Brando
┆
╰┈┈┈┈┈•
""")
        ent()

def ddd():
        clear()
        ddd = input("""\n╭┈ • DIGITE O DDD
┆
╰┈ •• ❥ """)
        clear()
        dd = get(f'https://brasilapi.com.br/api/ddd/v1/{ddd}').json()
        clear()
        for item in dd:
                if type(dd[item]) == list:
                        print(f'{vd}{item}{cl}:')
                        for i in dd[item]:
                                print(i)
                elif type(dd[item]) == str or int or float or bool:
                        print(f'{vd}{item}{cl}: {dd[item]}') #hi

        print("\n© ® OnlyFalopa Dev's")
        ent()
def nome():
    clear()
    nome = input("""╭┈ • DIGITE O NOME (OBS: Não utilize acentos...)
┆
╰┈ •• ❥ """ )
    cons = get(f"http://ghostcenter.xyz/api/nome/{nome}")
    elliot = cons.json()
    try:
    	result = elliot['dados']
    	for i in result:
    		print("\n© ® OnlyFalopa Dev's")
    		print(f"NOME = {i['nome']} ")
    		print(f"CPF = {i['cpf']} ")
    		print(f"NASCIMENTO = {i['nascimento']}")
    		print(f"SEXO = {i['sexo']} ")
    except:
    	print("Nada foi encontrado....")
    	ent()
    	
######
try:
        ope = input(f"{vd}Selecione uma opção {cl}==> ").strip().lower()[0]
except:
        reiniciar()
if ope == '1':
    ddd()
elif ope == '2':
    cep()
elif ope == '3':
    cpf()
elif ope == '4':
        ip()
elif ope == '5':
        tell()
elif ope == '6':
        nome()
elif ope == '7':
        cnpj()
elif ope == '8':
        covid()
elif ope == '0':
        placa()
elif ope == 'd':
        devs()
elif ope == 's':
        clear()
        print(f'{vd}Obrigado por usar o nosso painel :)\033[m')
else:
        reiniciar()
