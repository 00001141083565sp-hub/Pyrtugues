# 4. Referência completa de comandos

Esta página é gerada a partir do dicionário `TRADUCAO["portugues"]` do código Desktop fornecido. Algumas entradas são aliases ou regras auxiliares e nem todas devem ser usadas como substituições livres em qualquer posição.

## Regra importante

O tradutor aplica regras contextuais para `se`, `em`, operadores, métodos e módulos. Portanto, a tabela representa o vocabulário implementado, não uma promessa de que cada palavra possa ser trocada de forma cega em qualquer contexto.

## Estruturas de controle

| Pyrtugues | Python | Observação |
|---|---|---|
| `senão se` | `elif` |  |
| `senãose` | `elif` |  |
| `senão` | `else` |  |
| `enquanto verdadeiro` | `while True` |  |
| `enquanto` | `while` |  |
| `para cada` | `for` |  |
| `para` | `for` |  |
| `se` | `if` | Tratamento contextual no tradutor. |
| `em` | `in` | Tratamento contextual no tradutor. |
| `quebrar` | `break` |  |
| `continuar` | `continue` |  |
| `passar` | `pass` |  |
| `com` | `with` |  |
| `como` | `as` |  |
| `finalmente` | `finally` |  |

## Funções, classes e fluxo

| Pyrtugues | Python | Observação |
|---|---|---|
| `função` | `def` |  |
| `classe` | `class` |  |
| `retornar verdadeiro` | `return True` |  |
| `retornar falso` | `return False` |  |
| `retornar nulo` | `return None` |  |
| `retornar` | `return` |  |
| `produzir` | `yield` |  |
| `assíncrono` | `async` |  |
| `aguardar` | `await` |  |
| `global` | `global` |  |
| `nãolocal` | `nonlocal` |  |

## Importação e tratamento de erros

| Pyrtugues | Python | Observação |
|---|---|---|
| `importar` | `import` |  |
| `de` | `from` |  |
| `tentar` | `try` |  |
| `excepto` | `except` |  |
| `levantar` | `raise` |  |
| `afirmar` | `assert` |  |
| `verificar` | `assert` |  |
| `lançar` | `raise` |  |

## Valores e operadores lógicos

| Pyrtugues | Python | Observação |
|---|---|---|
| `verdadeiro` | `True` |  |
| `falso` | `False` |  |
| `nulo` | `None` |  |
| `vazio` | `pass` |  |
| `nada` | `None` |  |
| `e também` | `and` |  |
| `ou então` | `or` |  |
| `não é` | `is not` |  |
| `é` | `is` |  |
| `não` | `not` |  |
| `e` | `and` | Aplicado de forma contextual em expressões. |
| `ou` | `or` | Aplicado de forma contextual em expressões. |
| `maior ou igual a` | `>=` |  |
| `menor ou igual a` | `<=` |  |
| `maior ou igual` | `>=` |  |
| `menor ou igual` | `<=` |  |
| `maior que` | `>` |  |
| `menor que` | `<` |  |
| `diferente de` | `!=` |  |
| `igual a` | `==` |  |
| `fora de` | `not in` |  |
| `dentro de` | `in` |  |

## Operadores aritméticos

| Pyrtugues | Python | Observação |
|---|---|---|
| `mais` | `+` | Aplicado de forma contextual em expressões. |
| `menos` | `-` | Aplicado de forma contextual em expressões. |
| `vezes` | `*` | Aplicado de forma contextual em expressões. |
| `dividido por` | `/` |  |
| `resto` | `%` | Aplicado de forma contextual em expressões. |
| `potência` | `**` | Aplicado de forma contextual em expressões. |
| `elevado a` | `**` |  |
| `mais igual` | `+=` |  |
| `menos igual` | `-=` |  |
| `vezes igual` | `*=` |  |
| `dividido igual` | `/=` |  |
| `resto igual` | `%=` |  |
| `potência igual` | `**=` |  |

## Tipos e construtores

| Pyrtugues | Python | Observação |
|---|---|---|
| `inteiro` | `int` |  |
| `decimal` | `float` |  |
| `texto` | `str` |  |
| `booleano` | `bool` |  |
| `lista` | `list` |  |
| `dicionário` | `dict` |  |
| `tupla` | `tuple` |  |
| `conjunto` | `set` |  |

## Entrada, saída e built-ins

| Pyrtugues | Python | Observação |
|---|---|---|
| `mostrar` | `print` |  |
| `imprimir` | `print` |  |
| `pergunte` | `input` |  |
| `pergunta` | `input` |  |
| `intervalo` | `range` |  |
| `tamanho` | `len` |  |
| `comprimento` | `len` |  |
| `tipo` | `type` |  |
| `é instância` | `isinstance` |  |
| `é subclasse` | `issubclass` |  |
| `somar` | `sum` |  |
| `máximo` | `max` |  |
| `mínimo` | `min` |  |
| `ordenar` | `sorted` |  |
| `inverter` | `reversed` |  |
| `filtrar` | `filter` |  |
| `mapear` | `map` |  |
| `zipar` | `zip` |  |
| `enumerar` | `enumerate` |  |
| `todos` | `all` |  |
| `algum` | `any` |  |
| `absoluto` | `abs` |  |
| `arredondar` | `round` |  |
| `elevar` | `pow` |  |
| `hexadecimal` | `hex` |  |
| `octal` | `oct` |  |
| `binário` | `bin` |  |
| `ordinal` | `ord` |  |
| `caractere` | `chr` |  |
| `ajuda` | `help` |  |
| `atributos` | `vars` |  |
| `abrir` | `open` |  |
| `formatar` | `format` |  |
| `representar` | `repr` |  |
| `sair` | `exit` |  |
| `parar` | `stop` |  |
| `iniciar` | `start` |  |

## Métodos de string

| Pyrtugues | Python | Observação |
|---|---|---|
| `maiúsculas` | `upper` | Usado principalmente como método após `.`. |
| `minúsculas` | `lower` | Usado principalmente como método após `.`. |
| `capitalizar` | `capitalize` |  |
| `título` | `title` |  |
| `trocar` | `replace` |  |
| `dividir` | `split` |  |
| `juntar` | `join` |  |
| `tirar espaços` | `strip` |  |
| `começa com` | `startswith` |  |
| `termina com` | `endswith` |  |
| `encontrar` | `find` |  |
| `contar` | `count` |  |
| `é dígito` | `isdigit` |  |
| `é letra` | `isalpha` |  |
| `é espaço` | `isspace` |  |

## Métodos de lista

| Pyrtugues | Python | Observação |
|---|---|---|
| `adicionar` | `append` | Usado principalmente como método após `.`. |
| `estender` | `extend` |  |
| `inserir` | `insert` |  |
| `remover` | `remove` |  |
| `tirar` | `pop` |  |
| `limpar` | `clear` |  |
| `copiar` | `copy` |  |
| `índice` | `index` |  |
| `ordenar em ordem` | `sort` |  |
| `inverter ordem` | `reverse` |  |

## Métodos de dicionário

| Pyrtugues | Python | Observação |
|---|---|---|
| `chaves` | `keys` | Usado principalmente como método após `.`. |
| `valores` | `values` | Usado principalmente como método após `.`. |
| `itens` | `items` | Usado principalmente como método após `.`. |
| `pegar` | `get` | Usado principalmente como método após `.`. |
| `atualizar` | `update` | Usado principalmente como método após `.`. |

## Módulos e nomes auxiliares

| Pyrtugues | Python | Observação |
|---|---|---|
| `matemática` | `math` | Tratamento especial em imports/nomes qualificados. |
| `aleatório` | `random` | Tratamento especial em imports/nomes qualificados. |
| `data e hora` | `datetime` | Tratamento especial em imports/nomes qualificados. |
| `tempo` | `time` | Tratamento especial em imports/nomes qualificados. |
| `sistema` | `os` | Tratamento especial em imports/nomes qualificados. |
| `caminho` | `path` |  |
| `arquivo` | `file` |  |
| `requisição` | `request` |  |
| `resposta` | `response` |  |
| `expressão regular` | `re` | Tratamento especial em imports/nomes qualificados. |

## Exemplos rápidos

### Saída

```pyrtugues
mostrar("Olá")
```

### Entrada

```pyrtugues
nome = pergunte("Nome: ")
```

### Condição

```pyrtugues
se idade maior ou igual a 18:
    mostrar("Adulto")
senão:
    mostrar("Menor")
```

### Repetição

```pyrtugues
para i em intervalo(1, 6):
    mostrar(i)
```

### Função

```pyrtugues
função saudar(nome):
    retornar f"Olá, {nome}!"
```

### Tratamento de exceções

```pyrtugues
tentar:
    ...
excepto:
    ...
finalmente:
    ...
```
