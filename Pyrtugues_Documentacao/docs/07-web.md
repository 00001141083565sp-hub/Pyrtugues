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
