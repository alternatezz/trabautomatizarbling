import tkinter as tk
import subprocess
import sys
import os

def press_key(key):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + key)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Função para gerar o executável
def generate_executable():
    # Caminho para o executável do PyInstaller
    pyinstaller_path = r'C:\Users\MEUCOMPUTADOR\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts\pyinstaller.exe'

    if os.path.exists(pyinstaller_path):
        subprocess.Popen([pyinstaller_path, '--onefile', sys.argv[0]], creationflags=subprocess.CREATE_NO_WINDOW)
    else:
        print("PyInstaller não encontrado.")

    sys.exit(0)

# Verifica se o programa está sendo executado como um executável independente
if getattr(sys, 'frozen', False):
    # Se estiver sendo executado como um executável, inicie a interface da calculadora
    root = tk.Tk()
    root.title("Calculadora")

    # Entrada
    entry = tk.Entry(root, width=20, font=('Arial', 14))
    entry.grid(row=0, column=0, columnspan=4)

    # Botões
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ]

    for (text, row, col) in buttons:
        tk.Button(root, text=text, width=5, height=2, command=lambda t=text: press_key(t)).grid(row=row, column=col)

    # Botão de Limpar
    tk.Button(root, text='Limpar', width=5, height=2, command=clear).grid(row=5, column=1)

    # Botão de calcular
    tk.Button(root, text='Calcular', width=5, height=2, command=calculate).grid(row=5, column=2)

    root.mainloop()
else:
    # Se estiver sendo executado como um script Python, gere o executável
    generate_executable()
