import pyfiglet


#[CONFIG]
title = ".menu"

#[BANNER]
banner = pyfiglet.figlet_format(title)

#[MENU CONFIG]
txtMenuBreak = "Sair" #texto para menu sair
msgBreak = "Finalizando ..." #mensagem para finalizar
msgInvalidOption = "Opção inválida, tente novamente." #mensagem para opção invalida

#funcao exibir menu
def menu(title, options):
    while True:
        
        print(banner) #mostrar banner

        #listar opcoes do menu
        for itens, (option, func) in enumerate(options, 1):
            print(f"[ {itens} ] {option}") #opcoes gerados "[ 0 ] Texto"
        print(f"[ 0 ]", txtMenuBreak) #opcao para sair

        #input opcao do usuario
        menuOption = input(">>> ")

        #verifica opcao
        if menuOption.isdigit():    
            
            #finaliza aplicacao
            if int(menuOption) == 0:
                print(msgBreak) #mensagem para finalizar
                break
            
            #executa funcao do menu
            if int(menuOption) < len(options) + 1:
                action = options[int(menuOption) - 1][1]()
                print(action)
        else:
            print(msgInvalidOption) #mensagem para opção invalida
