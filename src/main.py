from cli_menu import *
# faz mais sentido as ações ficarem diretamente aqui né?

def action_menu1():
    print("Menu 1")

def action_menu2():
    print("Menu 2")

start = [
    # ("nome da opcao", nomeDaFuncao)
    ("Opcao 1", action_menu1),
    ("Opcao 2", action_menu2)
]

# start
menu("fellipematos", start)
