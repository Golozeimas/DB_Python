import tkinter as tk
import app.orm as orm
from tkinter import messagebox

# Raiz do projeto de uma aplicação desktop
root = tk.Tk()

# nome que fica encima da janela
root.title("Gerenciador de filmes")

# tamanho da janela é definido
root.geometry("500x500")

# impede de redimensionar (deixa sempre no tamanho que já foi feito)
root.resizable(False,False)

# isso aqui é para colocar um icon,  no caso não temos
root.iconbitmap()

# label é a escrita de texto na aplicação
label_id = tk.Label(root, text="ID:")

# posicionamento avançado
label_id.grid(row=0, column=0)

# entry representa o input ou caixa de texto
entry_id = tk.Entry(root, width=70)

# representa o posicionamento, no caso, está na mesma linha
# e a coluna pra frente por isso 1
entry_id.grid(row=0, column=1, padx=10, pady=5)

label_nome = tk.Label(root, text="Nome:")

label_nome.grid(row=1, column=0)

entry_nome = tk.Entry(root, width=70)

# desce apenas a linha, o padrão de colunas continua o mesmo
entry_nome.grid(row=1, column=1, padx=10, pady=5)

label_ano = tk.Label(root, text="Ano:")

label_ano.grid(row=2, column=0)

entry_ano = tk.Entry(root, width=70)

entry_ano.grid(row=2, column=1, padx=10, pady=5)

label_nota = tk.Label(root, text="Nota")

label_nota.grid(row=3, column=0)

entry_nota = tk.Entry(root, width=70)

entry_nota.grid(row=3, column=1, padx=10, pady=5)

# fazemos uma função pra usar no botão
def adicionar_filme():
    # pegando o input para modificamos ou adicionar no banco
    nome = entry_nome.get()
    ano = entry_ano.get()
    nota = entry_nota.get()
    orm.adiciona_filme(nome, ano, nota)

tk.mainloop()
