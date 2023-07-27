# cli-Menu
Simples menu para utilizar em suas aplicações CLI.
_Código simples e comentado, para futuras atualizações_

## Como utilizar
Instale `requirements.txt` no diretório do projeto:

```bash
$ cd pasta/do/cli-menu
$ python -m pip install -r requirements.txt
```

Clone o repositório do git, acesse a pasta src (pasta que contém os arquivos .py), execute o arquivo principal **main.py**

```bash
git clone https://github.com/fellipematos/simple-menu-cli
cd cli-menu/src
python main.py
```

---

### Personalização

Você pode mudar algumas constantes ao importar a biblioteca para mudar como `cli-menu` vai gerar os menus:
- `MENU_BREAK_TEXT`: Texto da opção de sair do menu.
- `MENU_BREAK_MSG`: Texto que será impresso na tela quando o usuário sair.
- `INVALID_OPT_MSG`: Mensagem para opção invalida.

---

Você pode utilizar apenas o arquivo `cli_menu.py` nas suas aplicações. Importe o arquivo na sua aplicação, define a variável com as opções do menu _conforme o modelo abaixo_

```python
from menuConfig import *

def funcaoMenu1(): ...
def funcaoMenu2(): ...
...

START = [
  ("Nome da Opcao 1", funcaoMenu1),
  ("Nome da Opcao 2", funcaoMenu2)
]
```

Depois que definir as opções do menu, inicie a função Menu() com os parâmetros _*conforme o modelo abaixo_

```python
menu("fellipematos", START)  # menu(título do menu, opções do menu)
```

---

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
