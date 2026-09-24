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
