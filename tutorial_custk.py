import tkinter as tk
import customtkinter

# Crea una instancia de la ventana
root = tk.Tk()
root.title("Ejemplo ventana")
root.geometry("500x500")

# Configura la apariencia de customtkinter
customtkinter.set_appearance_mode("System")  # Modo: "System" (estándar), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Temas: "blue" (estándar), "green", "dark-blue"

# Crea el Entry
entry = customtkinter.CTkEntry(root, placeholder_text="Ingresa texto")
entry.place(x=50, y=50, anchor="nw")

# Crea el desplegable
optionmenu = customtkinter.CTkOptionMenu(root, values=["Opción 1", "Opción 2", "Opción 3"])
optionmenu.place(x=50, y=100, anchor="nw")

# Crea el botón
button = customtkinter.CTkButton(root, text="Aceptar")
button.place(x=50, y=150, anchor="nw")

# Ejecuta el bucle de eventos
root.mainloop()
