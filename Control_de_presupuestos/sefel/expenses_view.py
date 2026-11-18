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

from .database import (
    obtener_obras,
    agregar_gasto,
    obtener_gastos
)


class ExpensesView:

    def __init__(self, ventana, usuario):
        self.ventana = ventana
        self.usuario = usuario
        self.obras = []

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
            text="GASTOS",
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

        self.crear_formulario(contenido)
        self.crear_tabla(contenido)

    def crear_formulario(self, contenido):
        panel = tk.Frame(
            contenido,
            bg=COLOR_BLANCO,
            bd=1,
            relief="solid",
            padx=20,
            pady=20
        )

        panel.pack(
            fill="x",
            pady=(0, 20)
        )

        tk.Label(
            panel,
            text="Registrar gasto real",
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO,
            font=("Arial", 14, "bold")
        ).grid(
            row=0,
            column=0,
            columnspan=3,
            sticky="w",
            pady=(0, 15)
        )

        tk.Label(
            panel,
            text="Obra",
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO,
            font=FUENTE_NORMAL_NEGRITA
        ).grid(
            row=1,
            column=0,
            sticky="w",
            padx=5
        )

        self.combo_obra = ttk.Combobox(
            panel,
            state="readonly",
            font=FUENTE_NORMAL
        )

        self.combo_obra.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=5,
            pady=(5, 10)
        )

        tk.Label(
            panel,
            text="Partida",
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO,
            font=FUENTE_NORMAL_NEGRITA
        ).grid(
            row=1,
            column=1,
            sticky="w",
            padx=5
        )

        self.entrada_partida = tk.Entry(
            panel,
            font=FUENTE_ENTRADA
        )

        self.entrada_partida.grid(
            row=2,
            column=1,
            sticky="ew",
            padx=5,
            pady=(5, 10)
        )

        tk.Label(
            panel,
            text="Concepto",
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO,
            font=FUENTE_NORMAL_NEGRITA
        ).grid(
            row=1,
            column=2,
            sticky="w",
            padx=5
        )

        self.entrada_concepto = tk.Entry(
            panel,
            font=FUENTE_ENTRADA
        )

        self.entrada_concepto.grid(
            row=2,
            column=2,
            sticky="ew",
            padx=5,
            pady=(5, 10)
        )

        tk.Label(
            panel,
            text="Monto",
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO,
            font=FUENTE_NORMAL_NEGRITA
        ).grid(
            row=3,
            column=0,
            sticky="w",
            padx=5
        )

        self.entrada_monto = tk.Entry(
            panel,
            font=FUENTE_ENTRADA
        )

        self.entrada_monto.grid(
            row=4,
            column=0,
            sticky="ew",
            padx=5,
            pady=(5, 10)
        )

        tk.Label(
            panel,
            text="Fecha",
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO,
            font=FUENTE_NORMAL_NEGRITA
        ).grid(
            row=3,
            column=1,
            sticky="w",
            padx=5
        )

        self.entrada_fecha = tk.Entry(
            panel,
            font=FUENTE_ENTRADA
        )

        self.entrada_fecha.grid(
            row=4,
            column=1,
            sticky="ew",
            padx=5,
            pady=(5, 10)
        )

        self.entrada_fecha.insert(
            0,
            "18-11-2026"
        )

        tk.Button(
            panel,
            text="Guardar gasto",
            command=self.guardar_gasto,
            bg=COLOR_PRINCIPAL,
            fg=COLOR_BLANCO,
            font=FUENTE_NORMAL_NEGRITA
        ).grid(
            row=4,
            column=2,
            sticky="e",
            padx=5
        )

        panel.columnconfigure(0, weight=1)
        panel.columnconfigure(1, weight=1)
        panel.columnconfigure(2, weight=1)

        self.cargar_obras()

    def crear_tabla(self, contenido):
        panel_tabla = tk.Frame(
            contenido,
            bg=COLOR_BLANCO,
            bd=1,
            relief="solid",
            padx=15,
            pady=15
        )

        panel_tabla.pack(
            fill="both",
            expand=True
        )

        columnas = (
            "obra",
            "partida",
            "concepto",
            "monto",
            "fecha"
        )

        self.tabla = ttk.Treeview(
            panel_tabla,
            columns=columnas,
            show="headings"
        )

        self.tabla.heading("obra", text="Obra")
        self.tabla.heading("partida", text="Partida")
        self.tabla.heading("concepto", text="Concepto")
        self.tabla.heading("monto", text="Monto")
        self.tabla.heading("fecha", text="Fecha")

        self.tabla.column("obra", width=160)
        self.tabla.column("partida", width=160)
        self.tabla.column("concepto", width=220)
        self.tabla.column("monto", width=120, anchor="e")
        self.tabla.column("fecha", width=110, anchor="center")

        self.tabla.pack(
            fill="both",
            expand=True
        )

        self.cargar_gastos()

    def cargar_obras(self):
        self.obras = obtener_obras()

        nombres = [
            obra[1]
            for obra in self.obras
        ]

        self.combo_obra["values"] = nombres

    def guardar_gasto(self):
        indice = self.combo_obra.current()

        partida = self.entrada_partida.get().strip()
        concepto = self.entrada_concepto.get().strip()
        monto_texto = self.entrada_monto.get().strip()
        fecha = self.entrada_fecha.get().strip()

        if (
            indice == -1
            or partida == ""
            or concepto == ""
            or monto_texto == ""
            or fecha == ""
        ):
            messagebox.showerror(
                "Datos incompletos",
                "Debe completar todos los campos."
            )
            return

        try:
            monto = float(monto_texto)

            if monto <= 0:
                raise ValueError

        except ValueError:
            messagebox.showerror(
                "Monto inválido",
                "El monto debe ser un número mayor que cero."
            )
            return

        obra_id = self.obras[indice][0]

        agregar_gasto(
            obra_id,
            partida,
            concepto,
            monto,
            fecha
        )

        messagebox.showinfo(
            "Gasto registrado",
            "El gasto se guardó correctamente."
        )

        self.entrada_partida.delete(0, tk.END)
        self.entrada_concepto.delete(0, tk.END)
        self.entrada_monto.delete(0, tk.END)

        self.cargar_gastos()

    def cargar_gastos(self):
        for registro in self.tabla.get_children():
            self.tabla.delete(registro)

        gastos = obtener_gastos()

        for gasto in gastos:
            nombre_obra = gasto[1]
            partida = gasto[2]
            concepto = gasto[3]
            monto = gasto[4]
            fecha = gasto[5]

            self.tabla.insert(
                "",
                "end",
                values=(
                    nombre_obra,
                    partida,
                    concepto,
                    f"$ {monto:,.0f}",
                    fecha
                )
            )

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

    def ir_comparacion(self):
        from .compare_view import CompareView

        CompareView(
            self.ventana,
            self.usuario
        )