import tkinter as tk
import random

def gerar_numero():
    # Gera um número aleatório entre 1 e 1000
    numero_gerado = random.randint(1, 1000)
    # Atualiza o rótulo para exibir o número gerado
    resultado_label.config(text=f"Número gerado: {numero_gerado}", fg="white")

# Criação da janela principal
janela = tk.Tk()
janela.title("Gerador de Números Aleatórios")

# Configuração da cor de fundo da janela
janela.config(bg="#4CAF50")

# Criação do botão para gerar o número
gerar_botao = tk.Button(
    janela, 
    text="Gerar Número", 
    command=gerar_numero, 
    font=("Arial", 14, "bold"),
    bg="#FF9800", 
    fg="white", 
    relief="raised", 
    bd=5,
    padx=10,
    pady=5
)
gerar_botao.pack(pady=20)

# Rótulo para exibir o resultado
resultado_label = tk.Label(
    janela, 
    text="", 
    font=("Arial", 16, "bold"), 
    bg="#4CAF50", 
    fg="white"
)
resultado_label.pack(pady=20)

# Inicia o loop principal da interface gráfica
janela.mainloop()
