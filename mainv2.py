from tkinter import ttk
from ventanav2 import Ventana
    
if __name__ == "__main__":
    
    app = Ventana()
    app.title('Biblioteca')
    estilo_ventana = ttk.Style(app)
    app.tk.call("source", "forest-dark.tcl")
    estilo_ventana.theme_use("forest-dark")
    app.minsize(width=1250, height=600)
    app.geometry('1300x650')
    app.columnconfigure(1, weight=1, minsize=440)
    app.columnconfigure(2, weight=1)
    app.rowconfigure(0, weight=1)
    
    app.mainloop()
    