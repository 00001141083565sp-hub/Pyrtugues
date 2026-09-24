# Documentação Oficial do Pyrtugues

> **Pyrtugues — Python em português, feito para aprender programação.**

Esta documentação foi montada a partir dos arquivos fornecidos do projeto: o código Desktop atual, o README, os arquivos HTML do site/editor Web e a licença atual.

## O que é o Pyrtugues?

O Pyrtugues é um projeto educacional de programação em português criado para facilitar o primeiro contato com lógica de programação e Python. A proposta é manter programação textual, usar uma sintaxe em português e permitir que o estudante enxergue a relação com o Python tradicional.

**Fluxo central:**

```text
Programar em português
        ↓
Entender a lógica
        ↓
Enxergar o Python
        ↓
Aprender Python
```

O README descreve o projeto como uma ponte para Python, e a Web usa a arquitetura Pyrtugues → tradutor → Python → Pyodide → execução no navegador.

## Navegação

- [01 — Introdução](01-introducao.md)
- [02 — Primeiros passos](02-primeiros-passos.md)
- [03 — Sintaxe](03-sintaxe.md)
- [04 — Referência completa de comandos](04-comandos.md)
- [05 — Como funciona o tradutor](05-tradutor.md)
- [06 — Desktop](06-desktop.md)
- [07 — Editor Web](07-web.md)
- [08 — Erros e execução](08-erros.md)
- [09 — Exemplos](09-exemplos.md)
- [10 — Pyrtugues → Python](10-pyrtugues-python.md)
- [11 — Para desenvolvedores](11-desenvolvedores.md)
- [12 — FAQ](12-faq.md)
- [13 — Licença](13-licenca.md)
- [14 — Glossário](14-glossario.md)
- [15 — Estado e limites documentados](15-estado-do-projeto.md)

## Versão e fonte

O código Desktop fornecido declara `1.3.0`. O README fornecido ainda contém `1.2.0` como versão atual em uma seção antiga. Por isso, esta documentação usa **v1.3.0 como referência do código Desktop** e registra a divergência em [Estado do projeto](15-estado-do-projeto.md).

## Canais oficiais

- Site: https://pyrtugues.netlify.app/
- Editor Web: https://pyrtugues-editor.netlify.app/
- GitHub: https://github.com/pyrtugues/Pyrtugues
- Releases: https://github.com/pyrtugues/Pyrtugues/releases/latest
- YouTube: https://www.youtube.com/@pyrtugues



---


# 1. Introdução

## O que é?

Pyrtugues é um projeto educacional de programação em português para facilitar o primeiro contato com lógica de programação e Python.

A ideia não é transformar programação em blocos. O usuário escreve código textual e utiliza comandos em português, enquanto a lógica continua próxima do Python.

## O problema que o projeto tenta reduzir

Um iniciante pode encontrar uma barreira inicial ao se deparar com palavras-chave como `if`, `else`, `while` e `print`. O Pyrtugues propõe começar com equivalentes em português e, ao mesmo tempo, mostrar o caminho para o Python.

## O que o Pyrtugues não é

- Não é o interpretador oficial do Python.
- Não é uma versão completa e independente do Python.
- Não é Scratch.
- Não pretende esconder a programação textual.
- Não deve ser tratado como substituto do Python.

## Identidade da proposta

> **Programar em português → entender a lógica → enxergar o Python → aprender Python.**

## Pyrtugues e nomes parecidos

**Pyrtugues** é o nome do projeto. Não deve ser confundido automaticamente com Pytuguês, Pituguês, Pytuga ou outros projetos de nomes semelhantes.



---


# 2. Primeiros passos

## Opção 1 — Editor Web

Abra o Editor Web:

https://pyrtugues-editor.netlify.app/

A versão Web permite escrever código Pyrtugues, visualizar o Python gerado, executar no navegador e receber entradas interativas.

## Opção 2 — Desktop

A versão Desktop atual é uma aplicação gráfica para Windows desenvolvida em Python + CustomTkinter/Tkinter. Os executáveis e releases ficam no GitHub.

## Primeiro programa

Comece com:

```pyrtugues
mostrar("Olá, mundo!")
```

Equivalente em Python:

```python
print("Olá, mundo!")
```

## Primeiro programa com variável

```pyrtugues
nome = "Ana"
mostrar(nome)
```

## Primeiro programa com entrada

```pyrtugues
nome = pergunte("Qual é o seu nome? ")
mostrar(f"Olá, {nome}!")
```

## Primeiro programa com condição

```pyrtugues
idade = 15

se idade maior que 10:
    mostrar("Você pode continuar!")
senão:
    mostrar("Ainda é cedo.")
```

## O fluxo mental

Ao escrever Pyrtugues, tente pensar na lógica primeiro e na tradução depois. O objetivo não é decorar substituições isoladas, mas reconhecer que as estruturas correspondem a conceitos do Python.



---


# 3. Sintaxe

## Blocos

Como no Python, estruturas compostas usam `:` e indentação.

```pyrtugues
se idade maior que 10:
    mostrar("Maior")
senão:
    mostrar("Menor")
```

## Variáveis

Atribuição segue a forma usada em Python:

```pyrtugues
nome = "Ana"
idade = 12
altura = 1.55
```

## Comentários

Comentários começam com `#`.

```pyrtugues
# Isto é um comentário
mostrar("Olá")
```

O tradutor protege comentários antes das substituições para que palavras dentro do comentário não sejam alteradas.

## Strings

Strings podem conter palavras que também são comandos do Pyrtugues sem que essas palavras sejam traduzidas.

```pyrtugues
mostrar("se idade maior que 10")
```

O texto continua como foi escrito.

## F-strings

F-strings podem conter expressões traduzíveis dentro de `{}`.

```pyrtugues
nome = "Ana"
mostrar(f"Olá, {nome}!")
```

O tradutor possui tratamento específico para expressões dentro de f-strings.

## Comparações em linguagem natural

Exemplos:

```pyrtugues
idade maior que 10
idade menor que 18
idade igual a 12
idade diferente de 10
idade maior ou igual a 18
idade menor ou igual a 17
```

## Operadores lógicos

```pyrtugues
idade maior que 10 e idade menor que 18
```

ou:

```pyrtugues
idade menor que 10 ou idade maior que 18
```

Também existe `não`.

## Atenção a contexto

O tradutor possui regras especiais para evitar substituições indevidas.

### `se`

Uma linha como:

```pyrtugues
se = 19
```

pode ser usada como variável, sem virar `if`.

Uma condição como:

```pyrtugues
se x:
    mostrar("Funcionou")
```

é traduzida para `if x:`.

### `em`

Na construção de repetição:

```pyrtugues
para numero em intervalo(1, 6):
    mostrar(numero)
```

`em` é convertido para `in`.

## Aliases

O dicionário atual também possui formas alternativas, por exemplo:

- `imprimir()` → `print()`
- `pergunta()` → `input()`
- `senãose` → `elif`
- `verificar` → `assert`
- `lançar` → `raise`



---


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



---


# 5. Como funciona o tradutor

## Arquitetura

```text
Código Pyrtugues
      ↓
Proteção de strings e comentários
      ↓
Traduções básicas
      ↓
Regras contextuais
      ↓
Restauração de strings e comentários
      ↓
Código Python
```

## Proteção de strings e comentários

O código Desktop possui um scanner caractere a caractere que protege:

- comentários iniciados por `#`;
- strings simples;
- strings duplas;
- strings multilinha;
- strings com prefixos;
- f-strings.

Os trechos protegidos recebem placeholders no formato:

```text
__PYRT_STR_0__
__PYRT_STR_1__
...
```

Depois das traduções, os trechos originais são restaurados.

Isso evita, por exemplo, que:

```pyrtugues
mostrar("se idade maior que 10")
```

seja transformado em uma instrução Python diferente.

## Ordenação das traduções

As chaves do dicionário são ordenadas do maior para o menor texto antes da aplicação. Isso faz com que expressões como:

```text
senão se
maior ou igual a
retornar verdadeiro
```

tenham prioridade sobre componentes menores.

## Limites de palavra

A função `_substituir_palavra()` usa limites baseados em caracteres para evitar que uma palavra localizada seja substituída dentro de um identificador maior.

## Regra especial para `se`

O código usa uma expressão contextual:

```text
^(\s*)se(?=\s+.+:)
```

Assim, `se` no início de uma condição pode virar `if`, enquanto um identificador como:

```pyrtugues
se = 19
```

não é convertido automaticamente.

## Regra especial para `em`

Depois que `para` vira `for`, o tradutor converte `em` apenas no formato de repetição:

```pyrtugues
para x em ...
```

para:

```python
for x in ...
```

A implementação procura um nome de variável entre `for` e `em`.

## Métodos

Os métodos em português são tratados quando aparecem após um ponto.

Exemplo:

```pyrtugues
nome.maiúsculas()
```

→

```python
nome.upper()
```

## Módulos

Nomes de módulos recebem tratamento especial em `import`/`from` e em referências qualificadas.

Exemplos do dicionário:

```text
matemática → math
aleatório → random
data e hora → datetime
tempo → time
sistema → os
expressão regular → re
```

## F-strings

O código possui um parser específico para f-strings. Ele:

1. preserva `{{` e `}}`;
2. encontra expressões dentro de `{}`;
3. acompanha profundidade de chaves;
4. respeita strings internas e escapes;
5. traduz a expressão interna;
6. recompõe a f-string.

## `pergunte()` no Desktop

No tradutor geral, `pergunte(` e `pergunta(` são convertidos para `input(`. Durante a execução Desktop, o namespace de execução substitui `input` por `self.input_gui`, permitindo entrada gráfica.

## O que não deve ser feito ao alterar o tradutor

Ao modificar o tradutor, teste especialmente:

- strings;
- comentários;
- f-strings;
- nomes de variáveis;
- `se` usado como variável;
- `em` em loops;
- operadores em frases;
- métodos depois de `.`;
- módulos em imports;
- código parcialmente digitado.



---


# 6. Aplicação Desktop

## Stack

A aplicação Desktop usa:

- Python;
- CustomTkinter;
- Tkinter.

## Versão atual do código fornecido

A classe `JanelaBR` define:

```python
self.versao = "1.3.0"
```

## Estrutura da interface

A janela é organizada como uma IDE educacional:

```text
┌────────────────────────┬───────────────────────┐
│ Seu Código             │ Python Gerado         │
│ Editor                 │ Tradução em tempo real│
└────────────────────────┴───────────────────────┘
[ Executar ] [ Parar ] [ Limpar saída ]
┌───────────────────────────────────────────────┐
│ Terminal / Saída                              │
└───────────────────────────────────────────────┘
```

A navegação interna possui:

- Editor;
- Exemplos;
- Sobre.

## Recursos do editor

O código fornecido implementa:

- números de linha;
- sincronização dos números de linha;
- destaque da linha atual;
- atualização do Python gerado;
- fechamento automático de pares e aspas;
- indentação automática;
- Tab e Shift+Tab;
- suporte a atalhos;
- copiar Python;
- baixar Python;
- carregamento de exemplos.

## Atalho principal

`Ctrl + Enter` executa o código.

## Visualização do Python

A tradução pode ser atualizada enquanto o usuário escreve, sem alterar o conteúdo digitado no editor.

Se a tradução temporária falhar enquanto o código está incompleto, a interface preserva a última tradução válida em vez de interromper a edição.

## Exemplos integrados

A aplicação possui uma biblioteca interna de exemplos, incluindo pelo menos exemplos de:

- Olá mundo;
- variáveis/saída;
- condição;
- repetição;
- função;
- calculadora.

## Execução

O Desktop executa o Python traduzido em uma thread em background.

O código executado recebe substituições de `input` e `print` para integrar entrada e saída com a interface.

## Parar execução

A aplicação usa `sys.settrace` e um evento de parada para detectar a solicitação de interrupção.

O botão **Parar** aciona essa interrupção e também cancela uma entrada gráfica pendente, quando necessário.



---


# 7. Editor Web

## Endereço

https://pyrtugues-editor.netlify.app/

## Tecnologias

O arquivo Web fornecido usa:

- HTML;
- CSS;
- JavaScript;
- Tailwind CSS por CDN;
- Font Awesome;
- Fira Code;
- Plus Jakarta Sans;
- Pyodide;
- Web Worker.

## Arquitetura declarada

```text
Pyrtugues
    ↓
Tradutor
    ↓
Python
    ↓
Pyodide
    ↓
Execução no navegador
```

## Interface do editor

A versão Web inclui:

- editor Pyrtugues;
- painel de Python gerado;
- execução;
- parada da execução;
- terminal;
- entrada interativa;
- exemplos;
- navegação Editor / Exemplos / Sobre;
- copiar Python;
- baixar `.py`;
- status do motor.

## Exemplo inicial

O editor Web fornecido inicia com um programa que usa:

```pyrtugues
mostrar("=== BEM-VINDO AO PYRTUGUES ===")

nome = pergunte("Qual é o seu nome? ")
idade = inteiro(pergunte("Quantos anos você tem? "))

se idade maior ou igual a 12:
    mostrar(f"Olá, {nome}! Você já pode criar jogos e aplicações incríveis.")
senão:
    mostrar(f"Oi, {nome}! Continue praticando lógica de programação!")
```

## Entrada interativa

A Web usa um modal de entrada solicitado pelo programa.

O fluxo é:

```text
pergunte(...)
    ↓
pedido de entrada
    ↓
janela/modal
    ↓
resposta do usuário
    ↓
continuação da execução
```

## Responsividade e aparência

O editor foi estruturado para telas menores, usa controles de toque com áreas mínimas e possui suporte a preferência de movimento reduzido no CSS.

## Site principal

https://pyrtugues.netlify.app/



---


# 8. Erros e execução

## Erros no Desktop

Quando uma execução falha, o código captura a exceção e tenta localizar a linha de erro no código gerado.

A aplicação percorre o traceback e procura o frame com:

```text
co_filename == "<string>"
```

A linha é então usada para apontar a linha correspondente do código Pyrtugues original.

A interface exibe:

```text
❌ Erro na linha X:
   <linha do código>

   Detalhes: <erro>
```

## Execução interrompida

Quando o usuário aciona Parar, a aplicação define um evento de interrupção.

O tracer pode gerar:

```text
Execução interrompida pelo usuário.
```

A aplicação então restaura o estado dos botões.

## Entrada pendente

Se `pergunte()` estiver esperando uma resposta e o usuário mandar parar a execução, a janela de entrada é fechada e os pedidos pendentes são cancelados.

## Erros de tradução

Enquanto o usuário ainda está digitando um código incompleto, a atualização do preview Python pode falhar temporariamente. O editor Desktop trata esse caso para não interromper a edição.

## Importante sobre segurança

A execução Desktop usa `exec()` sobre o Python traduzido. Isso significa que o Desktop **não deve ser descrito como um sandbox de segurança para código não confiável**.

A Web usa Pyodide/Web Worker, mas qualquer afirmação de segurança precisa considerar as APIs realmente expostas pelo ambiente Web.

## Exemplos de erro úteis para iniciantes

### Variável inexistente

```pyrtugues
mostrar(nome)
```

Se `nome` não foi definido, a execução poderá gerar erro de nome no Python.

A documentação pode ensinar:

```pyrtugues
nome = "Ana"
mostrar(nome)
```

### Conversão de entrada

Em vez de:

```pyrtugues
idade = pergunte("Idade: ")
```

quando uma operação numérica for necessária, use:

```pyrtugues
idade = inteiro(pergunte("Idade: "))
```



---


# 9. Exemplos práticos

## Olá, mundo

```pyrtugues
mostrar("Olá, mundo!")
```

## Variáveis

```pyrtugues
nome = "Vinicius"
idade = 12

mostrar(nome)
mostrar(idade)
```

## F-string

```pyrtugues
nome = "Ana"
idade = 12

mostrar(f"Olá, {nome}! Você tem {idade} anos.")
```

## Condição

```pyrtugues
idade = 15

se idade maior que 10:
    mostrar("Você pode continuar!")
senão:
    mostrar("Ainda é cedo.")
```

## Senão se

```pyrtugues
nota = 7

se nota maior ou igual a 7:
    mostrar("Aprovado")
senão se nota maior ou igual a 5:
    mostrar("Recuperação")
senão:
    mostrar("Reprovado")
```

## Repetição

```pyrtugues
para i em intervalo(1, 6):
    mostrar(i)
```

## Enquanto

```pyrtugues
contador = 1

enquanto contador menor ou igual a 5:
    mostrar(contador)
    contador mais igual 1
```

## Função

```pyrtugues
função saudar(nome):
    mostrar(f"Olá, {nome}!")

saudar("Ana")
```

## Retorno

```pyrtugues
função somar(a, b):
    retornar a + b

resultado = somar(10, 20)
mostrar(resultado)
```

## Calculadora

```pyrtugues
n1 = decimal(pergunte("Primeiro número: "))
op = pergunte("Operação (+, -, *, /): ")
n2 = decimal(pergunte("Segundo número: "))

se op == "+":
    mostrar(n1 + n2)
senão se op == "-":
    mostrar(n1 - n2)
senão se op == "*":
    mostrar(n1 * n2)
senão:
    mostrar(n1 / n2)
```

## Média

```pyrtugues
função calcular_media(nota1, nota2):
    retornar (nota1 + nota2) / 2

nota1 = decimal(pergunte("Nota 1: "))
nota2 = decimal(pergunte("Nota 2: "))

media = calcular_media(nota1, nota2)
mostrar(f"Média: {media}")
```

## Testando a regra especial de `se`

```pyrtugues
se = 19
x = se

se x:
    mostrar("Funcionou!")
```

A expectativa do tradutor é preservar `se = 19` e transformar a condição em `if x:`.

## Testando proteção de strings

```pyrtugues
mostrar("se idade maior que 10")
```

O texto dentro da string deve permanecer inalterado.



---


# 10. Pyrtugues → Python

## Ideia central

O objetivo do Pyrtugues não é prender o usuário em uma sintaxe paralela. A visualização do Python é parte da proposta educacional.

## Tabela básica

| Pyrtugues | Python |
|---|---|
| `mostrar()` | `print()` |
| `pergunte()` | `input()` |
| `se` | `if` |
| `senão` | `else` |
| `senão se` | `elif` |
| `enquanto` | `while` |
| `para` | `for` |
| `em` | `in` |
| `função` | `def` |
| `retornar` | `return` |
| `importar` | `import` |
| `tentar` | `try` |
| `excepto` | `except` |
| `inteiro()` | `int()` |
| `decimal()` | `float()` |
| `texto()` | `str()` |
| `lista()` | `list()` |
| `dicionário()` | `dict()` |
| `tupla()` | `tuple()` |
| `conjunto()` | `set()` |
| `intervalo()` | `range()` |
| `tamanho()` | `len()` |
| `verdadeiro` | `True` |
| `falso` | `False` |
| `nulo` | `None` |

## Exemplo lado a lado

### Pyrtugues

```pyrtugues
se idade maior ou igual a 18:
    mostrar("Pode entrar")
senão:
    mostrar("Não pode entrar")
```

### Python

```python
if idade >= 18:
    print("Pode entrar")
else:
    print("Não pode entrar")
```

## Por que isso é importante?

Ao visualizar o equivalente, o estudante pode começar a reconhecer:

- `se` → `if`;
- `senão` → `else`;
- `função` → `def`;
- `mostrar()` → `print()`;
- operadores em linguagem natural → operadores Python.

A migração para Python fica baseada em correspondências concretas, sem apagar a lógica que o estudante já aprendeu.



---


# 11. Para desenvolvedores

## Estrutura básica

A documentação fornecida aponta para:

```text
Pyrtugues/
├── assets/
├── LICENSE
├── README.md
├── Pyrtugues_code.py
├── index.html
└── ...
```

## Desktop

O arquivo principal é:

```text
Pyrtugues_code.py
```

A aplicação contém:

- tradução;
- interface;
- editor;
- exemplos;
- entrada gráfica;
- execução em background;
- terminal;
- tratamento de erros;
- navegação interna.

## Função pública de tradução

A função principal de tradução é:

```python
traduzir(codigo_br)
```

Ela:

1. protege strings e comentários;
2. aplica as traduções base;
3. trata `pergunte()`/`pergunta()` como `input()`;
4. restaura strings e comentários.

## Funções internas importantes

- `_proteger_strings_e_comentarios()`
- `_aplicar_traducoes_base()`
- `_traduzir_fstring()`
- `_traduzir_expressao_fstring()`
- `_substituir_palavra()`
- `traduzir()`

## Alterando o dicionário

O vocabulário principal fica em:

```python
TRADUCAO["portugues"]
```

As entradas são pares:

```python
"mostrar": "print"
```

## Contextos especiais

Nem tudo deve ser adicionado como substituição direta.

O código atual tem conjuntos auxiliares:

- `_METODOS`
- `_MODULOS`
- `_SKIP_DIRETO`

Esses conjuntos fazem parte da estratégia para evitar substituições incorretas.

## Regras para novas traduções

Antes de adicionar uma palavra:

1. verifique se ela pode aparecer dentro de strings;
2. verifique se pode ser nome de variável;
3. verifique se depende de contexto;
4. verifique se aparece depois de `.`;
5. verifique se deve funcionar em `import`/`from`;
6. adicione teste para o caso novo;
7. teste casos já existentes.

## F-string

Qualquer mudança no tradutor deve incluir testes para:

- texto literal;
- expressões;
- chaves aninhadas;
- strings dentro de expressões;
- escapes;
- `{{` e `}}`.

## Testes recomendados

O projeto deve testar pelo menos:

```pyrtugues
mostrar("Olá")
```

```pyrtugues
x = 10
mostrar(x)
```

```pyrtugues
x = 10
se x maior que 5:
    mostrar("sim")
```

```pyrtugues
para i em intervalo(1, 4):
    mostrar(i)
```

```pyrtugues
nome = "Ana"
mostrar(f"Olá, {nome}")
```

```pyrtugues
e = 10
mostrar(e)
```

```pyrtugues
mostrar("se idade maior que 10")
```

```pyrtugues
se = 19
x = se
se x:
    mostrar("foi")
```

## Observação sobre testes automatizados

O arquivo Desktop fornecido não contém uma suíte `pytest`/`unittest` dedicada. A seção acima é uma especificação recomendada de testes de regressão baseada nos casos críticos do tradutor.



---


# 12. FAQ

## Pyrtugues é Python?

Não. É uma proposta de sintaxe em português baseada na lógica do Python e traduzida para Python antes da execução.

## Pyrtugues substitui Python?

Não. O objetivo declarado é funcionar como uma ponte para aprender Python.

## Preciso saber inglês para começar?

A proposta é reduzir a barreira inicial causada pelos comandos em inglês. Depois, o estudante pode usar a relação visual com Python para continuar o aprendizado.

## Pyrtugues funciona no navegador?

Sim. O Editor Web usa Pyodide para executar Python no navegador.

## Pyrtugues funciona no Windows?

Sim. Existe uma aplicação Desktop para Windows.

## Existe versão Linux?

Os arquivos fornecidos documentam apenas Windows no Desktop e Web no navegador. Não há versão Linux documentada neles.

## Existe `pergunte()`?

Sim. `pergunte()` e o alias `pergunta()` correspondem a `input()`.

## Existe `mostrar()`?

Sim. `mostrar()` e `imprimir()` correspondem a `print()`.

## O código é realmente executado?

Sim, conforme a arquitetura documentada. No Desktop, o Python traduzido é executado no ambiente Python; na Web, Pyodide executa Python no navegador.

## O Pyrtugues é Scratch?

Não. O projeto é textual e mantém uma organização próxima da lógica do Python.

## O Pyrtugues é Portugol?

Não. A proposta e a arquitetura são diferentes: o Pyrtugues é pensado explicitamente como ponte para Python.

## Onde vejo o Python gerado?

No editor Desktop e no Editor Web há visualização/cópia do Python gerado.

## Posso modificar o Pyrtugues?

A resposta depende do tipo de uso. A licença atual permite modificações dentro das condições de uso pessoal ou educacional individual e restringe usos institucionais e comerciais sem autorização. Consulte o arquivo `LICENSE`.

## Pyrtugues é open source?

A licença atual é própria e restritiva. Ela deve ser lida antes de classificar o projeto juridicamente como open source.

## O projeto está pronto?

O projeto continua em desenvolvimento. A compatibilidade pode mudar e novos comandos/recursos podem ser adicionados.



---


# 13. Licença

## Nome

**PYRTUGUES PERSONAL & INDIVIDUAL EDUCATIONAL LICENSE**

Copyright (c) 2026 Vinicius Caracciolo.

## Resumo em linguagem simples

A licença concede gratuitamente:

- uso pessoal;
- uso educacional individual;
- estudo do código-fonte;
- cópias para esses fins;
- compartilhamento de cópia dentro dessas mesmas condições;
- compartilhamento de links oficiais.

Ela exige autorização prévia e expressa do autor para, entre outros:

- uso institucional;
- adoção oficial em escolas, cursos, universidades, empresas ou organizações;
- uso comercial;
- venda ou revenda;
- incorporação em produtos comerciais;
- geração de receita direta ou indireta.

Modificações também ficam limitadas às condições de uso pessoal ou educacional individual.

A licença preserva os créditos e não concede direitos sobre:

- nome Pyrtugues;
- logotipos;
- identidade visual;
- marcas.

## Regra prática

**Código publicado no GitHub não significa autorização automática para qualquer uso.**

Antes de copiar, modificar, redistribuir ou usar institucional/comercialmente, consulte o arquivo `LICENSE` e, quando necessário, solicite autorização ao autor.

> Esta página é um resumo informativo da licença fornecida. Para regras jurídicas aplicáveis ao projeto, o texto integral do arquivo `LICENSE` prevalece.



---


# 14. Glossário

### Pyrtugues
Projeto educacional de programação em português baseado na lógica do Python.

### Python
Linguagem que recebe o código traduzido pelo motor do Pyrtugues.

### Tradutor
Componente que transforma a sintaxe Pyrtugues em uma sintaxe Python correspondente.

### F-string
String formatada do Python que permite expressões dentro de `{}`.

### Editor Web
Versão executada no navegador, usando Pyodide e Web Worker.

### Pyodide
Ambiente usado pela versão Web para executar Python no navegador.

### Web Worker
Mecanismo do navegador utilizado pela versão Web para manter o motor de execução fora da interface principal.

### Desktop
Aplicação gráfica para Windows.

### `mostrar()`
Saída equivalente a `print()`.

### `pergunte()`
Entrada equivalente a `input()`.

### `se`
Estrutura condicional equivalente a `if` quando usada no contexto de condição.

### `senão`
Equivalente a `else`.

### `senão se`
Equivalente a `elif`.

### `para`
Equivalente a `for`.

### `em`
Equivalente a `in` na construção de repetição.

### `função`
Equivalente a `def`.

### `retornar`
Equivalente a `return`.

### `verdadeiro`
Equivalente a `True`.

### `falso`
Equivalente a `False`.

### `nulo`
Equivalente a `None`.



---


# 15. Estado do projeto e limites documentados

## Versão

O código Desktop fornecido define:

```python
self.versao = "1.3.0"
```

O README fornecido ainda possui uma seção declarando `1.2.0` como versão atual. Isso é uma divergência documental que deve ser sincronizada quando a documentação oficial for atualizada.

## O que já está documentado nos arquivos fornecidos

- linguagem em português;
- tradução para Python;
- execução Desktop;
- execução Web;
- editor;
- exemplos;
- entrada interativa;
- saída;
- licença própria;
- criador;
- site, editor Web, GitHub e YouTube.

## O que não deve ser declarado como implementado sem verificação adicional

- versão Linux;
- versão macOS;
- versão Android/iOS;
- suporte completo a toda a linguagem Python;
- sandbox absoluto para o Desktop;
- suíte de testes automatizados;
- qualquer biblioteca extra que não esteja presente/validada;
- qualquer promessa de compatibilidade total.

## Estado da documentação

Esta documentação foi construída a partir dos arquivos fornecidos do projeto. Quando um detalhe não pôde ser comprovado diretamente nesses arquivos, ele foi deixado como limite, recomendação ou observação.

## Próximas melhorias recomendadas para a documentação

1. sincronizar todas as referências de versão;
2. adicionar testes automatizados;
3. registrar uma especificação de compatibilidade por versão;
4. documentar explicitamente limitações conhecidas;
5. adicionar exemplos de entrada/saída para os principais comandos;
6. manter um changelog por release.



---

