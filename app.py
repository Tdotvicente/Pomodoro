import customtkinter as ctk
from cronometro import Cronometro
from config import verde_vibrante

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.cronometro = Cronometro
        self.Configurar_janela()
        self.Menu_projeto()
        self.rodando = False

    # Configurando Janela
    def Configurar_janela(self):
        self.title("Pomodoro")
        self.geometry("400x400")
        self.resizable(False, False)

    # Enquadramento dos botões usando tabview
    def Menu_projeto(self):
        self.abas = ctk.CTkTabview(self, width=390, height=390)
        self.abas.pack()
        self.abas.add("Home")
        self.abas.tab("Home")
        self.abas.add("Configuração")
        self.abas.add("Temas")

        for botao in self.abas._segmented_button._buttons_dict.values():
            botao.configure(width=100, height=30,
                        font=("Sans-serif", 16, "bold"))

    # Função que inicia o pomodoro
    def Iniciar_cronometro(self):
        if not self.cronometro:
            self.rodando = True
            self.cronometro()

    # Função que encerra a função do pomodoro
    def Parar_cronometro(self):
        self.rodando = False
        self.

if __name__ == "__main__":
    app = App()
    app.mainloop()