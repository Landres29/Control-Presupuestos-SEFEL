import tkinter as tk

from sefel.login import LoginView
from sefel.database import crear_base_datos


def main():

    crear_base_datos()

    ventana = tk.Tk()

    LoginView(ventana)

    ventana.mainloop()


if __name__ == "__main__":
    main()