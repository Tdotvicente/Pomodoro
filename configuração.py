import customtkinter as ctk
import time


ctk.set_appearance_mode("green")
ctk.set_default_color_theme("green")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.Configurar_janela()

    # Configurando Janela
    def Configurar_janela(self):
        self.title("Pomodoro")
        self.geometry("400x400")
        self.resizable(False, False)

    