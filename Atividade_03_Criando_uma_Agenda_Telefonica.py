import tkinter as tk
from tkinter import ttk, messagebox

agenda = {}

def adicionar_contato():
    nome = entry_nome.get()
    telefone = entry_telefone.get()
    
    if nome.strip() == "" or telefone.strip() == "":
        messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
    else:
        if nome not in agenda:
            agenda[nome] = telefone
            messagebox.showinfo("Sucesso", "Contato adicionado com sucesso!")
            listar_contatos()
        else:
            messagebox.showerror("Erro", "Este contato já existe na agenda.")

def buscar_contato():
    nome = entry_nome.get()
    
    if nome in agenda:
        telefone = agenda[nome]
        messagebox.showinfo("Informação", f"Telefone de {nome}: {telefone}")
    else:
        messagebox.showerror("Erro", "Contato não encontrado na agenda.")

def listar_contatos():
    lista_contatos.delete(0, tk.END)
    for nome, telefone in agenda.items():
        lista_contatos.insert(tk.END, f"{nome}: {telefone}")

def remover_contato():
    nome = entry_nome.get()
    
    if nome in agenda:
        del agenda[nome]
        messagebox.showinfo("Sucesso", "Contato removido com sucesso!")
        listar_contatos()
    else:
        messagebox.showerror("Erro", "Contato não encontrado na agenda.")

# Configuração da janela principal
root = tk.Tk()
root.title("Agenda Telefônica Moderna")

# Estilo da aplicação
style = ttk.Style()
style.theme_use("clam")  # Você pode escolher entre 'clam', 'alt', 'default' ou 'classic'

# Widgets
frame_campos = ttk.Frame(root)
frame_campos.pack(padx=20, pady=10)

label_nome = ttk.Label(frame_campos, text="Nome:")
label_nome.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
entry_nome = ttk.Entry(frame_campos)
entry_nome.grid(row=0, column=1, padx=5, pady=5)

label_telefone = ttk.Label(frame_campos, text="Telefone:")
label_telefone.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
entry_telefone = ttk.Entry(frame_campos)
entry_telefone.grid(row=1, column=1, padx=5, pady=5)

frame_botoes = ttk.Frame(root)
frame_botoes.pack(padx=20, pady=(0, 10), fill=tk.X)

botao_adicionar = ttk.Button(frame_botoes, text="Adicionar Contato", command=adicionar_contato)
botao_adicionar.pack(side=tk.LEFT, padx=5, pady=5)

botao_buscar = ttk.Button(frame_botoes, text="Buscar Contato", command=buscar_contato)
botao_buscar.pack(side=tk.LEFT, padx=5, pady=5)

botao_listar = ttk.Button(frame_botoes, text="Listar Contatos", command=listar_contatos)
botao_listar.pack(side=tk.LEFT, padx=5, pady=5)

botao_remover = ttk.Button(frame_botoes, text="Remover Contato", command=remover_contato)
botao_remover.pack(side=tk.LEFT, padx=5, pady=5)

frame_lista = ttk.Frame(root)
frame_lista.pack(padx=20, pady=10)

lista_contatos = tk.Listbox(frame_lista, width=50, height=10)
lista_contatos.pack(padx=5, pady=5)

# Loop principal da aplicação
root.mainloop()
