# simple-menu-cli
Simples menu para utilizar em suas aplicações CLI.
_Código simples e comentado, para futuras atualizações_

## Como utilizar:
Instale a biblioteca **pyfiglet**

> python -m pip install pyfiglet

Clone o repositório do git, acesse a pasta src (pasta que contém os arquivos .py), execute o arquivo principal **main.py**

> git clone https://github.com/fellipematos/simple-menu-cli
> cd simples-menu-cli/src
> python main.py

<HR>

### Arquivo de Configuração **menuConfig.py**
**title**: Define o titulo da sua aplicação.
**txtMenuBreak**: Define o texto para menu sair.
**msgBreak**: Define a mensagem para finalizar sua aplicação.
**msgInvalidOption**: Define a mensagem para opções inválida.

<HR>

### Arquivo de Funções **actions.py**
Arquivo para criar suas funções do menu.

<HR>

Você pode utilizar apenas o arquivo **menuConfig.py** nas suas aplicações. Importe o arquivo na sua aplicação, define a variável com as opções do menu _*conforme o modelo abaixo_

>from menuConfig import *
>
>**start** = [
>("Nome da Opcao 1", funcaoMenu1),
>("Nome da Opcao 2", funcaoMenu2)
>]


Depois que definir as opções do menu, inicie a função Menu() com os parâmetros _*conforme o modelo abaixo_

>menu("", **start**)

  <HR>

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
