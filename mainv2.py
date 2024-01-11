import tkinter as tk
from tkinter import ttk
from ventanav2 import Ventana
    
if __name__ == "__main__":
    root = tk.Tk()
    root.title('cosa')
    root.minsize(width=1250, height=600)
    root.geometry('1300x650')
    estilo_ventana = ttk.Style(root)
    root.tk.call("source", "forest-dark.tcl")
    estilo_ventana.theme_use("forest-dark")
    app = Ventana(root)
    
    app.master.columnconfigure(0, weight=1, minsize=440)
    app.master.columnconfigure(1, weight=1)
    app.master.rowconfigure(0, weight=1)
    
    app.mainloop()
    