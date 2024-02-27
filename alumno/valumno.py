import ttkbootstrap as ttk

import alumno.ventana_alumnos as veal
import alumno.pedidos_librosalu as peli
import alumno.pedidos_laminasalu as pela
import alumno.devoluciones_librosalu as deli
import alumno.devoluciones_laminasalu as dela

class NotebookAlumno(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.venalu = veal.VentanaAlumnos()
        self.pedlib = peli.PedidosLibros()
        self.pedlam = pela.PedidosLaminas()
        self.devlib = deli.DevolucionesLibros()
        self.devlam = dela.DevolucionesLaminas()
        
        self.mytabcontrol = ttk.Notebook(self.master, bootstyle='primary')
        
        self.alumno_tab = ttk.Frame(self.mytabcontrol)
        self.alumno_tab.columnconfigure(0, weight=1, minsize=370)
        self.alumno_tab.columnconfigure(1, weight=10)
        self.alumno_tab.rowconfigure(0, weight=1)
        
        self.pedidoli_tab = ttk.Frame(self.mytabcontrol) 
        self.pedidoli_tab.columnconfigure(0, weight=1, minsize=340)
        self.pedidoli_tab.columnconfigure(1, weight=10)
        self.pedidoli_tab.rowconfigure(0, weight=1)
        
        self.pedidola_tab = ttk.Frame(self.mytabcontrol) 
        self.pedidola_tab.columnconfigure(0, weight=1, minsize=340)
        self.pedidola_tab.columnconfigure(1, weight=10)
        self.pedidola_tab.rowconfigure(0, weight=1)
        
        self.devoli_tab = ttk.Frame(self.mytabcontrol)
        self.devoli_tab.columnconfigure(0, weight=1, minsize=340)
        self.devoli_tab.columnconfigure(1, weight=10)
        self.devoli_tab.rowconfigure(0, weight=1)

        self.devola_tab = ttk.Frame(self.mytabcontrol)
        self.devola_tab.columnconfigure(0, weight=1, minsize=340)
        self.devola_tab.columnconfigure(1, weight=10)
        self.devola_tab.rowconfigure(0, weight=1)
        
        self.mytabcontrol.add(self.alumno_tab, text ='Alumnos')
        self.mytabcontrol.add(self.pedidoli_tab, text ='Pedidos de Libros')
        self.mytabcontrol.add(self.pedidola_tab, text ='Pedidos de Laminas')
        self.mytabcontrol.add(self.devoli_tab, text ='Devoluciones Libros')
        self.mytabcontrol.add(self.devola_tab, text ='Devoluciones Laminas')
        
        self.mytabcontrol.grid(column=0, row=0, padx=10, pady=10, sticky='nswe')
        
        self.content()
        
    def content(self):
        #! Funciones label
        alumno1p_frame = ttk.LabelFrame(self.alumno_tab, text='Información Alumno', bootstyle='dark')
        alumno1p_frame.grid(column=0, row=0, padx=5, pady=5, sticky='nsw')
        alumno1p_frame.columnconfigure(0, weight=1, minsize=180)
        alumno1p_frame.columnconfigure(1, weight=1, minsize=180)
        
        alumno2p_frame = ttk.LabelFrame(self.alumno_tab, text='Visualizacion', bootstyle='dark')
        alumno2p_frame.grid(column=1, row=0, padx=5, pady=5, sticky='nsew')
        alumno2p_frame.columnconfigure(0, weight=1)
        alumno2p_frame.rowconfigure(0, weight=0)
        alumno2p_frame.rowconfigure(1, weight=10)
        
        peli1p_frame = ttk.LabelFrame(self.pedidoli_tab, text='Informacion Pedido', bootstyle='dark')
        peli1p_frame.grid(column=0, row=0, padx=5, pady=5, sticky='ns')
        peli1p_frame.columnconfigure(0, weight=1, minsize=139)
        peli1p_frame.columnconfigure(1, weight=1, minsize=185)
        
        peli2p_frame = ttk.LabelFrame(self.pedidoli_tab, text='Visualizacion', bootstyle='dark')
        peli2p_frame.grid(column=1, row=0, padx=5, pady=5, sticky='nsew')
        peli2p_frame.columnconfigure(0, weight=1)
        peli2p_frame.rowconfigure(0, weight=0)
        peli2p_frame.rowconfigure(1, weight=10)
        peli2p_frame.rowconfigure(2, weight=0)
        peli2p_frame.rowconfigure(3, weight=10)
        
        pela1p_frame = ttk.LabelFrame(self.pedidola_tab, text='Informacion Pedido', bootstyle='dark')
        pela1p_frame.grid(column=0, row=0, padx=5, pady=5, sticky='ns')
        pela1p_frame.columnconfigure(0, weight=1, minsize=139)
        pela1p_frame.columnconfigure(1, weight=1, minsize=185)
        
        pela2p_frame = ttk.LabelFrame(self.pedidola_tab, text='Visualizacion', bootstyle='dark')
        pela2p_frame.grid(column=1, row=0, padx=5, pady=5, sticky='nsew')
        pela2p_frame.columnconfigure(0, weight=1)
        pela2p_frame.rowconfigure(0, weight=0)
        pela2p_frame.rowconfigure(1, weight=10)
        pela2p_frame.rowconfigure(2, weight=0)
        pela2p_frame.rowconfigure(3, weight=10)
        
        devoli1p_frame = ttk.LabelFrame(self.devoli_tab, text='Funciones', bootstyle='dark')
        devoli1p_frame.grid(column=0, row=0, padx=5, pady=5, sticky='ns')
        devoli1p_frame.columnconfigure(0, weight=1, minsize=139)
        devoli1p_frame.columnconfigure(1, weight=1, minsize=185)
        
        devoli2p_frame = ttk.LabelFrame(self.devoli_tab, text='Visualizacion', bootstyle='dark')
        devoli2p_frame.grid(column=1, row=0, padx=5, pady=5, sticky='nsew')
        devoli2p_frame.columnconfigure(0, weight=1)
        devoli2p_frame.rowconfigure(0, weight=0)
        devoli2p_frame.rowconfigure(1, weight=10)      
        
        devola1p_frame = ttk.LabelFrame(self.devola_tab, text='Funciones', bootstyle='dark')
        devola1p_frame.grid(column=0, row=0, padx=5, pady=5, sticky='ns')
        devola1p_frame.columnconfigure(0, weight=1, minsize=139)
        devola1p_frame.columnconfigure(1, weight=1, minsize=185)
        
        devola2p_frame = ttk.LabelFrame(self.devola_tab, text='Visualizacion', bootstyle='dark')
        devola2p_frame.grid(column=1, row=0, padx=5, pady=5, sticky='nsew')
        devola2p_frame.columnconfigure(0, weight=1)
        devola2p_frame.rowconfigure(0, weight=0)
        devola2p_frame.rowconfigure(1, weight=10)              

        self.venalu.seccion_uno(alumno1p_frame)
        self.venalu.seccion_dos(alumno2p_frame)
        self.pedlib.seccion_uno(peli1p_frame)
        self.pedlib.seccion_dos(peli2p_frame)
        self.pedlam.seccion_uno(pela1p_frame)
        self.pedlam.seccion_dos(pela2p_frame)
        self.devlib.seccion_uno(devoli1p_frame)
        self.devlib.seccion_dos(devoli2p_frame)
        self.devlam.seccion_uno(devola1p_frame)
        self.devlam.seccion_dos(devola2p_frame)
        