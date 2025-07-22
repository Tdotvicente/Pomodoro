import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


class App(ctk.CTk):

    # Criando variaveis globais dentro da classe (App)
    # Caso precise chama-las, use APP.[nome da variavel]
    tempo = 60
    Foco_min = 5
    Pequena_pausa = 5
    Longa_pausa = 15 * 60

    def __init__(self):
        super().__init__()
        self.tempo = App.Foco_min
        self.temporizador = ctk.StringVar()
        self.volta = 1  # Controla o tempo entre a Foco e Pequena Pausa
        self.ciclo = 1  # Controla 4 voltas e o fim da longa pausa
        # Diz qual estado (Foco, Pausa, Descanso) está ativo
        self.estado = "Foco"
        self.rodando = False  # Crontrola o cronometro

        self.Configurar_janela()
        self.Menu_projeto()
        self.Visualizar_cronometro()
        self.Cronometro()  # Inicia o cronômetro
        self.abas.set("Home")

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

    # Formatando o temporizador do cronometro
    def Formatar_cronometro(self, segundos_restantes):
        return f"{segundos_restantes // 60:02}:{segundos_restantes % 60:02}"

    # Função que inicia o cronometro
    def Iniciar_cronometro(self):
        if not self.rodando:
            self.rodando = True
            self.Cronometro()

    # função que faz parar o cronometro
    def Parar_cronometro(self):
        self.rodando = False
        self.tempo = App.Foco_min  # Volta para 25 minutos
        self.estado = "Foco"  # Volta para o estado inicial
        self.temporizador.set(self.Formatar_cronometro(
            self.tempo))  # Atualiza o visor do tempo
        self.Atualizar_label_estado()  # Atualiza o texto do estado

    # Criando funções do cronometro
    def Cronometro(self):
        menu_home = self.abas.tab("Home")

        def Atualizar_temporizador():
            # Para o timer imediatamemente
            if not self.rodando:
                return

            if self.tempo >= 0:
                self.temporizador.set(self.Formatar_cronometro(self.tempo))
                menu_home.after(1000, Atualizar_temporizador)
                self.tempo -= 1

            else:
                # Quando tempo acabar, alterar o estado
                if self.estado == "Foco":
                    if self.volta % 4 != 0:
                        self.estado = "Pausa"
                        self.tempo = App.Pequena_pausa
                    else:
                        self.estado = "Descanso"
                        self.tempo = App.Longa_pausa

                elif self.estado == "Pausa":
                    self.estado = "Foco"
                    self.tempo = App.Foco_min
                    self.volta += 1

                elif self.estado == "Descanso":
                    self.estado = "Foco"
                    self.tempo = App.Foco_min
                    self.ciclo += 1
                    self.volta = 1

                # Atualizar a Label do texto no cronometro
                self.Atualizar_label_estado()
                Atualizar_temporizador()

        Atualizar_temporizador()

    # Criando as funções que o usuario irá interagir na primeira aba
    def Visualizar_cronometro(self):
        menu_home = self.abas.tab("Home")

        self.rotulo_home = ctk.CTkLabel(
            menu_home, text="", text_color="#25DC71", font=("Sans-serif", 40, "bold"))
        self.rotulo_home.pack(pady=30)

        temporizador_label = ctk.CTkLabel(
            menu_home, textvariable=self.temporizador, text_color="#25DC71", font=("Sans-serif", 60, "bold"))
        temporizador_label.pack()

        self.Atualizar_label_estado()

        # Criando os botões para interação da intercafe do usuario
        # Criando botão iniciar
        botao_iniciar = ctk.CTkButton(
            menu_home, text="Inicar", command=self.Iniciar_cronometro)
        botao_iniciar.pack()

        # Criando botão parar
        botao_parar = ctk.CTkButton(
            menu_home, text="Parar", command=self.Parar_cronometro)
        botao_parar.pack()

    def Atualizar_label_estado(self):
        textos = {
            "Foco": "Hora de focar",
            "Pausa": "Faça uma pausa",
            "Descanso": "Hora de descansar"
        }
        self.rotulo_home.configure(text=textos.get(self.estado, ""))


if __name__ == "__main__":
    app = App()
    app.mainloop()
