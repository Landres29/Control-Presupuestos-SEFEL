import tkinter as tk

from sefel.login import LoginView


def main():
    ventana = tk.Tk()
    LoginView(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()