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
