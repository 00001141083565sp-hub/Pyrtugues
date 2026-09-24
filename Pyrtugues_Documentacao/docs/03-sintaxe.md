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
