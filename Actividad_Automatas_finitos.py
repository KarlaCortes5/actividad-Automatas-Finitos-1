import tkinter as tk
from tkinter import messagebox

def validar_contraseña(contraseña):
    estado = "q0"
    estados_aceptacion = {"q4"}
    tiene_letra = False
    tiene_numero = False
    tiene_especial = False
    
    for c in contraseña:
        if c.isalpha():
            tiene_letra = True
        elif c.isdigit():
            tiene_numero = True
        elif c in "@#!":
            tiene_especial = True
        else:
            return False
    
    if tiene_letra and tiene_numero and tiene_especial:
        estado = "q4"
    
    return estado in estados_aceptacion

def verificar():
    contraseña = entry.get()
    if validar_contraseña(contraseña):
        messagebox.showinfo("Resultado", "Contraseña válida")
    else:
        messagebox.showerror("Resultado", "Contraseña inválida")

root = tk.Tk()
root.title("Validador de Contraseñas")
root.geometry("300x150")

tk.Label(root, text="Ingrese su contraseña:").pack(pady=5)
entry = tk.Entry(root, show="*")
entry.pack(pady=5)

tk.Button(root, text="Verificar", command=verificar).pack(pady=5)
root.mainloop()