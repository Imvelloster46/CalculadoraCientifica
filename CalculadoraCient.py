import tkinter
import math

def clicar(valor):
    # Obter o valor atual na entrada
    e = entry.get()
    # Inicializar a variável de resposta
    resp = " "

    try:
        if valor == "C":
            # Deletar o último caractere na entrada
            e = e[0:len(e) - 1]
            entry.delete(0, "end")
            entry.insert(0, e)
            return
        elif valor == "CE":
            # Limpar toda a entrada
            entry.delete(0, "end")
        elif valor == "√":
            resp = math.sqrt(eval(e))
        elif valor == "π":
            resp = math.pi
        elif valor == "cos0":
            resp = math.cos(math.radians(eval(e)))
        elif valor == "sin0":
            resp = math.sin(math.radians(eval(e)))
        elif valor == "tan0":
            resp = math.tan(math.radians(eval(e)))
        elif valor == "2π":
            resp = 2 * math.pi
        elif valor == "cosh":
            resp = math.cosh(eval(e))
        elif valor == "sinh":
            resp = math.sinh(eval(e))
        elif valor == "tanh":
            resp = math.tanh(eval(e))
        elif valor == chr(8731):
            resp = eval(e) ** (1 / 3)
        elif valor == "x\u02b8":
            entry.insert("end", "**")
            return
        elif valor == "x\u00B3":
            resp = eval(e) ** 3
        elif valor == "x\u00B2":
            resp = eval(e) ** 2
        elif valor == "ln":
            resp = math.log(eval(e))
        elif valor == "deg":
            resp = math.degrees(eval(e))
        elif valor == "rad":
            resp = math.radians(eval(e))
        elif valor == "e":
            resp = math.e
        elif valor == "log10":
            resp = math.log10(eval(e))
        elif valor == "x!":
            resp = math.factorial(eval(e))
        elif valor == chr(247):
            entry.insert("end", "/")
            return
        elif valor == "=":
            resp = eval(e)
        else:
            entry.insert("end", valor)
            return

        # Limpar o campo de entrada
        entry.delete(0, "end")
        # Exibir o resultado no campo de entrada
        entry.insert(0, resp)
    except SyntaxError:
        pass

# Criar a janela principal
root = tkinter.Tk()
root.title("Calculadora Científica")
root.geometry("680x486+100+100")
root.config(bg="black")

# Criar o widget de entrada
entry = tkinter.Entry(root, font=("arial", 20, "bold"),
                      bg="black", fg="white", bd=10, width=30)
entry.grid(row=0, column=0, columnspan=8)

# Lista de botões
botoes = ["C", "CE", "√", "+", "π", "cos0", "tan0", "sin0",
          "1", "2", "3", "-", "2π", "cosh", "tanh", "sinh", "4", "5",
          "6", "*", chr(8731), "x\u02b8", "x\u00B3", "x\u00B2", "7",
          "8", "9", chr(247), "ln", "deg", "rad", "e", "0", ".", "%",
          "=", "log10", "(", ")", "x!"]

linha = 1
coluna = 0

# Loop para criar botões na janela
for valor in botoes:
    # Criar botões
    botao = tkinter.Button(root, width=5, height=2, bd=2, text=valor,
                           bg="black", fg="white", font=("arial", 18, "bold"),
                           command=lambda botao=valor: clicar(botao))
    botao.grid(row=linha, column=coluna, pady=1)

    coluna += 1
    if coluna > 7:
        linha += 1
        coluna = 0

root.mainloop()