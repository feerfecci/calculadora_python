
import tkinter as tk

# ==============================
# Cores
# ==============================

black = "#383838"
white = "#feffff"
blue = "#38576b"
bege = "#ECEFF1"
laranja = "#FFAB40"


# ==============================
# Janela principal
# ==============================

window = tk.Tk()
window.title("Minha Calculadora")
window.geometry("235x310")
window.config(bg=black)


# ==============================
# Frames
# ==============================

frame_input = tk.Frame(window, width=235, height=50, bg=blue)
frame_input.grid(row=0, column=0, sticky="nsew")

frame_body = tk.Frame(window, width=235, height=260, bg=black)
frame_body.grid(row=1, column=0, sticky="nsew")

window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=0)
window.rowconfigure(1, weight=1)

frame_input.grid_propagate(False)

for coluna in range(4):
    frame_body.columnconfigure(coluna, weight=1, uniform="colunas")

for linha in range(5):
    frame_body.rowconfigure(linha, weight=1, uniform="linhas")


# ==============================
# Variáveis
# ==============================

typpd = ""
valor_texto = tk.StringVar()


# ==============================
# Funções
# ==============================

def entrar_valores(event):
    global typpd

    typpd = typpd + str(event)
    valor_texto.set(typpd)


def calcular():
    global typpd

    result = eval(typpd)
    typpd = ""
    typpd = str(result)
    valor_texto.set(result)


def limpar():
    global typpd

    typpd = ""
    valor_texto.set("")


# ==============================
# Tela da calculadora
# ==============================

app_label = tk.Label(
    frame_input,
    textvariable=valor_texto,
    width=16,
    height=2,
    padx=7,
    relief="flat",
    anchor="e",
    justify="right",
    font=("Ivy 18"),
    bg=blue,
    fg=white,
)

app_label.place(x=0, y=0)


# ==============================
# Botões
# ==============================

def make_button(
    frame, text, row, column, command,
    color=bege, text_color=black, columnspan=1
) -> tk.Button:
    button = tk.Button(
        frame,
        command=command,
        text=text,
        height=2,
        bg=color,
        fg=text_color,
        font=("Ivy 13 bold"),
        relief="raised",
        overrelief="ridge",
    )

    button.grid(
        row=row,
        column=column,
        columnspan=columnspan,
        sticky="nsew",
        padx=2,
        pady=2,
    )

    return button


# Linha 1
b_clean = make_button(frame_body, "C", 0, 0, limpar, columnspan=2)
b_module = make_button(frame_body, "%", 0, 2, lambda: entrar_valores("%"))
b_divsao = make_button(
    frame_body, "/", 0, 3, lambda: entrar_valores("/"), laranja, white
)

# Linha 2
b_7 = make_button(frame_body, "7", 1, 0, lambda: entrar_valores("7"))
b_8 = make_button(frame_body, "8", 1, 1, lambda: entrar_valores("8"))
b_9 = make_button(frame_body, "9", 1, 2, lambda: entrar_valores("9"))
b_mult = make_button(
    frame_body, "*", 1, 3, lambda: entrar_valores("*"), laranja, white
)

# Linha 3
b_4 = make_button(frame_body, "4", 2, 0, lambda: entrar_valores("4"))
b_5 = make_button(frame_body, "5", 2, 1, lambda: entrar_valores("5"))
b_6 = make_button(frame_body, "6", 2, 2, lambda: entrar_valores("6"))
b_minus = make_button(
    frame_body, "-", 2, 3, lambda: entrar_valores("-"), laranja, white
)

# Linha 4
b_1 = make_button(frame_body, "1", 3, 0, lambda: entrar_valores("1"))
b_2 = make_button(frame_body, "2", 3, 1, lambda: entrar_valores("2"))
b_3 = make_button(frame_body, "3", 3, 2, lambda: entrar_valores("3"))
b_plus = make_button(
    frame_body, "+", 3, 3, lambda: entrar_valores("+"), laranja, white
)

# Linha 5
b_zero = make_button(
    frame_body, "0", 4, 0, lambda: entrar_valores("0"), columnspan=2
)
b_dot = make_button(frame_body, ".", 4, 2, lambda: entrar_valores("."))
b_result = make_button(
    frame_body, "=", 4, 3, calcular, laranja, white
)


# ==============================
# Executar aplicação
# ==============================

window.mainloop()
