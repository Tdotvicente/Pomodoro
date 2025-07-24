import customtkinter as ctk
from cronometro import Cronometro
from config import verde_vibrante

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        # Configurando Janela principal
        self.title("Pomodoro")
        self.geometry("400x400")
        self.resizable(False, False)

        # Instanciando cronômetro (lógica)
        self.Cronometro = Cronometro()
        self.rodando = False

        # Criando abas e interface
        self.Temporizador_var = ctk.StringVar(value=self.Cronometro.Formatar_cronometro(
            self.Cronometro.tempo
        ))
        self.Menu_projeto()
        self.Criar_interface_home
        self.Atualizar_estado_label()
        self.abas.set("Home")

        self.Temporizador_var = ctk.StringVar()
        self.Temporizador_var.set(self.Cronometro.Formatar_cronometro(
            self.Cronometro.tempo
        ))

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

    # Criando elementos da aba Home
    def Criar_interface_home(self):
        Menu_home = self.abas.tab("Home")

        # Criando Labels dentro da aba home
        self.rotulo_estado = ctk.CTkLabel(Menu_home, text="", font=("Sans-serif", 20))
        self.rotulo_estado.pack(pady=10)

    def Atualizar_estado_label(self):
        textos = {
            "Foco": "Hora de focar",
            "Pausa": "Hora de pausar",
            "Descanso": "Hora de descansar"
        }
        estado = self.Cronometro.estado
        self.Rotulo_estado.configure(text=textos.get(estado, ""))

    # Função que inicia o pomodoro
    def Iniciar_cronometro(self):
        if not self.Cronometro:
            self.rodando = True
            self.atualizar_contagem()

    # Função que encerra a função do pomodoro
    def Parar_cronometro(self):
        self.rodando = False
        self.cronometro_redefinir()
        self.Temporizador_var.set(self.Cronometro.Formatar_tempo())
        self.Atualizar_estado_label()

    # Atualizando cronometro por segundo
    def Atualizar_contagem(self):
        if not self.rodando:
            return

        if self.Cronometro.tempo >= 0:
            pass


if __name__ == "__main__":
    app = App()
    app.mainloop()
