import tkinter as tk
from tkinter import messagebox

def show_hello_world():
    """Affiche une boîte de dialogue avec le message 'Hello, World!'."""
    messagebox.showinfo("Hello World", "Hello, World!")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Hello World App")
root.geometry("300x150")

# Ajout d'un bouton pour déclencher l'affichage du message
hello_button = tk.Button(
    root,
    text="Click me!",
    command=show_hello_world,
    font=("Arial", 12),
    padx=20,
    pady=10
)
hello_button.pack(pady=30)

# Lancement de la boucle principale de l'application
root.mainloop()