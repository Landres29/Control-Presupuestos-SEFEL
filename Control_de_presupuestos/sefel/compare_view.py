import tkinter as tk
from tkinter import ttk

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

from .database import obtener_resumen_costos


class CompareView:

    def __init__(self, ventana, usuario, obra_seleccionada=None):
        self.ventana = ventana
        self.usuario = usuario
        self.obra_seleccionada = obra_seleccionada

        self.limpiar()
        self.crear_interfaz()

    def limpiar(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def crear_interfaz(self):
        self.crear_barra_superior()

        cuerpo = tk.Frame(
            self.ventana,
            bg=COLOR_FONDO
        )

        cuerpo.pack(
            fill="both",
            expand=True
        )

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
        ).pack(
            side="left",
            padx=25
        )

        tk.Label(
            barra,
            text="Aplicación de escritorio",
            bg=COLOR_PRINCIPAL,
            fg=COLOR_BLANCO,
            font=("Arial", 9)
        ).pack(
            side="right",
            padx=25
        )

    def crear_menu(self, cuerpo):
        menu = tk.Frame(
            cuerpo,
            bg=COLOR_BLANCO,
            width=170
        )

        menu.pack(
            side="left",
            fill="y"
        )

        menu.pack_propagate(False)

        tk.Label(
            menu,
            text="MENÚ PRINCIPAL",
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO_SECUNDARIO,
            font=("Arial", 8, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(20, 10)
        )

        opciones = [
            ("Obras", self.ir_obras),
            ("Presupuestos", self.ir_presupuestos),
            ("Gastos", self.ir_gastos),
            ("Comparar costos", None)
        ]

        for texto, comando in opciones:
            seleccionado = texto == "Comparar costos"

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
            text="COMPARACIÓN DE COSTOS",
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO,
            font=FUENTE_TITULO
        ).pack(anchor="w")

        tk.Frame(
            contenido,
            bg=COLOR_LINEA,
            height=2
        ).pack(
            fill="x",
            pady=(8, 20)
        )

        self.crear_tabla(contenido)

    def crear_tabla(self, contenido):
        panel = tk.Frame(
            contenido,
            bg=COLOR_BLANCO,
            bd=1,
            relief="solid",
            padx=15,
            pady=15
        )

        panel.pack(
            fill="both",
            expand=True
        )

        tk.Label(
            panel,
            text="Resumen por obra",
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO,
            font=("Arial", 14, "bold")
        ).pack(
            anchor="w",
            pady=(0, 10)
        )

        # Buscador
        tk.Label(
            panel,
            text="Buscar obra",
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO,
            font=FUENTE_NORMAL_NEGRITA
        ).pack(
            anchor="w"
        )

        self.entrada_busqueda = tk.Entry(
            panel,
            font=FUENTE_ENTRADA
        )

        self.entrada_busqueda.pack(
            fill="x",
            pady=(5, 15),
            ipady=5
        )

        self.entrada_busqueda.bind(
            "<KeyRelease>",
            self.filtrar_comparacion
        )

        columnas = (
            "obra",
            "presupuesto",
            "gastos",
            "diferencia",
            "estado"
        )

        self.tabla = ttk.Treeview(
            panel,
            columns=columnas,
            show="headings"
        )

        self.tabla.heading(
            "obra",
            text="Obra"
        )

        self.tabla.heading(
            "presupuesto",
            text="Presupuesto"
        )

        self.tabla.heading(
            "gastos",
            text="Gastos"
        )

        self.tabla.heading(
            "diferencia",
            text="Diferencia"
        )

        self.tabla.heading(
            "estado",
            text="Estado"
        )

        self.tabla.column(
            "obra",
            width=220
        )

        self.tabla.column(
            "presupuesto",
            width=150,
            anchor="e"
        )

        self.tabla.column(
            "gastos",
            width=150,
            anchor="e"
        )

        self.tabla.column(
            "diferencia",
            width=150,
            anchor="e"
        )

        self.tabla.column(
            "estado",
            width=130,
            anchor="center"
        )

        self.tabla.pack(
            fill="both",
            expand=True
        )

        tk.Label(
            panel,
            text="Diferencia = presupuesto - gastos",
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO_SECUNDARIO,
            font=FUENTE_NORMAL
        ).pack(
            anchor="w",
            pady=(10, 0)
        )

        self.cargar_comparacion()

    def cargar_comparacion(self, filtro=""):
        for registro in self.tabla.get_children():
            self.tabla.delete(registro)

        datos = obtener_resumen_costos()

        filtro = filtro.lower().strip()

        fila_seleccionada = None

        for dato in datos:
            nombre = dato[1]
            presupuesto = dato[2]
            gastos = dato[3]

            if filtro != "" and filtro not in nombre.lower():
                continue

            diferencia = presupuesto - gastos

            if diferencia > 0:
                estado = "Superávit"
            elif diferencia < 0:
                estado = "Déficit"
            else:
                estado = "Equilibrado"

            fila = self.tabla.insert(
                "",
                "end",
                values=(
                    nombre,
                    f"$ {presupuesto:,.0f}",
                    f"$ {gastos:,.0f}",
                    f"$ {diferencia:,.0f}",
                    estado
                )
            )

            if (
                self.obra_seleccionada is not None
                and nombre == self.obra_seleccionada
            ):
                fila_seleccionada = fila

        if fila_seleccionada is not None:
            self.tabla.selection_set(fila_seleccionada)
            self.tabla.focus(fila_seleccionada)
            self.tabla.see(fila_seleccionada)

    def filtrar_comparacion(self, event=None):
        texto = self.entrada_busqueda.get()

        self.cargar_comparacion(texto)

    def ir_obras(self):
        from .main_view import MainView

        MainView(
            self.ventana,
            self.usuario
        )

    def ir_presupuestos(self):
        from .budget_view import BudgetView

        BudgetView(
            self.ventana,
            self.usuario
        )

    def ir_gastos(self):
        from .expenses_view import ExpensesView

        ExpensesView(
            self.ventana,
            self.usuario
        )