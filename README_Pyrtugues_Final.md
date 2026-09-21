# 🐍 Pyrtugues

> **Python em português, feito para aprender programação.**

O **Pyrtugues** é um projeto educacional criado para facilitar o primeiro contato com programação usando uma sintaxe em português, mantendo a **lógica do Python como base**.

A ideia do projeto é:

**Programar em português → entender a lógica → enxergar o Python → aprender Python.**

---

## 🌐 Links oficiais

### Site do Pyrtugues
**https://pyrtugues.netlify.app/**

Apresentação do projeto, explicação de como ele funciona, informações sobre o criador, download e outros materiais.

### Editor Web
**https://pyrtugues-editor.netlify.app/**

Editor online para escrever código em Pyrtugues e experimentar a linguagem diretamente no navegador.

### GitHub
**https://github.com/pyrtugues/Pyrtugues**

Código-fonte, versões e arquivos do projeto.

### Perfil do projeto no GitHub
**https://github.com/pyrtugues**

---

## ✨ O que é o Pyrtugues?

O Pyrtugues funciona como uma ponte entre português e Python.

Por exemplo:

```python
se idade maior ou igual a 12:
    mostrar("Olá!")
```

é traduzido para Python como:

```python
if idade >= 12:
    print("Olá!")
```

A proposta é manter os conceitos de programação próximos do Python, mas deixar a escrita inicial mais natural para quem fala português.

---

## 🎯 Objetivo

O projeto foi criado para:

- facilitar o primeiro contato com programação;
- diminuir a barreira do inglês para iniciantes;
- ensinar lógica de programação com conceitos reais;
- aproximar o estudante do Python;
- servir como material de apoio para estudantes, iniciantes e ambientes educacionais.

O Pyrtugues não pretende substituir o Python. A ideia é funcionar como uma **ponte para o aprendizado de Python**.

---

## 🖥️ Versão para Windows

O projeto possui uma versão desktop desenvolvida em **Python + CustomTkinter**.

Ela permite escrever e executar programas usando a sintaxe do Pyrtugues.

O projeto também possui uma versão distribuída como **`.exe`** para Windows.

### Download

A versão publicada no repositório possui a release:

**v1.0.0**

Download direto:

https://github.com/pyrtugues/Pyrtugues/releases/download/v1.2.0/Pyrtugues_v.1.2.0.exe

As outras versões podem ser encontradas em:

https://github.com/pyrtugues/Pyrtugues/releases

---

## 🌐 Editor Web

O projeto também possui um editor que funciona no navegador:

**https://pyrtugues-editor.netlify.app/**

A versão web utiliza tecnologias web e **Pyodide** para executar Python no navegador.

Entre os recursos presentes no editor estão:

- editor de código;
- tradução de Pyrtugues para Python;
- execução no navegador;
- entrada interativa com `pergunte()`;
- exemplos prontos;
- saída no terminal;
- cópia do Python gerado;
- download do código Python como `.py`;
- execução isolada do motor em Web Worker.

---

## 📚 Exemplos

### 👋 Olá, mundo

Pyrtugues:

```python
mostrar("Olá, mundo!")
```

Python:

```python
print("Olá, mundo!")
```

### 🔀 Condição

Pyrtugues:

```python
se idade maior que 10:
    mostrar("Você pode continuar!")
senão:
    mostrar("Continue praticando!")
```

Python:

```python
if idade > 10:
    print("Você pode continuar!")
else:
    print("Continue praticando!")
```

### 🔁 Repetição

Pyrtugues:

```python
para i em intervalo(1, 6):
    mostrar(i)
```

Python:

```python
for i in range(1, 6):
    print(i)
```

### ⌨️ Entrada

Pyrtugues:

```python
nome = pergunte("Qual é o seu nome? ")
mostrar(f"Olá, {nome}!")
```

Python:

```python
nome = input("Qual é o seu nome? ")
print(f"Olá, {nome}!")
```

### 🧮 Calculadora

Pyrtugues:

```python
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

### 🔢 Tabuada

Pyrtugues:

```python
numero = inteiro(pergunte("Ver tabuada de qual número? "))

para i em intervalo(1, 11):
    mostrar(f"{numero} x {i} = {numero * i}")
```

---

## 🧩 Alguns comandos

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
| `quebrar` | `break` |
| `continuar` | `continue` |
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

> A linguagem e o conjunto de comandos continuam em desenvolvimento e podem receber novos recursos nas próximas versões.

---

## 🧠 Como funciona?

A arquitetura básica é:

```text
Código em Pyrtugues
        ↓
Motor de tradução
        ↓
Código Python
        ↓
Execução
```

Na versão Web:

```text
Pyrtugues
    ↓
Tradutor
    ↓
Python
    ↓
Pyodide
    ↓
Python executado no navegador
```

A proposta é que o estudante consiga visualizar a relação entre o que escreve em português e o Python equivalente.

---

## 🛠️ Tecnologias

### Desktop

- Python
- CustomTkinter
- Tkinter

### Web

- HTML
- CSS
- JavaScript
- Tailwind CSS
- Font Awesome
- Pyodide
- Web Worker

---

## 📂 Estrutura do projeto

A estrutura pode variar conforme a versão, mas o repositório contém as diferentes partes do projeto, por exemplo:

```text
Pyrtugues/
├── README.md
├── LICENSE
├── index.html
├── Pyrtugues_code.py
├── assets/
└── ...
```

---

## 🚀 Começando pelo GitHub

Clone o repositório:

```bash
git clone https://github.com/pyrtugues/Pyrtugues.git
```

Entre na pasta:

```bash
cd Pyrtugues
```

Depois, consulte os arquivos e o README da versão atual para saber como executar cada parte.

---

## 🔄 Desenvolvimento

O Pyrtugues possui atualmente duas frentes principais:

```text
                 PYRTUGUES
                     │
        ┌────────────┴────────────┐
        ↓                         ↓
     Desktop                    Web
        ↓                         ↓
 Python + GUI              HTML/CSS/JS
                                  ↓
                               Pyodide
```

A ideia é manter a linguagem e os conceitos consistentes entre as diferentes versões.

---

## 🌱 Projeto em desenvolvimento

O Pyrtugues continua sendo desenvolvido.

Entre as áreas que podem evoluir estão:

- novos comandos;
- melhorias no tradutor;
- suporte a mais recursos do Python;
- mensagens de erro mais amigáveis;
- melhorias no editor;
- novos exemplos;
- materiais educacionais;
- versão mobile;
- documentação.

---

## 🤝 Contribuindo

Você pode contribuir com o projeto de várias formas:

- testando exemplos;
- encontrando e reportando bugs;
- sugerindo novos comandos;
- melhorando a documentação;
- criando exemplos;
- contribuindo com código.

Ao modificar o tradutor, é importante verificar se a alteração não interfere em:

- nomes de variáveis;
- strings;
- comentários;
- f-strings;
- expressões;
- código já suportado.

---

## 🔎 Onde encontrar o Pyrtugues

Os principais endereços oficiais do projeto são:

```text
Site:
https://pyrtugues.netlify.app/

Editor:
https://pyrtugues-editor.netlify.app/

GitHub:
https://github.com/pyrtugues/Pyrtugues

Perfil:
https://github.com/pyrtugues
```

Manter esses endereços conectados ajuda quem encontra o projeto a chegar rapidamente ao site, ao editor e ao código-fonte.

---

## 📄 Licença

O projeto é open-source.

Consulte o arquivo `LICENSE` deste repositório para conhecer os termos completos de uso, cópia e distribuição.

---

## 👨‍💻 Criador

**Vinicius Caracciolo**

O Pyrtugues foi criado como um projeto pessoal voltado para programação e educação, com a ideia de tornar o primeiro contato com código mais acessível para quem fala português.

O projeto foi iniciado quando Vinicius tinha 12 anos.

---

## ⭐ Apoie o projeto

Você pode ajudar o Pyrtugues:

- usando o projeto;
- testando o editor;
- compartilhando o site;
- compartilhando o GitHub;
- encontrando bugs;
- enviando sugestões;
- contribuindo com código ou documentação.

---

## 💚 Pyrtugues

**Programação em português.  
Lógica de verdade.  
Uma ponte para o Python.**
