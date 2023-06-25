import pyfiglet
from typing import List, Tuple, Callable

#[CONFIG]

def make_title(value: str) -> str:
    return pyfiglet.figlet_format(value)

#[MENU CONFIG]
# constantes para as mensagens do menu
MENU_BREAK_TEXT = "Sair" # texto para menu sair
MENU_BREAK_MSG = "Finalizando ..." # texto para menu sair
INVALID_OPT_MSG = "Opção inválida, tente novamente." #mensagem para opção invalida

def is_int(text: str) -> bool:
    try:
        int(text)
        return True
    except ValueError:
        return False

#funcao exibir menu
def menu(title: str, options: List[Tuple[str, Callable]]):
    # Algo interessante para adicionar é um subtítulo...
    """Cria um menu dinâmico para linha de comando.

    title: str: Título do menu
    options: list[tuple[str, callable]]: Opções do menu e suas ações 
    """
    banner = make_title(title)
    
    while True:
        
        print(banner) # mostrar banner

        # listar opções do menu
        for itens, (option, _) in enumerate(options, 1):
            print(f"[ {itens} ] {option}") #opcoes gerados "[ 0 ] Texto"
        print("[ 0 ]", MENU_BREAK_TEXT)

        # input opção do usuário
        menuOption = input(">>> ")

        # verifica opção
        if menuOption.isdigit():    

            # if int(menuOption) == 0: # Isso poderia causar problemas caso o usuário escrevesse texto.
            # Ao invés, criei uma função simples que checa isso.
            
            if is_int(menuOption):
                # finaliza aplicacao
                if int(menuOption) == 0:
                    print(MENU_BREAK_MSG) #mensagem para finalizar
                    break
                elif int(menuOption) < len(options) + 1:
                    options[int(menuOption) - 1][1]() # Não é melhor só executar diretamente?
                else:                               # Essa corrente de prints não é legal, mas fica um desafio pra ti ae, tenta resolver essa.
                    print(INVALID_OPT_MSG)
            else:
                print(INVALID_OPT_MSG)
        else:
            print(INVALID_OPT_MSG)

# OBS: Poderia utilizar orientação a objetos (classes) para fazer a
# estrutura do que é um Menu e o que ele realmente faz,
# mas a abordagem com funções funciona muito bem. 