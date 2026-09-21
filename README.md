🐍 Pyrtugues

Python em português, feito para aprender programação.

O Pyrtugues é um projeto educacional que busca facilitar os primeiros passos na programação usando uma sintaxe em português, mantendo a lógica do Python como base.

A ideia é simples:

Programar em português → entender a lógica → enxergar o Python → aprender Python.

✨ O que é o Pyrtugues?

O Pyrtugues funciona como uma ponte para quem está começando.

Em vez de:

if idade >= 12:
    print("Olá!")

você pode escrever:

se idade maior ou igual a 12:
    mostrar("Olá!")

A proposta não é criar uma linguagem com uma lógica completamente diferente, mas aproximar a escrita inicial do aluno da linguagem natural em português.

🎯 Objetivo

O projeto foi pensado para:

facilitar o primeiro contato com programação;

reduzir a barreira do inglês para iniciantes;

ensinar conceitos reais de programação;

manter a lógica e a estrutura inspiradas no Python;

servir como uma ponte para o aprendizado posterior de Python.

O Pyrtugues foi pensado especialmente para estudantes, crianças, jovens, iniciantes, escolas e oficinas de tecnologia.

💻 Versões

🖥️ Aplicativo para Windows

O projeto possui uma versão desktop feita em Python com interface gráfica.

Ela permite escrever, traduzir e executar código Pyrtugues localmente.

🌐 Editor Web

Também existe uma versão web para experimentar a linguagem diretamente no navegador:

Editor Web:
https://pyrtugues-editor.netlify.app/

A versão web usa Python no navegador através do Pyodide e possui recursos como:

editor de código;

tradução para Python;

execução de programas;

entrada interativa com pergunte();

exemplos prontos;

cópia do Python gerado;

download do código traduzido como .py.

📚 Exemplos

Olá, mundo

mostrar("Olá, mundo!")

Python:

print("Olá, mundo!")

Condição

se idade maior que 10:
    mostrar("Você pode continuar!")
senão:
    mostrar("Continue praticando!")

Python:

if idade > 10:
    print("Você pode continuar!")
else:
    print("Continue praticando!")

Repetição

para i em intervalo(1, 6):
    mostrar(i)

Python:

for i in range(1, 6):
    print(i)

Entrada de dados

nome = pergunte("Qual é o seu nome? ")
mostrar(f"Olá, {nome}!")

Python:

nome = input("Qual é o seu nome? ")
print(f"Olá, {nome}!")

🧩 Alguns comandos

Pyrtugues

Python

mostrar()

print()

pergunte()

input()

se

if

senão

else

senão se

elif

enquanto

while

para

for

em

in

função

def

retornar

return

importar

import

tentar

try

excepto

except

inteiro()

int()

decimal()

float()

texto()

str()

intervalo()

range()

tamanho()

len()

verdadeiro

True

falso

False

nulo

None

O projeto está em desenvolvimento e o conjunto de comandos suportados pode evoluir ao longo das versões.

🧠 Como funciona?

A ideia geral é:

Código em Pyrtugues
        ↓
Motor de tradução
        ↓
Código Python
        ↓
Execução

Na versão web:

Pyrtugues
    ↓
Tradutor JavaScript
    ↓
Python
    ↓
Pyodide
    ↓
Python executado no navegador

🔗 Links

Código-fonte

https://github.com/pyrtugues/Pyrtugues

Editor Web

https://pyrtugues-editor.netlify.app/

Perfil do GitHub

https://github.com/pyrtugues

Downloads

Os executáveis e outras versões podem ser publicados na área de Releases deste repositório.

🚀 Como usar o repositório

Clone o projeto:

git clone https://github.com/pyrtugues/Pyrtugues.git

Entre na pasta:

cd Pyrtugues

A estrutura do projeto pode incluir:

Pyrtugues/
├── README.md
├── index.html
├── Pyrtugues_code.py
├── assets/
└── ...

🛠️ Desenvolvimento

O Pyrtugues possui diferentes partes que podem evoluir separadamente:

                 PYRTUGUES
                     │
        ┌────────────┴────────────┐
        ↓                         ↓
     Desktop                    Web
        ↓                         ↓
 Python + GUI              HTML/CSS/JS
                                  ↓
                               Pyodide

Uma das metas de desenvolvimento é manter a linguagem consistente entre as diferentes versões.

🌱 Projeto em evolução

O Pyrtugues ainda está em desenvolvimento.

Isso significa que novos comandos, exemplos, correções, melhorias de tradução, interface e materiais educacionais podem ser adicionados ao longo do tempo.

Sugestões, testes e contribuições são bem-vindos.

🤝 Contribuindo

Você pode ajudar de várias formas:

testar exemplos;

encontrar bugs;

sugerir comandos;

melhorar a documentação;

criar exemplos educacionais;

contribuir com código.

Antes de adicionar uma nova tradução, é importante verificar se ela não interfere em:

nomes de variáveis;

strings;

comentários;

f-strings;

expressões Python;

código já suportado.

🔍 Encontrando o Pyrtugues na web

Para facilitar a descoberta do projeto, os principais lugares devem usar o mesmo nome e identidade:

Pyrtugues
github.com/pyrtugues
github.com/pyrtugues/Pyrtugues
pyrtugues-editor.netlify.app

Também é importante manter links entre o site, o editor web e o repositório.

📄 Licença

Este projeto é open-source.

Consulte o arquivo LICENSE do repositório para ver os termos completos de uso e distribuição.

👨‍💻 Criador

Vinicius Caracciolo

O Pyrtugues nasceu como um projeto pessoal de programação e educação, com a ideia de tornar o primeiro contato com código mais acessível em português.

⭐ Apoie o projeto

Você pode apoiar o projeto:

usando e testando o Pyrtugues;

compartilhando o repositório;

encontrando bugs;

sugerindo melhorias;

contribuindo com documentação e código.

💚 Pyrtugues

Programação em português.
Lógica de verdade.
Uma ponte para o Python.
