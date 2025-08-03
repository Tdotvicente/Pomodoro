import customtkinter as ctk
from cronometro import Cronometro
from mensagem import dialogo_mensagem, estados_ui
from config import verde_vibrante
from CTkMessagebox import CTkMessagebox

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
        self.Criar_interface_home()
        self.Atualizar_estado_label()
        self.abas.set("Home")

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
        self.rotulo_estado = ctk.CTkLabel(
            Menu_home, text="", font=("Sans-serif", 30, "bold"))
        self.rotulo_estado.pack(pady=10)

        self.rotulo_tempo = ctk.CTkLabel(Menu_home, textvariable=self.Temporizador_var, font=(
            "Sans-serif", 30, "bold"), text_color=verde_vibrante)
        self.rotulo_tempo.pack(pady=10)

        self.botao_iniciar = ctk.CTkButton(
            Menu_home, text="Iniciar", font=("Sans-serif", 20, "bold"), command=self.Iniciar_cronometro)
        self.botao_iniciar.pack(pady=10)

        self.botao_encerrar = ctk.CTkButton(
            Menu_home, text="Parar", font=("Sans-serif", 20, "bold"), command=self.Parar_cronometro)
        self.botao_encerrar.pack(pady=10)

    def Atualizar_estado_label(self):
        estado = self.Cronometro.estado
        texto = estados_ui.get(estado, "")
        self.rotulo_estado.configure(text=texto)

    # Função que inicia o pomodoro
    def Iniciar_cronometro(self):
        if not self.Cronometro.rodando:
            self.Cronometro.iniciar_cronometro()
            self.botao_iniciar.configure(state="disabled")
            self.botao_encerrar.configure(state="normal")
            self.Atualizar_contagem()

    # Função que encerra a função do pomodoro
    def Parar_cronometro(self):
        self.Cronometro.parar_cronometro()
        self.Reiniciar_cronometro()

    # Reiniciando cronômetro
    def Reiniciar_cronometro(self):
        self.Cronometro.reiniciar_cronometro()
        self.Temporizador_var.set(
            self.Cronometro.Formatar_cronometro(self.Cronometro.tempo))
        self.Atualizar_estado_label()
        self.botao_iniciar.configure(state="normal")
        self.botao_encerrar.configure(state="disabled")

    # Atualizando cronometro por segundo

    def Atualizar_contagem(self):
        if not self.Cronometro.rodando:
            return

        if self.Cronometro.tempo >= 0:
            self.Cronometro.tempo -= 1
            self.Temporizador_var.set(
                self.Cronometro.Formatar_cronometro(self.Cronometro.tempo))
            self.after(1000, self.Atualizar_contagem)

        else:
            # Bloco feito para funcionar antes de mudar de foco
            if self.Cronometro.estado == "Foco":
                self.rodando = False

                resposta = CTkMessagebox(title=dialogo_mensagem["confirmação"]["titúlo"],
                                        message=dialogo_mensagem["confirmação"]["mensagem"], icon="question",
                                        option_1=dialogo_mensagem["confirmação"]["opções"][0],
                                        option_2=dialogo_mensagem["confirmação"]["opções"][1])

                if resposta.get() == "Sim":
                    self.Cronometro.Fases_etapas()
                    self.Atualizar_estado_label()
                    self.Temporizador_var.set(
                        self.Cronometro.Formatar_cronometro(self.Cronometro.tempo))
                    self.rodando = True
                    self.after(1000, self.Atualizar_contagem)

                else:
                    self.Parar_cronometro()

            else:
                self.Cronometro.Fases_etapas()
                self.Atualizar_estado_label()
                self.Temporizador_var.set(
                    self.Cronometro.Formatar_cronometro(self.Cronometro.tempo))
                self.after(1000, self.Atualizar_contagem)


if __name__ == "__main__":
    app = App()
    app.mainloop()
