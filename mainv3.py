from tkinter import ttk
from ventanav4principal import Ventana
    
if __name__ == "__main__":
    
    app = Ventana()
    app.title('Biblioteca')
    estilo_ventana = ttk.Style(app)
    app.tk.call("source", "forest-dark.tcl")
    estilo_ventana.theme_use("forest-dark")
    app.minsize(width=1200, height=650)
    # 1440x900
    app.geometry('1000x600')
    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)
    app.mainloop()
    