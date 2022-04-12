#--------------------------------
magen = '\033[1;95m '
verm = '\033[1;31m'
verd = '\033[1;32m'
vd = '\033[0;36m'
cl = '\033[1;97m'
amal = '\033[1;96m '


from os import system, name, execl
from sys import executable, argv, stdout
from time import strftime, sleep
from getpass import getuser



class basic():
    def op():
        try:
            open('https://chat.whatsapp.com/FhFvqBpRYCV6tsmaBSMclT')
        except:
            basic.cls()
            print(f'{verm}Navegador nao encontrado. Entre no grupo por conta propria.\nhttps://chat.whatsapp.com/FhFvqBpRYCV6tsmaBSMclT')
            basic.ent()

    def cls():
        system("cls||clear")

    def reset():
        stdout.flush()
        execl(executable, 'python', __file__, * argv[1:])

    def ent():
        input(f'{verd}\nEnter para continuar... ')
        basic.reset()


class info():
    def hours():
        year, month, day, hour, min = map(int, strftime("%Y %m %d %H %M").split())
        return f'[{hour}:{min}]'

    def ins():
        print(info.hours())

    def user():
        us = getuser()
        return us



class prints():
    def ban():
        print(f'''{magen}
   __      _
  / _|    | |
 | |_ __ _| | ___  _ __   __ _ ___
 |  _/ _` | |/ _ \| '_ \ / _` / __|
 | || (_| | | (_) | |_) | (_| \__ \\
 |_| \__,_|_|\___/| .__/ \__,_|___/
                  | |
                  |_|
        ''')

    def util():
        print(f'''{amal}
{verd}1{amal} - Consulta CPF
{verd}2{amal} - Consulta NOME
{verd}3{amal} - Consulta CNPJ
{verd}4{amal} - Consulta CEP
{verd}5{amal} - Consulta PLACA
{verd}6{amal} - Consulta Covid
{verd}7{amal} - Devs
{verd}8{amal} - Grupo Whatsapp
{verd}9{amal} - Sair{magen}
              ''')

# Instalação de libs.

try:
    from webbrowser import open
except:
    if(name=="posix"):
        system("pacman -S python-pip")
        system("pip install webbrowser")
        basic.cls()
        print(info.hours(),'Instalado webbrowser.')
        sleep(3)
        basic.cls()

    else:
        system("pip install webbrowser")
        basic.cls()
        print(info.hours(),'Instalado webbrowser')
        sleep(3)
        basic.cls()

try:
    from requests import get
except:
    if(name=="posix"):
        system("pacman -S python-pip")
        system("pip install requests")
        basic.cls()
        print(info.hours(),'Instalado requests.')
        sleep(3)
        basic.cls()

    else:
        system("pip install requests")
        basic.cls()
        print(info.hours(),'Instalado requests.')
        sleep(3)
        basic.cls()

class consultas():
    def inpu():
        prints.ban()
        prints.util()

        # parte que talvez vai ficar bagunçada, mas vou tentar deixar organizado.

    def escs():
        try:
            print(f'Digite a opcao desejada.\n')
            inp = int(input(f'╭─{info.user()}{vd}@{vd}{magen}{info.user()} in ~via  v3.9.9\n╰─λ '))
        except:
            print(f'{verm}Voce nao digitou um numero.')
            sleep(3)
            basic.reset()
            basic.cls()

        if(inp == 1):
            basic.cls()
            print(f'Digite o cpf sem pontos.')
            try:
                cpf = int(input(f'╭─{info.user()}{vd}@{vd}{magen}{info.user()} in ~via  v3.9.9\n╰─λ '))
            except:
                basic.cls()
                print(f'{verm}Voce nao digitou um numero de CPF valido!')
                sleep(3)
                basic.ent()

            # URL DO GET
            try:
                url = get(f'http://api.trackear.com.br/basepv/cpf/{cpf}/noip').json()
            except:
                basic.cls()
                print(f'!ERRO! Ocorreu um erro na tentativa de request. Tente novamente mais tarde.')
                basic.ent()

            for i in url:
                print(f'{magen}{i}{magen}: {url[i]}')
            basic.ent()

        elif(inp == 2):
            basic.cls()
            print(f'Digite o nome sem acentos.')
            nom = str(input(f'╭─{info.user()}{vd}@{vd}{magen}{info.user()} in ~via  v3.9.9\n╰─λ '))

            # URL DO GET
            try:
                url = get(f'http://ghostcenter.xyz/api/nome/{nom}').json()
            except:
                basic.cls()
                print(f'!ERRO! Ocorreu um erro na tentativa de request. Tente novamente mais tarde.')
                basic.ent()

            for a in url:
                print(f'{magen}{a}{magen}: {url[a]}')
            basic.ent()

        elif(inp == 3):
            basic.cls()
            cnpj=input(f'╭─{info.user()}{vd}@{vd}{magen}{info.user()} in ~via  v3.9.9\n╰─λ ')
            try:
                pj = get(f'https://www.receitaws.com.br/v1/cnpj/{cnpj}/').json()
            except:
                basic.cls()
                print(f'!ERRO! Ocorreu um erro na tentativa de request. Tente novamente mais tarde.')
                basic.ent()

            basic.cls()
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
            basic.ent()

        elif(inp == 4):
            basic.cls()
            print(f'Digite o cep sem espacos e pontos.')
            try:
                cep = int(input(f'╭─{info.user()}{vd}@{vd}{magen}{info.user()} in ~via  v3.9.9\n╰─λ '))
            except:
                print(f'{verm}Voce nao digitou um cep valido!')
                basic.ent()

            try:
                url = get(f'https://viacep.com.br/ws/{cep}/json/').json()
            except:
                basic.cls()
                print(f'!ERRO! Ocorreu um erro na tentativa de request. Tente novamente mais tarde.')
                basic.ent()

            for i in url:
                print(f'{magen}{i}{magen}: {url[i]}')
            basic.ent()

        elif(inp == 5):
            basic.cls()
            print(f'Digite a placa sem pontos.')
            try:
                placa = int(input(f'╭─{info.user()}{vd}@{vd}{magen}{info.user()} in ~via  v3.9.9\n╰─λ '))
            except:
                print(f'{verm}Voce nao digitou uma placa valida!')
                basic.ent()

            try:
                url = get(f'https://apicarros.com/v1/consulta/{placa}/json', verify=False).json()
            except:
                basic.cls()
                print(f'!ERRO! Ocorreu um erro na tentativa de request. Tente novamente mais tarde.')
                basic.ent()

            for j in url:
                print(f'{magen}{j}{magen}: {url[j]}')
            basic.ent()

        elif(inp == 6):
            basic.cls()
            print(f'Digite o estado.')
            estad = str(input(f'╭─{info.user()}{vd}@{vd}{magen}{info.user()} in ~via  v3.9.9\n╰─λ '))
            try:
                sp = get(f"https://covid19-brazil-api.now.sh/api/report/v1/brazil/uf/{estad}").json()
            except:
                basic.cls()
                print(f'!ERRO! Ocorreu um erro na tentativa de request. Tente novamente mais tarde.')
                basic.ent()

            for item in sp:
                    if sp[item] != '':
                            print(f'{vd}{item}{cl}: {sp[item]}')

            basic.ent()

        elif(inp == 7):
            basic.cls()
            print(f"{verm}Equipe OnlyFalopas: {magen} MrDiniz, Spyware, R0han Kishibe , Crowley, Swag Baby, Dio brando, Ghosthype")
            basic.ent()

        elif(inp == 8):
            basic.op()

        elif(inp == 9):
            basic.cls()
            print(f'{magen}Obrigado por usar o nosso painel :)\033[m')
            exit()


# chamar voids que criei

basic.cls()
consultas.inpu()
consultas.escs()
