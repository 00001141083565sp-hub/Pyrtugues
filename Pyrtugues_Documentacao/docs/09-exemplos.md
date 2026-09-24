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
