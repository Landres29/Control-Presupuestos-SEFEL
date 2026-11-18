import tkinter as tk
from tkinter import messagebox

from .styles import (
    COLOR_PRINCIPAL,
    COLOR_BLANCO,
    COLOR_TEXTO,
    COLOR_TEXTO_SECUNDARIO,
    FUENTE_NORMAL,
    FUENTE_NORMAL_NEGRITA,
    FUENTE_ENTRADA
)

from .database import agregar_obra


class ObraForm:

    def __init__(self, ventana_principal, usuario, al_guardar):
        self.ventana_principal = ventana_principal
        self.usuario = usuario
        self.al_guardar = al_guardar

        self.ventana = tk.Toplevel()
        self.ventana.title("Registrar obra")
        self.ventana.geometry("450x320")
        self.ventana.resizable(False, False)

        self.crear_interfaz()

    def crear_interfaz(self):

        contenedor = tk.Frame(
            self.ventana,
            bg=COLOR_BLANCO,
            padx=25,
            pady=25
        )

        contenedor.pack(
            fill="both",
            expand=True
        )

        tk.Label(
            contenedor,
            text="Registrar nueva obra",
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO,
            font=("Arial", 15, "bold")
        ).pack(anchor="w")

        tk.Label(
            contenedor,
            text="Ingrese los datos básicos de la obra.",
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO_SECUNDARIO,
            font=FUENTE_NORMAL
        ).pack(
            anchor="w",
            pady=(5, 20)
        )

        tk.Label(
            contenedor,
            text="Nombre de la obra",
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO,
            font=FUENTE_NORMAL_NEGRITA
        ).pack(anchor="w")

        self.entrada_nombre = tk.Entry(
            contenedor,
            font=FUENTE_ENTRADA
        )

        self.entrada_nombre.pack(
            fill="x",
            ipady=5,
            pady=(5, 15)
        )

        tk.Label(
            contenedor,
            text="Descripción",
            bg=COLOR_BLANCO,
            fg=COLOR_TEXTO,
            font=FUENTE_NORMAL_NEGRITA
        ).pack(anchor="w")

        self.entrada_descripcion = tk.Entry(
            contenedor,
            font=FUENTE_ENTRADA
        )

        self.entrada_descripcion.pack(
            fill="x",
            ipady=5,
            pady=(5, 20)
        )

        botones = tk.Frame(
            contenedor,
            bg=COLOR_BLANCO
        )

        botones.pack(
            fill="x"
        )

        tk.Button(
            botones,
            text="Cancelar",
            command=self.ventana.destroy,
            width=12
        ).pack(
            side="right",
            padx=(10, 0)
        )

        tk.Button(
            botones,
            text="Guardar obra",
            command=self.guardar,
            bg=COLOR_PRINCIPAL,
            fg=COLOR_BLANCO,
            font=FUENTE_NORMAL_NEGRITA,
            width=14
        ).pack(
            side="right"
        )

    def guardar(self):

        nombre = self.entrada_nombre.get().strip()
        descripcion = self.entrada_descripcion.get().strip()

        if nombre == "":
            messagebox.showerror(
                "Dato requerido",
                "Debe ingresar el nombre de la obra."
            )
            return

        agregar_obra(
            nombre,
            descripcion
        )

        messagebox.showinfo(
            "Obra registrada",
            "La obra se guardó correctamente."
        )

        self.ventana.destroy()

        if self.al_guardar:
            self.al_guardar()