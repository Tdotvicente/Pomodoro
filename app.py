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

        self.title("Pomodoro")
        self.geometry("400x400")
        self.resizable(False, False)

        self.cronometro = Cronometro()
        self.rodando = False

        self.temporizador_var = ctk.StringVar(value=self.cronometro.formatar_cronometro(
            self.cronometro.tempo
        ))

        self.menu_projeto()
        self.criar_interface_home()
        self.atualizar_estado_label()
        self.abas.set("Home")

    def menu_projeto(self):
        self.abas = ctk.CTkTabview(self, width=390, height=390)
        self.abas.pack()
        self.abas.add("Home")
        self.abas.tab("Home")
        self.abas.add("Configuração")
        self.abas.add("Temas")

        for botao in self.abas._segmented_button._buttons_dict.values():
            botao.configure(width=100, height=30, font=("Sans-serif", 16, "bold"))

    def criar_interface_home(self):
        menu_home = self.abas.tab("Home")

        self.rotulo_estado = ctk.CTkLabel(menu_home, text="", font=("Sans-serif", 30, "bold"))
        self.rotulo_estado.pack(pady=10)

        self.rotulo_tempo = ctk.CTkLabel(menu_home, textvariable=self.temporizador_var, font=(
            "Sans-serif", 30, "bold"), text_color=verde_vibrante)
        self.rotulo_tempo.pack(pady=10)

        self.botao_iniciar = ctk.CTkButton(
            menu_home, text="Iniciar", font=("Sans-serif", 20, "bold"), command=self.iniciar_cronometro)
        self.botao_iniciar.pack(pady=10)

        self.botao_encerrar = ctk.CTkButton(
            menu_home, text="Parar", font=("Sans-serif", 20, "bold"), command=self.parar_cronometro)
        self.botao_encerrar.pack(pady=10)

    def atualizar_estado_label(self):
        estado = self.cronometro.estado
        texto = estados_ui.get(estado, "")
        self.rotulo_estado.configure(text=texto)

    def iniciar_cronometro(self):
        if not self.cronometro.rodando:
            self.cronometro.iniciar_cronometro()
            self.botao_iniciar.configure(state="disabled")
            self.botao_encerrar.configure(state="normal")
            self.atualizar_contagem()

    def parar_cronometro(self):
        self.cronometro.parar_cronometro()
        self.reiniciar_cronometro()

    def reiniciar_cronometro(self):
        self.cronometro.reiniciar_cronometro()
        self.temporizador_var.set(self.cronometro.formatar_cronometro(self.cronometro.tempo))
        self.atualizar_estado_label()
        self.botao_iniciar.configure(state="normal")
        self.botao_encerrar.configure(state="disabled")

    def atualizar_contagem(self):
        if not self.cronometro.rodando:
            return

        if self.cronometro.tempo >= 0:
            self.cronometro.tempo -= 1
            self.temporizador_var.set(self.cronometro.formatar_cronometro(self.cronometro.tempo))
            self.after(1000, self.atualizar_contagem)
        else:
            if self.cronometro.estado == "Foco":
                self.rodando = False
                resposta = CTkMessagebox(title=dialogo_mensagem["confirmação"]["titúlo"],
                                         message=dialogo_mensagem["confirmação"]["mensagem"], icon="question",
                                         option_1=dialogo_mensagem["confirmação"]["opções"][0],
                                         option_2=dialogo_mensagem["confirmação"]["opções"][1])
                if resposta.get() == "Sim":
                    self.cronometro.fases_etapas()
                    self.atualizar_estado_label()
                    self.temporizador_var.set(self.cronometro.formatar_cronometro(self.cronometro.tempo))
                    self.rodando = True
                    self.after(1000, self.atualizar_contagem)
                else:
                    self.parar_cronometro()
            else:
                self.cronometro.fases_etapas()
                self.atualizar_estado_label()
                self.temporizador_var.set(self.cronometro.formatar_cronometro(self.cronometro.tempo))
                self.after(1000, self.atualizar_contagem)

if __name__ == "__main__":
    app = App()
    app.mainloop()
