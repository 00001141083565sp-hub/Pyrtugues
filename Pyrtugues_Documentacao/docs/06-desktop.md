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
