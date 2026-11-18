import tkinter as tk
from tkinter import ttk

from .styles import *


class CompareView:

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
            ("Presupuestos", self.ir_presupuestos),
            ("Gastos", self.ir_gastos),
            ("Comparar costos", None)
        ]

        for texto, comando in opciones:

            tk.Button(
                menu,
                text=texto,
                command=comando,
                bg="#e8f1f5" if texto == "Comparar costos" else COLOR_BLANCO,
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
            text="CONSULTA DE DATOS · COMPARACIÓN",
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
            padx=20,
            pady=20
        )

        panel.pack(fill="both", expand=True)

        tk.Label(
            panel,
            text="Obra consultada: Galpón A",
            bg=COLOR_BLANCO,
            font=FUENTE_NORMAL_NEGRITA
        ).pack(anchor="w", pady=(0, 15))

        columnas = (
            "partida",
            "presupuestado",
            "gastado",
            "diferencia"
        )

        tabla = ttk.Treeview(
            panel,
            columns=columnas,
            show="headings"
        )

        tabla.heading("partida", text="Partida")
        tabla.heading("presupuestado", text="Presupuestado")
        tabla.heading("gastado", text="Gastado")
        tabla.heading("diferencia", text="Diferencia")

        tabla.insert(
            "",
            "end",
            values=(
                "Materiales",
                "$ 500.000",
                "$ 550.000",
                "-$ 50.000"
            )
        )

        tabla.insert(
            "",
            "end",
            values=(
                "Mano de obra",
                "$ 800.000",
                "$ 750.000",
                "+$ 50.000"
            )
        )

        tabla.insert(
            "",
            "end",
            values=(
                "TOTAL",
                "$ 1.300.000",
                "$ 1.300.000",
                "$ 0"
            )
        )

        tabla.pack(fill="both", expand=True)

        tk.Label(
            panel,
            text="Diferencia = presupuesto inicial - gastos acumulados",
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO,
            font=FUENTE_NORMAL_NEGRITA
        ).pack(anchor="w", pady=(15, 3))

        tk.Label(
            panel,
            text="Una diferencia negativa indica gasto superior a lo presupuestado.",
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO_SECUNDARIO,
            font=FUENTE_NORMAL
        ).pack(anchor="w")

    def ir_obras(self):
        from .main_view import MainView
        MainView(self.ventana, self.usuario)

    def ir_presupuestos(self):
        from .budget_view import BudgetView
        BudgetView(self.ventana, self.usuario)

    def ir_gastos(self):
        from .expenses_view import ExpensesView
        ExpensesView(self.ventana, self.usuario)