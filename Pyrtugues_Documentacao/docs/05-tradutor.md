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
