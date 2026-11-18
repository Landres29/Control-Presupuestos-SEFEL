import tkinter as tk
from tkinter import ttk, messagebox

from .styles import *


class BudgetView:

    def __init__(self, ventana, usuario):
        self.ventana = ventana
        self.usuario = usuario

        self.limpiar()
        self.crear_interfaz()

    def limpiar(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def crear_interfaz(self):

        barra = tk.Frame(
            self.ventana,
            bg=COLOR_PRINCIPAL,
            height=55
        )

        barra.pack(fill="x")
        barra.pack_propagate(False)

        tk.Label(
            barra,
            text="SEFEL | Control de presupuestos y gastos",
            bg=COLOR_PRINCIPAL,
            fg=COLOR_BLANCO,
            font=("Arial", 13, "bold")
        ).pack(side="left", padx=25)

        cuerpo = tk.Frame(
            self.ventana,
            bg=COLOR_FONDO
        )

        cuerpo.pack(fill="both", expand=True)

        menu = tk.Frame(
            cuerpo,
            bg=COLOR_BLANCO,
            width=170
        )

        menu.pack(side="left", fill="y")
        menu.pack_propagate(False)

        opciones = [
            ("Obras", self.ir_obras),
            ("Presupuestos", None),
            ("Gastos", self.ir_gastos),
            ("Comparar costos", self.ir_comparacion)
        ]

        for texto, comando in opciones:

            tk.Button(
                menu,
                text=texto,
                command=comando,
                bg="#e8f1f5" if texto == "Presupuestos" else COLOR_BLANCO,
                relief="flat",
                anchor="w",
                padx=20,
                pady=10
            ).pack(fill="x")

        contenido = tk.Frame(
            cuerpo,
            bg=COLOR_FONDO
        )

        contenido.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=25
        )

        tk.Label(
            contenido,
            text="PRESUPUESTO INICIAL",
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO,
            font=FUENTE_TITULO
        ).pack(anchor="w")

        tk.Frame(
            contenido,
            bg=COLOR_LINEA,
            height=2
        ).pack(fill="x", pady=(8, 20))

        panel = tk.Frame(
            contenido,
            bg=COLOR_BLANCO,
            bd=1,
            relief="solid",
            padx=25,
            pady=25
        )

        panel.pack(fill="x")

        tk.Label(
            panel,
            text="Obra",
            bg=COLOR_BLANCO,
            font=FUENTE_NORMAL_NEGRITA
        ).grid(row=0, column=0, sticky="w")

        self.obra = ttk.Combobox(
            panel,
            values=["Galpón A", "Montaje B", "Obra C"],
            state="readonly"
        )

        self.obra.grid(
            row=1,
            column=0,
            padx=(0, 15),
            pady=(5, 15)
        )

        tk.Label(
            panel,
            text="Partida",
            bg=COLOR_BLANCO,
            font=FUENTE_NORMAL_NEGRITA
        ).grid(row=0, column=1, sticky="w")

        self.partida = tk.Entry(panel)

        self.partida.grid(
            row=1,
            column=1,
            pady=(5, 15)
        )

        tk.Label(
            panel,
            text="Monto presupuestado",
            bg=COLOR_BLANCO,
            font=FUENTE_NORMAL_NEGRITA
        ).grid(row=2, column=0, sticky="w")

        self.monto = tk.Entry(panel)

        self.monto.grid(
            row=3,
            column=0,
            pady=(5, 15)
        )

        tk.Button(
            panel,
            text="Guardar presupuesto",
            command=self.guardar,
            bg=COLOR_PRINCIPAL,
            fg=COLOR_BLANCO
        ).grid(
            row=4,
            column=1,
            pady=20
        )

    def guardar(self):

        if not self.obra.get() or not self.partida.get() or not self.monto.get():

            messagebox.showerror(
                "Datos incompletos",
                "Debe completar todos los campos."
            )
            return

        messagebox.showinfo(
            "Registro guardado",
            "El presupuesto se guardó correctamente."
        )

    def ir_obras(self):
        from .main_view import MainView
        MainView(self.ventana, self.usuario)

    def ir_gastos(self):
        from .expenses_view import ExpensesView
        ExpensesView(self.ventana, self.usuario)

    def ir_comparacion(self):
        from .compare_view import CompareView
        CompareView(self.ventana, self.usuario)