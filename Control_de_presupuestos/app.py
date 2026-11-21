import tkinter as tk
from tkinter import messagebox

from sefel.login import LoginView
from sefel.database import (
    crear_base_datos,
    base_datos_existe
)


def main():

    ventana = tk.Tk()

    # Comprobar que exista la base de datos original
    if not base_datos_existe():

        ventana.withdraw()

        messagebox.showerror(
            "Base de datos no encontrada",
            "No se encontró la base de datos sefel.db.\n\n"
            "La aplicación no puede continuar para evitar crear "
            "una base de datos vacía."
        )

        ventana.destroy()
        return

    # Comprobar y mantener las tablas existentes
    crear_base_datos()

    LoginView(ventana)

    ventana.mainloop()


if __name__ == "__main__":
    main()