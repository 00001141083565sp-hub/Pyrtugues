from kivy.graphics import Color, RoundedRectangle, Line, Ellipse
from kivy.uix.widget import Widget

import re
import sys
import traceback
import threading
from queue import Queue, Empty

from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

TRADUCAO = {
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
    "sair": "exit",
    "parar": "stop",
    "iniciar": "start",
}


def traduzir_expressao(codigo):
    for br, py in sorted(TRADUCAO.items(), key=lambda x: -len(x[0])):
        if br in ("e", "ou"):
            continue
        codigo = re.sub(
            rf"(?<![A-Za-zÀ-ÿ0-9_]){re.escape(br)}(?![A-Za-zÀ-ÿ0-9_])",
            py, codigo, flags=re.IGNORECASE
        )

    codigo = re.sub(
        r"(?i)(?<![A-Za-zÀ-ÿ0-9_])e(?![A-Za-zÀ-ÿ0-9_])"
        r"(?=\s*(?:==|!=|>=|<=|>|<))", "and", codigo)
    codigo = re.sub(
        r"(?i)(?<![A-Za-zÀ-ÿ0-9_])e(?![A-Za-zÀ-ÿ0-9_])"
        r"(?=\s+(?:[A-Za-zÀ-ÿ_][A-Za-zÀ-ÿ0-9_]*|\(|\[|\{))", "and", codigo)

    codigo = re.sub(
        r"(?i)(?<![A-Za-zÀ-ÿ0-9_])ou(?![A-Za-zÀ-ÿ0-9_])"
        r"(?=\s*(?:==|!=|>=|<=|>|<))", "or", codigo)
    codigo = re.sub(
        r"(?i)(?<![A-Za-zÀ-ÿ0-9_])ou(?![A-Za-zÀ-ÿ0-9_])"
        r"(?=\s+(?:[A-Za-zÀ-ÿ_][A-Za-zÀ-ÿ0-9_]*|\(|\[|\{))", "or", codigo)
    return codigo


def traduzir_fstring(texto):
    m = re.match(r"(?is)^([rubf]{1,2})?(['\"])(.*)\2$", texto)
    if not m or "f" not in (m.group(1) or "").lower():
        return texto
    prefixo = m.group(1) or ""
    quote = m.group(2)
    corpo = m.group(3)

    def conv(match):
        return "{" + traduzir_expressao(match.group(1)) + "}"

    corpo = re.sub(r"\{([^{}]*)\}", conv, corpo)
    return prefixo + quote + corpo + quote


def proteger_strings(codigo):
    strings = []
    padrao = re.compile(
        r'''(?is)(?:[rubf]{0,2})(?:"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*')'''
    )

    def capturar(match):
        valor = match.group(0)
        prefixo = re.match(r"(?i)^[rubf]{0,2}", valor).group(0)
        if "f" in prefixo.lower():
            valor = traduzir_fstring(valor)
        strings.append(valor)
        return f"__PYRT_STR_{len(strings)-1}__"

    return padrao.sub(capturar, codigo), strings


def restaurar_strings(codigo, strings):
    for i, valor in enumerate(strings):
        codigo = codigo.replace(f"__PYRT_STR_{i}__", valor)
    return codigo


def traduzir(codigo_br):
    protegido, strings = proteger_strings(codigo_br)
    return restaurar_strings(traduzir_expressao(protegido), strings)


class KivyStdout:
    def __init__(self, app):
        self.app = app

    def write(self, texto):
        if texto:
            Clock.schedule_once(
                lambda dt, msg=texto: self.app.escrever_saida(msg), 0
            )

    def flush(self):
        pass


class InputManager:
    """Gerencia de forma assíncrona as solicitações de 'pergunte' na UI do Kivy."""
    def __init__(self, app):
        self.app = app

    def solicitar(self, prompt=""):
        if prompt:
            print(prompt, end="", flush=True)
        
        q = Queue()
        Clock.schedule_once(lambda dt: self._abrir_modal(prompt, q), 0)
        
        # Aguarda a resposta do usuário sem travar a thread principal do Kivy
        while True:
            try:
                val = q.get(timeout=0.1)
                return val
            except Empty:
                continue

    def _abrir_modal(self, prompt, q):
        conteudo = BoxLayout(orientation="vertical", padding=dp(20), spacing=dp(16))
        
        header_box = BoxLayout(orientation="horizontal", size_hint_y=None, height=dp(35))
        header_box.add_widget(Label(
            text=prompt.strip() or "Insira o valor solicitado:",
            color=(0.95, 0.96, 0.98, 1),
            font_size=dp(15),
            bold=True,
            halign="left"
        ))
        conteudo.add_widget(header_box)

        txt_input = TextInput(
            text="",
            multiline=False,
            font_size=dp(15),
            size_hint_y=None,
            height=dp(48),
            background_color=(0.11, 0.16, 0.24, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(0.06, 0.82, 0.52, 1),
            padding=[dp(14), dp(12)],
            hint_text="Digite sua resposta aqui..."
        )
        conteudo.add_widget(txt_input)

        btn = AccentButton(text="Confirmar Resposta", accent=True, size_hint_y=None, height=dp(46))
        conteudo.add_widget(btn)

        popup = Popup(
            title="Entrada Necessária (Pyrtugues)",
            title_color=(0.063, 0.718, 0.435, 1),
            title_size=dp(16),
            content=conteudo,
            size_hint=(0.85, 0.38),
            auto_dismiss=False
        )

        def enviar(*_):
            val = txt_input.text
            print(val)
            q.put(val)
            popup.dismiss()

        btn.bind(on_release=enviar)
        txt_input.bind(on_text_validate=enviar)
        popup.open()
        Clock.schedule_once(lambda dt: setattr(txt_input, 'focus', True), 0.1)



def abrir_modal_input(prompt, q):
    conteudo = BoxLayout(orientation="vertical", padding=dp(20), spacing=dp(16))
    
    # Cabeçalho decorado com Canvas
    header_box = BoxLayout(orientation="horizontal", size_hint_y=None, height=dp(35))
    header_box.add_widget(Label(
        text=prompt or "Insira o valor solicitado:",
        color=(0.95, 0.96, 0.98, 1),
        font_size=dp(15),
        bold=True,
        halign="left"
    ))
    conteudo.add_widget(header_box)

    txt_input = TextInput(
        text="",
        multiline=False,
        font_size=dp(15),
        size_hint_y=None,
        height=dp(48),
        background_color=(0.11, 0.16, 0.24, 1),
        foreground_color=(1, 1, 1, 1),
        cursor_color=(0.06, 0.82, 0.52, 1),
        padding=[dp(14), dp(12)]
    )
    conteudo.add_widget(txt_input)

    btn = AccentButton(text="Confirmar Entrada", accent=True, size_hint_y=None, height=dp(46))
    conteudo.add_widget(btn)

    popup = Popup(
        title="Entrada de Dados (Pyrtugues)",
        title_color=(0.063, 0.718, 0.435, 1),
        title_size=dp(16),
        content=conteudo,
        size_hint=(0.85, 0.35),
        auto_dismiss=False
    )

    def enviar(*_):
        val = txt_input.text
        print(val)
        q.put(val)
        popup.dismiss()

    btn.bind(on_release=enviar)
    txt_input.bind(on_text_validate=enviar)
    popup.open()
    Clock.schedule_once(lambda dt: setattr(txt_input, 'focus', True), 0.1)


class RoundedPanel(Widget):
    """Painel visual moderno com cantos arredondados."""
    def __init__(self, fill=(0.08, 0.11, 0.16, 1),
                 border=(0.16, 0.22, 0.32, 1),
                 radius=16, **kwargs):
        super().__init__(**kwargs)
        self.fill = fill
        self.border = border
        self.radius = radius
        with self.canvas.before:
            Color(*self.fill)
            self.bg = RoundedRectangle(
                pos=self.pos, size=self.size,
                radius=[dp(self.radius)]
            )
            Color(*self.border)
            self.line = Line(
                rounded_rectangle=(
                    self.x, self.y, self.width, self.height, dp(self.radius)
                ),
                width=1.2
            )
        self.bind(pos=self._sync, size=self._sync)

    def _sync(self, *_):
        self.bg.pos = self.pos
        self.bg.size = self.size
        self.bg.radius = [dp(self.radius)]
        self.line.rounded_rectangle = (
            self.x, self.y, self.width, self.height, dp(self.radius)
        )


class AccentButton(Button):
    """Botão visual do Pyrtugues com estado normal, pressionado e seleção."""
    def __init__(self, accent=False, outline=False, **kwargs):
        super().__init__(**kwargs)
        self.accent = accent
        self.outline = outline
        self.background_normal = ""
        self.background_down = ""
        self.background_color = (0, 0, 0, 0)
        self.color = (0.97, 0.98, 0.99, 1)
        self.font_size = dp(14)
        self.bold = True
        self.padding = [dp(10), dp(6)]

        with self.canvas.before:
            self._bg_color = Color(1, 1, 1, 1)
            self.bg = RoundedRectangle(pos=self.pos, size=self.size, radius=[dp(12)])
            self._border_color = Color(1, 1, 1, 1)
            self.border_line = Line(
                rounded_rectangle=(self.x, self.y, self.width, self.height, dp(12)),
                width=1.4
            )
        self.bind(pos=self._sync, size=self._sync, state=self._sync,
                  disabled=self._sync)
        self._sync()

    def _get_colors(self):
        if self.disabled:
            return (0.07, 0.09, 0.13, 1), (0.12, 0.15, 0.21, 1)
        if self.state == "down":
            if self.accent:
                return (0.045, 0.52, 0.31, 1), (0.063, 0.718, 0.435, 1)
            if self.outline:
                return (0.10, 0.15, 0.22, 1), (0.18, 0.26, 0.38, 1)
            return (0.09, 0.13, 0.18, 1), (0.15, 0.22, 0.32, 1)
        if self.accent:
            return (0.063, 0.718, 0.435, 1), (0.08, 0.82, 0.50, 1)
        if self.outline:
            return (0.07, 0.10, 0.15, 1), (0.18, 0.25, 0.35, 1)
        return (0.10, 0.14, 0.20, 1), (0.16, 0.22, 0.32, 1)

    def _sync(self, *_):
        bg_col, border_col = self._get_colors()
        self._bg_color.rgba = bg_col
        self._border_color.rgba = border_col
        self.bg.pos = self.pos
        self.bg.size = self.size
        self.border_line.rounded_rectangle = (
            self.x, self.y, self.width, self.height, dp(12)
        )

    def set_style(self, *, accent=None, outline=None):
        if accent is not None:
            self.accent = accent
        if outline is not None:
            self.outline = outline
        self._sync()


class StatusDot(Widget):
    def __init__(self, color=(0.063, 0.718, 0.435, 1), **kwargs):
        super().__init__(**kwargs)
        self.dot_color = color
        with self.canvas:
            Color(*self.dot_color)
            self.circle = Ellipse(pos=self.pos, size=self.size)
        self.bind(pos=self._sync, size=self._sync)

    def _sync(self, *_):
        self.circle.pos = self.pos
        self.circle.size = self.size


class PyrtuguesApp(App):
    title = "Pyrtugues - Programação em Português"

    BG = (0.035, 0.047, 0.078, 1)         # #090C14
    PANEL = (0.063, 0.086, 0.137, 1)      # #101623
    EDITOR = (0.047, 0.067, 0.110, 1)     # #0C111C
    BORDER = (0.141, 0.192, 0.286, 1)     # #24314A
    TEXT = (0.973, 0.980, 0.988, 1)       # #F8FAFC
    CODE = (0.900, 0.925, 0.955, 1)       # #E6EEF4
    SECONDARY = (0.620, 0.680, 0.760, 1)  # #9EAEC2
    MUTED = (0.420, 0.480, 0.580, 1)      # #6B7A94
    GREEN = (0.063, 0.718, 0.435, 1)      # #10B981
    ERROR = (0.95, 0.38, 0.38, 1)

    def build(self):
        Window.clearcolor = self.BG
        self.input_manager = InputManager(self)

        root = BoxLayout(
            orientation="vertical",
            padding=[dp(16), dp(14), dp(16), dp(14)],
            spacing=dp(12)
        )

        # ---------- HEADER MODERNO COM ABAS DE NAVEGAÇÃO ----------
        header = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=dp(64),
            padding=[dp(18), dp(10)],
            spacing=dp(12)
        )

        with header.canvas.before:
            Color(*self.PANEL)
            self.header_bg = RoundedRectangle(
                pos=header.pos, size=header.size, radius=[dp(16)]
            )
            Color(*self.BORDER)
            self.header_line = Line(
                rounded_rectangle=(
                    header.x, header.y, header.width, header.height, dp(16)
                ),
                width=1.2
            )
        header.bind(
            pos=lambda *_: self._sync_round_rect(
                self.header_bg, self.header_line, header, 16
            ),
            size=lambda *_: self._sync_round_rect(
                self.header_bg, self.header_line, header, 16
            )
        )
        header.bind(size=lambda *_: self._ajustar_cabecalho(header))

        self.logo = Label(
            text="[b]PYRTUGUES[/b]",
            markup=True,
            color=self.TEXT,
            font_size=dp(18),
            size_hint_x=None,
            width=dp(140),
            halign="left",
            valign="middle"
        )
        self.logo.bind(size=lambda inst, _: setattr(inst, "text_size", inst.size))
        header.add_widget(self.logo)

        nav_box = BoxLayout(
            orientation="horizontal",
            spacing=dp(5),
            size_hint_x=1
        )
        self.btn_aba_editor = AccentButton(text="Editor", accent=True, size_hint_x=1)
        self.btn_aba_editor.bind(on_release=lambda *_: self.mudar_aba("editor"))
        nav_box.add_widget(self.btn_aba_editor)

        self.btn_aba_input = AccentButton(text="Input", outline=True, size_hint_x=1)
        self.btn_aba_input.bind(on_release=lambda *_: self.mudar_aba("input"))
        nav_box.add_widget(self.btn_aba_input)

        self.btn_aba_exemplos = AccentButton(text="Exemplos", outline=True, size_hint_x=1)
        self.btn_aba_exemplos.bind(on_release=lambda *_: self.mudar_aba("exemplos"))
        nav_box.add_widget(self.btn_aba_exemplos)

        self.btn_aba_sobre = AccentButton(text="Sobre", outline=True, size_hint_x=1)
        self.btn_aba_sobre.bind(on_release=lambda *_: self.mudar_aba("sobre"))
        nav_box.add_widget(self.btn_aba_sobre)

        header.add_widget(nav_box)

        self.status_box = BoxLayout(
            orientation="horizontal",
            size_hint_x=None,
            width=dp(86),
            spacing=dp(6)
        )
        dot = StatusDot(size_hint=(None, None), size=(dp(9), dp(9)), pos_hint={'center_y': 0.5})
        self.status_box.add_widget(Widget())
        self.status_box.add_widget(dot)
        self.status_label = Label(
            text="Pronto",
            color=self.SECONDARY,
            font_size=dp(12),
            size_hint_x=None,
            width=dp(48),
            halign="left",
            valign="middle"
        )
        self.status_label.bind(size=lambda inst, _: setattr(inst, "text_size", inst.size))
        self.status_box.add_widget(self.status_label)
        header.add_widget(self.status_box)

        root.add_widget(header)

        # ---------- CONTAINER DE TELAS (ABAS) ----------
        self.container_telas = BoxLayout(orientation="vertical", spacing=dp(10))

        # 1. TELA DO EDITOR
        self.tela_editor = BoxLayout(orientation="vertical", spacing=dp(10))
        
        editor_title_box = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=dp(30),
            padding=[dp(4), 0]
        )
        editor_title_box.add_widget(Label(
            text="[b]Editor de Código (.pyrt)[/b]",
            markup=True,
            color=self.TEXT,
            font_size=dp(14),
            halign="left",
            valign="middle"
        ))
        editor_title_box.children[0].bind(
            size=lambda inst, _: setattr(inst, "text_size", inst.size)
        )

        badge_hint = Label(
            text="Português Nativo",
            color=self.MUTED,
            font_size=dp(11),
            size_hint_x=None,
            width=dp(110),
            halign="right",
            valign="middle"
        )
        badge_hint.bind(size=lambda inst, _: setattr(inst, "text_size", badge_hint.size))
        editor_title_box.add_widget(badge_hint)
        self.tela_editor.add_widget(editor_title_box)

        editor_card = BoxLayout(orientation="vertical", padding=dp(2), size_hint_y=0.55)
        with editor_card.canvas.before:
            Color(*self.EDITOR)
            self.editor_bg = RoundedRectangle(pos=editor_card.pos, size=editor_card.size, radius=[dp(16)])
            Color(*self.BORDER)
            self.editor_line = Line(rounded_rectangle=(editor_card.x, editor_card.y, editor_card.width, editor_card.height, dp(16)), width=1.2)
        editor_card.bind(
            pos=lambda *_: self._sync_round_rect(self.editor_bg, self.editor_line, editor_card, 16),
            size=lambda *_: self._sync_round_rect(self.editor_bg, self.editor_line, editor_card, 16)
        )

        self.caixa_codigo = TextInput(
            text=(
                'mostrar("=== SISTEMA PYRTUGUES ===")\n'
                '\n'
                'nome = pergunte("Qual é o seu nome? ")\n'
                'idade = inteiro(pergunte("Quantos anos você tem? "))\n'
                '\n'
                'se idade maior ou igual a 12:\n'
                '    mostrar(f"Olá, {nome}! Você já pode programar sistemas incríveis.")\n'
                'senão:\n'
                '    mostrar(f"Oi, {nome}! O futuro da tecnologia é seu!")\n'
            ),
            font_size=dp(14),
            foreground_color=self.CODE,
            background_color=(0, 0, 0, 0),
            cursor_color=self.GREEN,
            selection_color=(0.063, 0.718, 0.435, 0.3),
            padding=[dp(16), dp(16)],
            multiline=True,
            write_tab=False,
            hint_text="Escreva seu código em português aqui...",
            hint_text_color=self.MUTED,
            cursor_width=dp(2)
        )
        editor_card.add_widget(self.caixa_codigo)
        self.tela_editor.add_widget(editor_card)

        action_bar = BoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height=dp(48),
            spacing=dp(12)
        )
        self.btn_executar = AccentButton(text="▶  Executar", accent=True, size_hint_x=0.5)
        self.btn_executar.bind(on_release=lambda *_: self.iniciar_execucao())
        action_bar.add_widget(self.btn_executar)

        self.btn_limpar = AccentButton(text="🧹 Limpar", outline=True, size_hint_x=0.5)
        self.btn_limpar.bind(on_release=lambda *_: self.limpar())
        action_bar.add_widget(self.btn_limpar)
        self.tela_editor.add_widget(action_bar)

        output_title_box = BoxLayout(orientation="horizontal", size_hint_y=None, height=dp(28), padding=[dp(4), 0])
        out_label = Label(text="[b]Saída do Terminal[/b]", markup=True, color=self.TEXT, font_size=dp(13), halign="left", valign="middle")
        out_label.bind(size=lambda inst, _: setattr(inst, "text_size", inst.size))
        output_title_box.add_widget(out_label)
        self.tela_editor.add_widget(output_title_box)

        output_card = BoxLayout(orientation="vertical", padding=dp(2), size_hint_y=0.28)
        with output_card.canvas.before:
            Color(*self.EDITOR)
            self.output_bg = RoundedRectangle(pos=output_card.pos, size=output_card.size, radius=[dp(16)])
            Color(*self.BORDER)
            self.output_line = Line(rounded_rectangle=(output_card.x, output_card.y, output_card.width, output_card.height, dp(16)), width=1.2)
        output_card.bind(
            pos=lambda *_: self._sync_round_rect(self.output_bg, self.output_line, output_card, 16),
            size=lambda *_: self._sync_round_rect(self.output_bg, self.output_line, output_card, 16)
        )

        self.saida = TextInput(
            text="Pronto para executar seu código...",
            readonly=True,
            font_size=dp(13),
            foreground_color=self.SECONDARY,
            background_color=(0, 0, 0, 0),
            padding=[dp(16), dp(14)],
            cursor_color=(0, 0, 0, 0),
            multiline=True
        )
        output_card.add_widget(self.saida)
        self.tela_editor.add_widget(output_card)

        # 2. ABA DE INPUT / ENTRADA DE DADOS
        self.tela_input = ScrollView(size_hint=(1, 1))
        input_layout = BoxLayout(orientation="vertical", spacing=dp(14), padding=dp(15), size_hint_y=None)
        input_layout.bind(minimum_height=input_layout.setter('height'))

        input_layout.add_widget(Label(text="[b]Gerenciador de Input Interativo[/b]", markup=True, color=self.TEXT, font_size=dp(16), size_hint_y=None, height=dp(30), halign="left"))
        
        desc_input = Label(
            text="Aqui você pode testar entradas de dados avulsas (simulando a função 'pergunte') ou configurar dados padrão para os seus testes de lógica.",
            color=self.SECONDARY,
            font_size=dp(13),
            text_size=(Window.width - dp(60), None),
            halign="left",
            valign="top",
            size_hint_y=None
        )
        desc_input.bind(width=lambda inst, w: setattr(inst, "text_size", (w, None)), texture_size=lambda inst, sz: setattr(inst, "height", sz[1]))
        input_layout.add_widget(desc_input)

        card_teste_input = BoxLayout(orientation="vertical", padding=dp(16), spacing=dp(12), size_hint_y=None, height=dp(190))
        with card_teste_input.canvas.before:
            Color(*self.PANEL)
            RoundedRectangle(pos=card_teste_input.pos, size=card_teste_input.size, radius=[dp(14)])
        
        card_teste_input.add_widget(Label(text="[b]Testar Pergunta (pergunte)[/b]", markup=True, color=self.TEXT, font_size=dp(14), halign="left"))
        
        self.input_prompt_txt = TextInput(
            text="Qual é o seu esporte favorito? ",
            multiline=False,
            font_size=dp(13),
            size_hint_y=None,
            height=dp(42),
            background_color=(0.11, 0.16, 0.24, 1),
            foreground_color=(1, 1, 1, 1),
            padding=[dp(12), dp(10)]
        )
        card_teste_input.add_widget(self.input_prompt_txt)

        btn_testar_prompt = AccentButton(text="💬 Abrir Janela de Input", accent=True, size_hint_y=None, height=dp(42))
        btn_testar_prompt.bind(on_release=lambda *_: threading.Thread(target=lambda: self.input_manager.solicitar(self.input_prompt_txt.text), daemon=True).start())
        card_teste_input.add_widget(btn_testar_prompt)

        input_layout.add_widget(card_teste_input)
        self.tela_input.add_widget(input_layout)

        # 3. TELA DE EXEMPLOS
        self.tela_exemplos = ScrollView(size_hint=(1, 1))
        ex_layout = BoxLayout(orientation="vertical", spacing=dp(12), padding=dp(10), size_hint_y=None)
        ex_layout.bind(minimum_height=ex_layout.setter('height'))

        ex_layout.add_widget(Label(text="[b]Biblioteca de Exemplos Pyrtugues[/b]", markup=True, color=self.TEXT, font_size=dp(16), size_hint_y=None, height=dp(30), halign="left"))
        
        exemplos_lista = [
            ("Calculadora Simples", 'n1 = decimal(pergunte("Digite o 1º número: "))\nop = pergunte("Operação (+, -, *, /): ")\nn2 = decimal(pergunte("Digite o 2º número: "))\n\nse op == "+":\n    mostrar(n1 + n2)\nsenão se op == "-":\n    mostrar(n1 - n2)\nsenão se op == "*":\n    mostrar(n1 * n2)\nsenão:\n    mostrar(n1 / n2)'),
            ("Tabuada Interativa", 'num = inteiro(pergunte("Qual tabuada você quer ver? "))\npara i em intervalo(1, 11):\n    mostrar(f"{num} x {i} = {num * i}")'),
            ("Contagem Regressiva", 'mostrar("Iniciando contagem...")\npara t em intervalo(5, 0, -1):\n    mostrar(t)\nmostrar("Fogo! 🚀")')
        ]

        for titulo, codigo in exemplos_lista:
            card_ex = BoxLayout(orientation="vertical", padding=dp(14), spacing=dp(8), size_hint_y=None, height=dp(118))
            with card_ex.canvas.before:
                Color(*self.PANEL)
                RoundedRectangle(pos=card_ex.pos, size=card_ex.size, radius=[dp(12)])
            card_ex.add_widget(Label(text=f"[b]{titulo}[/b]", markup=True, color=self.TEXT, font_size=dp(14), halign="left"))
            
            btn_carregar = AccentButton(text="📂 Carregar no Editor", accent=True, size_hint_y=None, height=dp(40))
            btn_carregar.bind(on_release=lambda _, c=codigo: self.carregar_codigo_exemplo(c))
            card_ex.add_widget(btn_carregar)
            ex_layout.add_widget(card_ex)

        self.tela_exemplos.add_widget(ex_layout)

        # 4. TELA SOBRE O PROJETO E CRIADOR
        self.tela_sobre = ScrollView(size_hint=(1, 1))
        sobre_layout = BoxLayout(orientation="vertical", spacing=dp(15), padding=dp(15), size_hint_y=None)
        sobre_layout.bind(minimum_height=sobre_layout.setter('height'))

        sobre_layout.add_widget(Label(text="[b]Sobre o Pyrtugues[/b]", markup=True, color=self.TEXT, font_size=dp(18), size_hint_y=None, height=dp(35)))
        
        texto_sobre = (
            "O Pyrtugues é uma ferramenta educacional desenvolvida para tornar o aprendizado "
            "de lógica de programação acessível e intuitivo através do português nativo.\n\n"
            "Criado por Vinicius Caracciolo (com 12 anos de idade), o projeto tem como objetivo "
            "remover barreiras iniciais de idioma para jovens programadores, mantendo toda a "
            "compatibilidade com a sintaxe e o poder do Python."
        )
        lbl_sobre = Label(text=texto_sobre, color=self.SECONDARY, font_size=dp(14), text_size=(Window.width - dp(60), None), halign="left", valign="top", size_hint_y=None)
        lbl_sobre.bind(width=lambda inst, w: setattr(inst, "text_size", (w, None)), texture_size=lambda inst, sz: setattr(inst, "height", sz[1]))
        sobre_layout.add_widget(lbl_sobre)
        self.tela_sobre.add_widget(sobre_layout)

        self.container_telas.add_widget(self.tela_editor)
        root.add_widget(self.container_telas)

        footer = Label(
            text="Pyrtugues • Criado por Vinicius Caracciolo",
            color=self.MUTED,
            font_size=dp(10),
            size_hint_y=None,
            height=dp(20),
            halign="center",
            valign="middle"
        )
        footer.bind(size=lambda inst, _: setattr(inst, "text_size", inst.size))
        root.add_widget(footer)

        return root

    def _ajustar_cabecalho(self, header):
        # Mantém as quatro abas utilizáveis também em telas menores de celular.
        compacto = header.width < dp(620)
        self.logo.width = dp(100) if compacto else dp(140)
        self.status_box.width = dp(18) if header.width < dp(520) else dp(86)
        self.btn_aba_editor.font_size = dp(12 if compacto else 14)
        self.btn_aba_input.font_size = dp(12 if compacto else 14)
        self.btn_aba_exemplos.font_size = dp(11 if compacto else 14)
        self.btn_aba_sobre.font_size = dp(12 if compacto else 14)
        self.status_label.opacity = 0 if header.width < dp(520) else 1

    def _sync_round_rect(self, rect, line, widget, radius):
        rect.pos = widget.pos
        rect.size = widget.size
        rect.radius = [dp(radius)]
        line.rounded_rectangle = (
            widget.x, widget.y, widget.width, widget.height, dp(radius)
        )

    def mudar_aba(self, nome_aba):
        self.container_telas.clear_widgets()
        
        for botao in (
            self.btn_aba_editor, self.btn_aba_input,
            self.btn_aba_exemplos, self.btn_aba_sobre
        ):
            botao.set_style(accent=False, outline=True)

        if nome_aba == "editor":
            self.btn_aba_editor.set_style(accent=True, outline=False)
            self.container_telas.add_widget(self.tela_editor)
        elif nome_aba == "input":
            self.btn_aba_input.set_style(accent=True, outline=False)
            self.container_telas.add_widget(self.tela_input)
        elif nome_aba == "exemplos":
            self.btn_aba_exemplos.set_style(accent=True, outline=False)
            self.container_telas.add_widget(self.tela_exemplos)
        elif nome_aba == "sobre":
            self.btn_aba_sobre.set_style(accent=True, outline=False)
            self.container_telas.add_widget(self.tela_sobre)

    def carregar_codigo_exemplo(self, codigo):
        self.caixa_codigo.text = codigo
        self.mudar_aba("editor")

    def set_status(self, text, running=False):
        self.status_label.text = text
        self.status_label.color = self.GREEN if not running else (1, 0.75, 0.2, 1)
        self.btn_executar.disabled = running
        self.btn_executar.text = "⏳  Executando..." if running else "▶  Executar"

    def limpar(self):
        self.caixa_codigo.text = ""
        self.saida.text = "Editor limpo com sucesso."
        self.saida.foreground_color = self.SECONDARY
        self.set_status("Pronto")

    def escrever_saida(self, texto):
        self.saida.text += texto

    def iniciar_execucao(self):
        if self.btn_executar.disabled:
            return

        self.saida.text = ""
        self.saida.foreground_color = self.CODE
        self.set_status("Executando", running=True)
        threading.Thread(
            target=self._executar_em_thread,
            daemon=True
        ).start()

    def _mostrar_resultado(self, texto, erro=False):
        if texto and not self.saida.text:
            self.saida.text = texto
        elif not self.saida.text.strip():
            self.saida.text = "Código executado com sucesso."
        
        self.saida.foreground_color = self.ERROR if erro else self.CODE
        self.set_status("Erro" if erro else "Concluído")

    def _executar_em_thread(self):
        try:
            codigo_br = self.caixa_codigo.text
            codigo_py = traduzir(codigo_br)

            old_stdout = sys.stdout
            sys.stdout = KivyStdout(self)
            try:
                namespace = {
                    "__name__": "__main__",
                    "pergunte": self.input_manager.solicitar,
                    "input": self.input_manager.solicitar,
                }
                exec(codigo_py, namespace)
            finally:
                sys.stdout = old_stdout

            Clock.schedule_once(
                lambda *_: self._mostrar_resultado(
                    self.saida.text if self.saida.text.strip()
                    else "Código executado com sucesso."
                )
            )
        except Exception:
            erro = traceback.format_exc()
            Clock.schedule_once(
                lambda *_: self._mostrar_resultado(
                    "❌ Erro na execução:\n\n" + erro, True
                )
            )


if __name__ == "__main__":
    PyrtuguesApp().run()
