import tkinter as tk
from tkinter import ttk, messagebox

from .styles import (
    COLOR_PRINCIPAL,
    COLOR_FONDO,
    COLOR_BLANCO,
    COLOR_TEXTO,
    COLOR_TEXTO_SECUNDARIO,
    COLOR_LINEA,
    FUENTE_TITULO,
    FUENTE_NORMAL,
    FUENTE_NORMAL_NEGRITA,
    FUENTE_ENTRADA
)


class ExpensesView:

    def __init__(self, ventana, usuario):
        self.ventana = ventana
        self.usuario = usuario

        self.limpiar()
        self.crear_interfaz()

    def limpiar(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def crear_interfaz(self):
        self.crear_barra_superior()

        cuerpo = tk.Frame(self.ventana, bg=COLOR_FONDO)
        cuerpo.pack(fill="both", expand=True)

        self.crear_menu(cuerpo)
        self.crear_contenido(cuerpo)

    def crear_barra_superior(self):
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

        tk.Label(
            barra,
            text="Aplicación de escritorio",
            bg=COLOR_PRINCIPAL,
            fg=COLOR_BLANCO,
            font=("Arial", 9)
        ).pack(side="right", padx=25)

    def crear_menu(self, cuerpo):

        menu = tk.Frame(
            cuerpo,
            bg=COLOR_BLANCO,
            width=170
        )

        menu.pack(side="left", fill="y")
        menu.pack_propagate(False)

        tk.Label(
            menu,
            text="MENÚ PRINCIPAL",
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO_SECUNDARIO,
            font=("Arial", 8, "bold")
        ).pack(anchor="w", padx=20, pady=(20, 10))

        opciones = [
            ("Obras", self.ir_obras),
            ("Presupuestos", self.ir_presupuestos),
            ("Gastos", None),
            ("Comparar costos", self.ir_comparacion)
        ]

        for texto, comando in opciones:

            seleccionado = texto == "Gastos"

            tk.Button(
                menu,
                text=texto,
                command=comando,
                bg="#e8f1f5" if seleccionado else COLOR_BLANCO,
                fg=COLOR_TEXTO,
                relief="flat",
                anchor="w",
                padx=20,
                pady=8,
                font=FUENTE_NORMAL_NEGRITA if seleccionado else FUENTE_NORMAL
            ).pack(fill="x")

    def crear_contenido(self, cuerpo):

        contenido = tk.Frame(
            cuerpo,
            bg=COLOR_FONDO
        )

        contenido.pack(
            side="left",
            fill="both",
            expand=True,
            padx=30,
            pady=25
        )

        tk.Label(
            contenido,
            text="INGRESO DE DATOS",
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
            pady=20
        )

        panel.pack(fill="x")

        tk.Label(
            panel,
            text="Registrar gasto real",
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO,
            font=("Arial", 14, "bold")
        ).grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="w",
            pady=(0, 5)
        )

        tk.Label(
            panel,
            text="El gasto se asocia a una obra y a una partida presupuestaria.",
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO_SECUNDARIO,
            font=FUENTE_NORMAL
        ).grid(
            row=1,
            column=0,
            columnspan=2,
            sticky="w",
            pady=(0, 20)
        )

        self.obra = ttk.Combobox(
            panel,
            values=["Galpón A", "Montaje B", "Obra C"],
            state="readonly"
        )

        self.partida = ttk.Combobox(
            panel,
            values=["Materiales", "Mano de obra", "Equipos"],
            state="readonly"
        )

        self.concepto = tk.Entry(panel, font=FUENTE_ENTRADA)
        self.monto = tk.Entry(panel, font=FUENTE_ENTRADA)
        self.fecha = tk.Entry(panel, font=FUENTE_ENTRADA)

        self.crear_campo(panel, "Obra", self.obra, 2, 0)
        self.crear_campo(panel, "Partida", self.partida, 2, 1)

        self.crear_campo(panel, "Concepto", self.concepto, 4, 0)
        self.crear_campo(panel, "Monto (CLP)", self.monto, 4, 1)

        self.crear_campo(panel, "Fecha", self.fecha, 6, 0)

        self.fecha.insert(0, "26-10-2026")

        tk.Button(
            panel,
            text="Guardar gasto",
            command=self.guardar,
            bg=COLOR_PRINCIPAL,
            fg=COLOR_BLANCO,
            font=FUENTE_NORMAL_NEGRITA,
            width=18
        ).grid(
            row=7,
            column=1,
            sticky="e",
            pady=(25, 0)
        )

        panel.columnconfigure(0, weight=1)
        panel.columnconfigure(1, weight=1)

    def crear_campo(self, panel, texto, campo, fila, columna):

        tk.Label(
            panel,
            text=texto,
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO,
            font=FUENTE_NORMAL_NEGRITA
        ).grid(
            row=fila,
            column=columna,
            sticky="w",
            padx=10
        )

        campo.grid(
            row=fila + 1,
            column=columna,
            sticky="ew",
            padx=10,
            pady=(5, 15)
        )

    def guardar(self):

        if (
            not self.obra.get()
            or not self.partida.get()
            or not self.concepto.get()
            or not self.monto.get()
            or not self.fecha.get()
        ):
            messagebox.showerror(
                "Datos incompletos",
                "Debe completar todos los campos."
            )
            return

        try:
            monto = float(self.monto.get())

            if monto <= 0:
                raise ValueError

        except ValueError:
            messagebox.showerror(
                "Monto inválido",
                "El monto debe ser mayor que cero."
            )
            return

        messagebox.showinfo(
            "Registro guardado",
            "El gasto se guardó correctamente."
        )

    def ir_obras(self):
        from .main_view import MainView
        MainView(self.ventana, self.usuario)

    def ir_presupuestos(self):
        from .budget_view import BudgetView
        BudgetView(self.ventana, self.usuario)

    def ir_comparacion(self):
        from .compare_view import CompareView
        CompareView(self.ventana, self.usuario)