import tkinter as tk

def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    if tarefa:
        lista_tarefas.insert(tk.END, tarefa)
        entrada_tarefa.delete(0, tk.END)

def remover_tarefa():
    try:
        indice = lista_tarefas.curselection()[0]
        lista_tarefas.delete(indice)
    except IndexError:
        pass

# Configuração da janela principal
root = tk.Tk()
root.title("Lista de Tarefas")

# Frame para entrada de tarefas
frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10)

entrada_tarefa = tk.Entry(frame_entrada, font=("Helvetica", 14))
entrada_tarefa.pack(side=tk.LEFT, ipadx=50)

botao_adicionar = tk.Button(frame_entrada, text="Adicionar Tarefa", font=("Helvetica", 12), command=adicionar_tarefa)
botao_adicionar.pack(side=tk.LEFT, padx=10)

# Lista de tarefas
lista_tarefas = tk.Listbox(root, font=("Helvetica", 12), width=50, height=15)
lista_tarefas.pack(padx=20, pady=10)

botao_remover = tk.Button(root, text="Remover Tarefa Selecionada", font=("Helvetica", 12), command=remover_tarefa)
botao_remover.pack(pady=5)

root.mainloop()
