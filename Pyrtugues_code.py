import re
import customtkinter as ctk
from tkinter import messagebox
import sys
TRADUCAO = {
    "portugues": {
        "senão se": "elif",
        "senãose": "elif",
        "senão": "else",
        "enquanto verdadeiro": "while True",
        "enquanto": "while",
        "para cada": "for",
        "para": "for",
        "se": "if",
        "em": "in",
        "quebrar": "break",
        "continuar": "continue",
        "passar": "pass",
        "com": "with",
        "como": "as",
        "finalmente": "finally",

        "função": "def",
        "classe": "class",
        "retornar verdadeiro": "return True",
        "retornar falso": "return False",
        "retornar nulo": "return None",
        "retornar": "return",
        "produzir": "yield",
        "assíncrono": "async",
        "aguardar": "await",

        "importar": "import",
        "de": "from",

        "tentar": "try",
        "excepto": "except",
        "levantar": "raise",
        "afirmar": "assert",
        "verificar": "assert",
        "lançar": "raise",

        "global": "global",
        "nãolocal": "nonlocal",

        "verdadeiro": "True",
        "falso": "False",
        "nulo": "None",
        "vazio": "pass",
        "nada": "None",

        "e também": "and",
        "ou então": "or",
        "não é": "is not",
        "é": "is",
        "não": "not",
        "e": "and",
        "ou": "or",

        "maior ou igual a": ">=",
        "menor ou igual a": "<=",
        "maior ou igual": ">=",
        "menor ou igual": "<=",
        "maior que": ">",
        "menor que": "<",
        "diferente de": "!=",
        "igual a": "==",
        "fora de": "not in",
        "dentro de": "in",

        "mais": "+",
        "menos": "-",
        "vezes": "*",
        "dividido por": "/",
        "resto": "%",
        "potência": "**",
        "elevado a": "**",

        "inteiro": "int",
        "decimal": "float",
        "texto": "str",
        "booleano": "bool",
        "lista": "list",
        "dicionário": "dict",
        "tupla": "tuple",
        "conjunto": "set",

        "mostrar": "print",
        "imprimir": "print",
        "pergunte": "input",
        "pergunta": "input",
        "intervalo": "range",
        "tamanho": "len",
        "comprimento": "len",
        "tipo": "type",
        "é instância": "isinstance",
        "é subclasse": "issubclass",

        "somar": "sum",
        "máximo": "max",
        "mínimo": "min",
        "ordenar": "sorted",
        "inverter": "reversed",
        "filtrar": "filter",
        "mapear": "map",
        "zipar": "zip",
        "enumerar": "enumerate",
        "todos": "all",
        "algum": "any",

        "absoluto": "abs",
        "arredondar": "round",
        "elevar": "pow",
        "hexadecimal": "hex",
        "octal": "oct",
        "binário": "bin",
        "ordinal": "ord",
        "caractere": "chr",

        "ajuda": "help",
        "atributos": "vars",
        "abrir": "open",
        "formatar": "format",
        "representar": "repr",

        "maiúsculas": "upper",
        "minúsculas": "lower",
        "capitalizar": "capitalize",
        "título": "title",
        "trocar": "replace",
        "dividir": "split",
        "juntar": "join",
        "tirar espaços": "strip",
        "começa com": "startswith",
        "termina com": "endswith",
        "encontrar": "find",
        "contar": "count",
        "é dígito": "isdigit",
        "é letra": "isalpha",
        "é espaço": "isspace",

        "adicionar": "append",
        "estender": "extend",
        "inserir": "insert",
        "remover": "remove",
        "tirar": "pop",
        "limpar": "clear",
        "copiar": "copy",
        "índice": "index",
        "ordenar em ordem": "sort",
        "inverter ordem": "reverse",

        "chaves": "keys",
        "valores": "values",
        "itens": "items",
        "pegar": "get",
        "atualizar": "update",

        "matemática": "math",
        "aleatório": "random",
        "data e hora": "datetime",
        "tempo": "time",
        "sistema": "os",
        "caminho": "path",
        "arquivo": "file",
        "requisição": "request",
        "resposta": "response",
        "expressão regular": "re",

        "mais igual": "+=",
        "menos igual": "-=",
        "vezes igual": "*=",
        "dividido igual": "/=",
        "resto igual": "%=",
        "potência igual": "**=",

        "retornar verdadeiro": "return True",
        "retornar falso": "return False",
        "retornar nulo": "return None",
        "sair": "exit",
        "parar": "stop",
        "iniciar": "start",
    },
    "espanhol": {
        "sino si": "elif",
        "sinosi": "elif",
        "sino": "else",
        "mientras verdadero": "while True",
        "mientras": "while",
        "para cada": "for",
        "para": "for",
        "si": "if",
        "en": "in",
        "romper": "break",
        "continuar": "continue",
        "pasar": "pass",
        "con": "with",
        "como": "as",
        "finalmente": "finally",

        "función": "def",
        "clase": "class",
        "devolver verdadero": "return True",
        "devolver falso": "return False",
        "devolver nulo": "return None",
        "devolver": "return",
        "producir": "yield",
        "asíncrono": "async",
        "esperar": "await",

        "importar": "import",
        "de": "from",

        "intentar": "try",
        "excepto": "except",
        "levantar": "raise",
        "afirmar": "assert",
        "verificar": "assert",
        "lanzar": "raise",

        "global": "global",
        "nolocal": "nonlocal",

        "verdadero": "True",
        "falso": "False",
        "nulo": "None",
        "vacío": "pass",
        "nada": "None",

        "y también": "and",
        "o entonces": "or",
        "no es": "is not",
        "es instancia": "isinstance",
        "es subclase": "issubclass",
        "es": "is",
        "no": "not",
        "y": "and",
        "o": "or",

        "mayor o igual a": ">=",
        "menor o igual a": "<=",
        "mayor o igual": ">=",
        "menor o igual": "<=",
        "mayor que": ">",
        "menor que": "<",
        "diferente de": "!=",
        "igual a": "==",
        "fuera de": "not in",
        "dentro de": "in",

        "más igual a": "+=",
        "menos igual a": "-=",
        "veces igual a": "*=",
        "dividido igual a": "/=",
        "resto igual a": "%=",
        "potencia igual a": "**=",

        "más igual": "+=",
        "menos igual": "-=",
        "veces igual": "*=",
        "dividido igual": "/=",
        "resto igual": "%=",
        "potencia igual": "**=",

        "más": "+",
        "menos": "-",
        "veces": "*",
        "dividido por": "/",
        "resto": "%",
        "potencia": "**",
        "elevado a": "**",

        "entero": "int",
        "decimal": "float",
        "texto": "str",
        "booleano": "bool",
        "lista": "list",
        "diccionario": "dict",
        "tupla": "tuple",
        "conjunto": "set",

        "mostrar": "print",
        "imprimir": "print",
        "pregunte": "input",
        "pregunta": "input",
        "intervalo": "range",
        "tamaño": "len",
        "longitud": "len",
        "tipo": "type",

        "sumar": "sum",
        "máximo": "max",
        "mínimo": "min",
        "ordenar": "sorted",
        "invertir": "reversed",
        "filtrar": "filter",
        "mapear": "map",
        "comprimir": "zip",
        "enumerar": "enumerate",
        "todos": "all",
        "algún": "any",

        "absoluto": "abs",
        "redondear": "round",
        "elevar": "pow",
        "hexadecimal": "hex",
        "octal": "oct",
        "binario": "bin",
        "ordinal": "ord",
        "carácter": "chr",

        "ayuda": "help",
        "atributos": "vars",
        "abrir": "open",
        "formatear": "format",
        "representar": "repr",

        "mayúsculas": "upper",
        "minúsculas": "lower",
        "capitalizar": "capitalize",
        "título": "title",
        "cambiar": "replace",
        "dividir": "split",
        "unir": "join",
        "quitar espacios": "strip",
        "comienza con": "startswith",
        "termina con": "endswith",
        "encontrar": "find",
        "contar": "count",
        "es dígito": "isdigit",
        "es letra": "isalpha",
        "es espacio": "isspace",

        "agregar": "append",
        "extender": "extend",
        "insertar": "insert",
        "eliminar": "remove",
        "sacar": "pop",
        "limpiar": "clear",
        "copiar": "copy",
        "índice": "index",
        "ordenar en orden": "sort",
        "invertir orden": "reverse",

        "claves": "keys",
        "valores": "values",
        "elementos": "items",
        "obtener": "get",
        "actualizar": "update",

        "matemáticas": "math",
        "aleatorio": "random",
        "fecha y hora": "datetime",
        "tiempo": "time",
        "sistema": "os",
        "ruta": "path",
        "archivo": "file",
        "solicitud": "request",
        "respuesta": "response",
        "expresión regular": "re",

        "salir": "exit",
        "parar": "stop",
        "iniciar": "start",
}
}


def proteger_strings(codigo):
    strings = []
    
    def capturar(match):
        strings.append(match.group(0))
        return f"__STR_{len(strings)-1}__"
    
    codigo = re.sub(r'(?<!f)"[^"]*"|(?<!f)\'[^\']*\'', capturar, codigo)
    return codigo, strings


def restaurar_strings(codigo, strings):
    for i, s in enumerate(strings):
        codigo = codigo.replace(f"__STR_{i}__", s)
    return codigo


def traduzir_fstrings(codigo):
    def traduzir_expressao(match):
        expressao = match.group(1)
        for br, py in sorted(TRADUCAO.items(), key=lambda x: -len(x[0])):
            expressao = re.sub(
                rf'\b{re.escape(br)}\b',
                py,
                expressao,
                flags=re.IGNORECASE
            )
        return "{" + expressao + "}"
    
    codigo = re.sub(
        r'f"([^"]*)"',
        lambda m: 'f"' + re.sub(r'\{([^}]*)\}', traduzir_expressao, m.group(1)) + '"',
        codigo
    )
    codigo = re.sub(
        r"f'([^']*)'",
        lambda m: "f'" + re.sub(r'\{([^}]*)\}', traduzir_expressao, m.group(1)) + "'",
        codigo
    )
    return codigo


def traduzir(codigo_br):
    # 1. Protege strings primeiro
    codigo_protegido, strings = proteger_strings(codigo_br)

    # 2. Traduz somente o código fora das strings
    for br, py in sorted(TRADUCAO.items(), key=lambda x: -len(x[0])):
        codigo_protegido = re.sub(
            rf'\b{re.escape(br)}\b',
            py,
            codigo_protegido,
            flags=re.IGNORECASE
        )

    # 3. Restaura as strings originais
    return restaurar_strings(codigo_protegido, strings)


class JanelaBR(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("🐍 Python BR")
        self.geometry("1100x760")
        self.minsize(900, 650)
        ctk.set_appearance_mode("Dark")

        self.namespace = {}

        # ===== Visual =====
        self.configure(fg_color="#0B0F19")

        topo = ctk.CTkFrame(
            self, height=72, corner_radius=0,
            fg_color="#111827"
        )
        topo.pack(fill="x")
        topo.pack_propagate(False)

        marca = ctk.CTkFrame(topo, fg_color="transparent")
        marca.pack(side="left", padx=24)

        ctk.CTkLabel(
            marca,
            text="🐍",
            font=("Segoe UI Emoji", 28)
        ).pack(side="left", padx=(0, 10))

        textos = ctk.CTkFrame(marca, fg_color="transparent")
        textos.pack(side="left")

        ctk.CTkLabel(
            textos,
            text="Python BR",
            font=("Segoe UI", 22, "bold"),
            text_color="#F8FAFC"
        ).pack(anchor="w")

        ctk.CTkLabel(
            textos,
            text="Programação em português",
            font=("Segoe UI", 11),
            text_color="#94A3B8"
        ).pack(anchor="w")

        ctk.CTkButton(
            topo,
            text="ⓘ  Sobre / Como usar",
            command=self.abrir_sobre,
            fg_color="#151D2E",
            hover_color="#1E293B",
            border_width=1,
            border_color="#263247",
            text_color="#CBD5E1",
            font=("Segoe UI", 11, "bold"),
            height=34,
            width=170,
            corner_radius=8
        ).pack(side="right", padx=(8, 16))

        ctk.CTkLabel(
            topo,
            text="PYTHON • BR",
            font=("Consolas", 10, "bold"),
            text_color="#64748B"
        ).pack(side="right", padx=8)

        # ===== Área principal =====
        conteudo = ctk.CTkFrame(self, fg_color="transparent")
        conteudo.pack(fill="both", expand=True, padx=20, pady=18)

        editor_top = ctk.CTkFrame(
            conteudo, fg_color="transparent", height=36
        )
        editor_top.pack(fill="x")
        editor_top.pack_propagate(False)

        ctk.CTkLabel(
            editor_top,
            text="📝  Seu código",
            font=("Segoe UI", 15, "bold"),
            text_color="#F8FAFC"
        ).pack(side="left")

        ctk.CTkLabel(
            editor_top,
            text="Ctrl + Enter para executar",
            font=("Segoe UI", 10),
            text_color="#64748B"
        ).pack(side="right")

        # ===== Editor (estilo VS Code) =====
        editor_frame = ctk.CTkFrame(
            conteudo,
            fg_color="#111827",
            corner_radius=12,
            border_width=1,
            border_color="#263247"
        )
        editor_frame.pack(fill="both", expand=True, pady=(0, 12))

        editor_frame.grid_rowconfigure(0, weight=1)
        editor_frame.grid_columnconfigure(1, weight=1)

        # Números de linha
        self.numeros_linha = ctk.CTkTextbox(
            editor_frame,
            width=52,
            font=("Consolas", 14),
            fg_color="#090E18",
            text_color="#64748B",
            border_width=0,
            corner_radius=0,
            wrap="none",
            activate_scrollbars=False
        )
        self.numeros_linha.grid(
            row=0, column=0, sticky="ns",
            padx=(6, 0), pady=2
        )
        self.numeros_linha.configure(state="disabled")

        # Código
        self.caixa_codigo = ctk.CTkTextbox(
            editor_frame,
            font=("Consolas", 14),
            fg_color="#0D1421",
            text_color="#E2E8F0",
            border_width=0,
            corner_radius=10,
            wrap="none",
            padx=16,
            pady=14,
            undo=True
        )
        self.caixa_codigo.grid(
            row=0, column=1, sticky="nsew",
            padx=(0, 2), pady=2
        )

        # Atualiza números conforme o usuário digita e rola
        self.caixa_codigo.bind("<KeyRelease>", self.atualizar_numeros_linha)
        self.caixa_codigo.bind("<MouseWheel>", self.sincronizar_numeros_linha)
        self.caixa_codigo.bind("<Button-4>", self.sincronizar_numeros_linha)
        self.caixa_codigo.bind("<Button-5>", self.sincronizar_numeros_linha)

        self.carregar_exemplo()

        # ===== Botões =====
        botoes = ctk.CTkFrame(
            conteudo, fg_color="transparent", height=48
        )
        botoes.pack(fill="x", pady=(0, 14))
        botoes.pack_propagate(False)

        ctk.CTkButton(
            botoes,
            text="▶  Executar",
            command=self.executar_codigo,
            fg_color="#22C55E",
            hover_color="#16A34A",
            text_color="#052E16",
            font=("Segoe UI", 13, "bold"),
            height=42,
            width=145,
            corner_radius=9
        ).pack(side="left", padx=(0, 8))

        ctk.CTkButton(
            botoes,
            text="💡  Exemplo",
            command=self.carregar_exemplo,
            fg_color="#151D2E",
            hover_color="#1E293B",
            border_width=1,
            border_color="#263247",
            text_color="#F8FAFC",
            font=("Segoe UI", 12, "bold"),
            height=42,
            width=120,
            corner_radius=9
        ).pack(side="left", padx=8)

        ctk.CTkButton(
            botoes,
            text="🗑  Limpar saída",
            command=lambda: self.caixa_saida.delete("1.0", "end"),
            fg_color="#151D2E",
            hover_color="#1E293B",
            border_width=1,
            border_color="#263247",
            text_color="#F8FAFC",
            font=("Segoe UI", 12),
            height=42,
            width=135,
            corner_radius=9
        ).pack(side="left", padx=8)

        # ===== Saída =====
        saida_top = ctk.CTkFrame(
            conteudo, fg_color="transparent", height=34
        )
        saida_top.pack(fill="x")
        saida_top.pack_propagate(False)

        ctk.CTkLabel(
            saida_top,
            text="📤  Saída",
            font=("Segoe UI", 15, "bold"),
            text_color="#F8FAFC"
        ).pack(side="left")

        ctk.CTkLabel(
            saida_top,
            text="Terminal",
            font=("Consolas", 10),
            text_color="#64748B"
        ).pack(side="right")

        saida_frame = ctk.CTkFrame(
            conteudo,
            fg_color="#111827",
            corner_radius=12,
            border_width=1,
            border_color="#263247",
            height=175
        )
        saida_frame.pack(fill="x")
        saida_frame.pack_propagate(False)

        self.caixa_saida = ctk.CTkTextbox(
            saida_frame,
            height=165,
            font=("Consolas", 12),
            fg_color="#070B12",
            border_width=0,
            corner_radius=10,
            text_color="#86EFAC",
            wrap="none",
            padx=14,
            pady=12
        )
        self.caixa_saida.pack(fill="both", expand=True, padx=2, pady=2)

        self.bind("<Control-Return>", lambda e: self.executar_codigo())

    def atualizar_numeros_linha(self, event=None):
        """Atualiza os números de linha do editor."""
        total = int(self.caixa_codigo.index("end-1c").split(".")[0])
        numeros = "\n".join(str(i) for i in range(1, total + 1))

        self.numeros_linha.configure(state="normal")
        self.numeros_linha.delete("1.0", "end")
        self.numeros_linha.insert("1.0", numeros)
        self.numeros_linha.configure(state="disabled")

        self.sincronizar_numeros_linha()

    def sincronizar_numeros_linha(self, event=None):
        """Mantém os números alinhados com a rolagem do código."""
        try:
            self.numeros_linha.yview_moveto(self.caixa_codigo.yview()[0])
        except Exception:
            pass

    # ===== Backend original =====

    def input_gui(self, prompt=""):
        janela = ctk.CTkToplevel(self)
        janela.title("Entrada")
        janela.geometry("400x160")
        janela.grab_set()

        resultado = [""]

        ctk.CTkLabel(janela, text=prompt, font=("Segoe UI", 13)).pack(pady=15, padx=20)

        entrada = ctk.CTkEntry(janela, width=320, font=("Consolas", 13))
        entrada.pack(pady=5, padx=20)
        entrada.focus()

        def confirmar(event=None):
            resultado[0] = entrada.get()
            janela.destroy()

        entrada.bind("<Return>", confirmar)

        ctk.CTkButton(
            janela, text="OK", command=confirmar,
            fg_color="#10B981", font=("Segoe UI", 12, "bold")
        ).pack(pady=10)

        self.wait_window(janela)
        return resultado[0]

    def abrir_sobre(self):
        """Abre a central de informações do Python BR."""
        janela = ctk.CTkToplevel(self)
        janela.title("Sobre o Python BR")
        janela.geometry("760x620")
        janela.minsize(680, 540)
        janela.configure(fg_color="#0B0F19")
        janela.transient(self)
        janela.grab_set()

        # Cabeçalho
        cabecalho = ctk.CTkFrame(janela, fg_color="#111827", corner_radius=0, height=86)
        cabecalho.pack(fill="x")
        cabecalho.pack_propagate(False)

        marca = ctk.CTkFrame(cabecalho, fg_color="transparent")
        marca.pack(side="left", padx=24, pady=14)

        ctk.CTkLabel(
            marca, text="🐍", font=("Segoe UI Emoji", 30)
        ).pack(side="left", padx=(0, 12))

        textos = ctk.CTkFrame(marca, fg_color="transparent")
        textos.pack(side="left")

        ctk.CTkLabel(
            textos, text="Python BR", font=("Segoe UI", 21, "bold"),
            text_color="#F8FAFC"
        ).pack(anchor="w")
        ctk.CTkLabel(
            textos, text="Programação em português", font=("Segoe UI", 10),
            text_color="#94A3B8"
        ).pack(anchor="w")

        # Abas
        abas = ctk.CTkTabview(
            janela,
            fg_color="#0B0F19",
            segmented_button_fg_color="#111827",
            segmented_button_selected_color="#2563EB",
            segmented_button_selected_hover_color="#1D4ED8",
            segmented_button_unselected_color="#151D2E",
            segmented_button_unselected_hover_color="#1E293B",
            text_color="#F8FAFC"
        )
        abas.pack(fill="both", expand=True, padx=18, pady=18)

        aba_sobre = abas.add("🐍 Sobre o projeto")
        aba_criador = abas.add("👨‍💻 Sobre o criador")
        aba_usar = abas.add("📖 Como usar")

        def criar_scroll(aba):
            scroll = ctk.CTkScrollableFrame(
                aba, fg_color="transparent", corner_radius=0
            )
            scroll.pack(fill="both", expand=True, padx=8, pady=8)
            return scroll

        # ===== Sobre o projeto =====
        frame = criar_scroll(aba_sobre)
        ctk.CTkLabel(
            frame, text="Uma ponte para aprender Python", anchor="w",
            font=("Segoe UI", 20, "bold"), text_color="#F8FAFC"
        ).pack(fill="x", pady=(4, 8))
        ctk.CTkLabel(
            frame,
            text=(
                "O Python BR é um projeto educacional que permite escrever código "
                "usando palavras em português e executar o resultado com Python.\n\n"
                "A ideia é facilitar o primeiro contato com programação sem mudar a "
                "lógica que o aluno vai encontrar no Python tradicional."
            ),
            anchor="w", justify="left", wraplength=620,
            font=("Segoe UI", 13), text_color="#CBD5E1"
        ).pack(fill="x", pady=(0, 18))

        exemplo = ctk.CTkFrame(
            frame, fg_color="#0D1421", corner_radius=10,
            border_width=1, border_color="#263247"
        )
        exemplo.pack(fill="x", pady=(0, 18))
        ctk.CTkLabel(
            exemplo, text="Python BR", font=("Consolas", 11, "bold"),
            text_color="#60A5FA", anchor="w"
        ).pack(fill="x", padx=14, pady=(12, 4))
        ctk.CTkLabel(
            exemplo, text='se idade maior que 10:\n    mostrar("Olá!")',
            font=("Consolas", 13), text_color="#E2E8F0", anchor="w", justify="left"
        ).pack(fill="x", padx=14, pady=(0, 10))
        ctk.CTkLabel(
            exemplo, text="↓  mesma lógica em Python", font=("Segoe UI", 10),
            text_color="#64748B", anchor="w"
        ).pack(fill="x", padx=14, pady=(0, 4))
        ctk.CTkLabel(
            exemplo, text='if idade > 10:\n    print("Olá!")',
            font=("Consolas", 13), text_color="#A7F3D0", anchor="w", justify="left"
        ).pack(fill="x", padx=14, pady=(0, 12))

        ctk.CTkLabel(
            frame,
            text="O objetivo é aprender a lógica primeiro e tornar a passagem para o Python tradicional mais natural.",
            anchor="w", justify="left", wraplength=620,
            font=("Segoe UI", 12), text_color="#94A3B8"
        ).pack(fill="x")

        # ===== Sobre o criador =====
        frame = criar_scroll(aba_criador)
        ctk.CTkLabel(
            frame, text="Sobre o criador", anchor="w",
            font=("Segoe UI", 20, "bold"), text_color="#F8FAFC"
        ).pack(fill="x", pady=(4, 12))
        ctk.CTkLabel(
            frame,
            text=(
                "Olá! Eu sou o criador do Python BR.\n\n"
                "Comecei este projeto com a ideia de tornar a programação mais acessível "
                "para quem está começando, especialmente estudantes e crianças.\n\n"
                "A proposta é simples: usar o português para diminuir a barreira inicial, "
                "mas manter a lógica e os conceitos do Python. Assim, o que é aprendido "
                "aqui pode servir de base para aprender Python depois."
            ),
            anchor="w", justify="left", wraplength=620,
            font=("Segoe UI", 13), text_color="#CBD5E1"
        ).pack(fill="x", pady=(0, 18))

        destaque = ctk.CTkFrame(frame, fg_color="#111827", corner_radius=10)
        destaque.pack(fill="x")
        ctk.CTkLabel(
            destaque, text="💡 Por que o projeto existe?",
            font=("Segoe UI", 13, "bold"), text_color="#F8FAFC", anchor="w"
        ).pack(fill="x", padx=16, pady=(14, 6))
        ctk.CTkLabel(
            destaque,
            text="Para aproximar o aluno da programação e mostrar que código pode ser entendido passo a passo.",
            font=("Segoe UI", 12), text_color="#94A3B8", anchor="w", justify="left", wraplength=580
        ).pack(fill="x", padx=16, pady=(0, 14))

        ctk.CTkLabel(
            frame,
            text="Nome do criador: Vinicius caracciolo dos santos.",
            font=("Segoe UI", 10), text_color="#64748B", anchor="w"
        ).pack(fill="x", pady=(16, 0))

        # ===== Como usar =====
        frame = criar_scroll(aba_usar)
        ctk.CTkLabel(
            frame, text="Começando no Python BR", anchor="w",
            font=("Segoe UI", 20, "bold"), text_color="#F8FAFC"
        ).pack(fill="x", pady=(4, 14))

        passos = [
            ("1", "Escreva", "Digite seu programa no editor de código."),
            ("2", "Execute", "Clique em ▶ Executar ou pressione Ctrl + Enter."),
            ("3", "Veja a saída", "O resultado do programa aparece no painel de saída."),
            ("4", "Experimente", "Use o botão 💡 Exemplo para carregar um programa pronto."),
        ]
        for numero, titulo, descricao in passos:
            card = ctk.CTkFrame(frame, fg_color="#111827", corner_radius=10)
            card.pack(fill="x", pady=5)
            ctk.CTkLabel(
                card, text=numero, width=32, height=32,
                corner_radius=16, fg_color="#2563EB",
                text_color="#FFFFFF", font=("Segoe UI", 12, "bold")
            ).pack(side="left", padx=(12, 10), pady=12)
            bloco = ctk.CTkFrame(card, fg_color="transparent")
            bloco.pack(side="left", fill="x", expand=True, padx=(0, 12), pady=9)
            ctk.CTkLabel(
                bloco, text=titulo, font=("Segoe UI", 12, "bold"),
                text_color="#F8FAFC", anchor="w"
            ).pack(fill="x")
            ctk.CTkLabel(
                bloco, text=descricao, font=("Segoe UI", 10),
                text_color="#94A3B8", anchor="w", justify="left"
            ).pack(fill="x")

        ctk.CTkLabel(
            frame, text="Comandos básicos", font=("Segoe UI", 15, "bold"),
            text_color="#F8FAFC", anchor="w"
        ).pack(fill="x", pady=(22, 8))

        comandos = [
            ("mostrar(...)" , "Mostra uma informação na saída."),
            ("pergunte(...)" , "Pede uma informação ao usuário."),
            ("se ...:" , "Executa um bloco quando uma condição é verdadeira."),
            ("enquanto ...:" , "Repete um bloco enquanto uma condição for verdadeira."),
            ("função ...:" , "Cria uma função."),
        ]
        for comando, descricao in comandos:
            linha = ctk.CTkFrame(frame, fg_color="#0D1421", corner_radius=8)
            linha.pack(fill="x", pady=3)
            ctk.CTkLabel(
                linha, text=comando, width=190, anchor="w",
                font=("Consolas", 11, "bold"), text_color="#A7F3D0"
            ).pack(side="left", padx=12, pady=10)
            ctk.CTkLabel(
                linha, text=descricao, anchor="w", justify="left",
                font=("Segoe UI", 10), text_color="#94A3B8"
            ).pack(side="left", fill="x", expand=True, padx=(0, 12), pady=10)

        ctk.CTkButton(
            janela, text="Fechar", command=janela.destroy,
            fg_color="#2563EB", hover_color="#1D4ED8",
            font=("Segoe UI", 12, "bold"), height=38,
            width=110, corner_radius=8
        ).pack(pady=(0, 16))

    def executar_codigo(self):
        codigo_br = self.caixa_codigo.get("1.0", "end").strip()

        if not codigo_br:
            messagebox.showwarning("Aviso", "Digite algum código!")
            return

        self.caixa_saida.delete("1.0", "end")
        self.escrever_saida("─" * 50 + "\n")

        linhas_br = codigo_br.split("\n")

        try:
            codigo_py = traduzir(codigo_br)
            self.escrever_saida("📤 Saída:\n")
            self.escrever_saida("─" * 50 + "\n")

            sys.stdout = self

            namespace = self.namespace.copy()
            namespace["input"] = self.input_gui

            exec(codigo_py, namespace)
            self.namespace.update(namespace)

        except Exception as e:
            import traceback
            tb = e.__traceback__
            linha_erro = None
            while tb:
                if tb.tb_frame.f_code.co_filename == "<string>":
                    linha_erro = tb.tb_lineno
                tb = tb.tb_next

            if linha_erro and linha_erro <= len(linhas_br):
                self.escrever_saida(f"\n❌ Erro na linha {linha_erro}:\n")
                self.escrever_saida(f"   {linhas_br[linha_erro - 1]}\n")
                self.escrever_saida(f"\n   Detalhes: {e}\n")
            else:
                self.escrever_saida(f"\n❌ Erro: {e}\n")

        finally:
            sys.stdout = sys.__stdout__
            self.escrever_saida("\n" + "=" * 50 + "\n")

    def write(self, texto):
        self.escrever_saida(texto)

    def flush(self):
        pass

    def escrever_saida(self, texto):
        self.caixa_saida.insert("end", texto)
        self.caixa_saida.see("end")

    def carregar_exemplo(self):
        exemplo = '''função calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    retornar media

função classificar(media):
    se media maior ou igual 7:
        retornar "Aprovado"
    senão se media maior ou igual 5:
        retornar "Recuperação"
    senão:
        retornar "Reprovado"

mostrar("=== SISTEMA DE NOTAS ===")

nome = pergunte("Nome do aluno: ")
nota1 = decimal(pergunte("Nota 1: "))
nota2 = decimal(pergunte("Nota 2: "))

media = calcular_media(nota1, nota2)
situacao = classificar(media)

mostrar(f"\\nAluno: {nome}")
mostrar(f"Média: {media}")
mostrar(f"Situação: {situacao}")
'''
        self.caixa_codigo.delete("1.0", "end")
        self.caixa_codigo.insert("1.0", exemplo)
        self.atualizar_numeros_linha()


if __name__ == "__main__":
    app = JanelaBR()
    app.mainloop()