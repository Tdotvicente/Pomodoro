from config import foco_min, pequena_pausa, longa_pausa

class Cronometro():
    def __init__(self):
        self.tempo = foco_min
        self.estado = "Foco"
        self.volta = 1
        self.ciclo = 1
        self.rodando = False

    ## Lógica de como funciona o pomodoro
    # configurando a interface do cronometro
    def formatar_cronometro(self, segundos_restantes):
        minutos = segundos_restantes // 60
        segundos = segundos_restantes % 60
        return f'{minutos:02d}:{segundos:02d}'

    # configurando o processo do pomodoro
    def fases_etapas(self):
        if self.estado == "Foco":
            if self.volta % 4 != 0:
                self.estado = "Pausa"
                self.tempo = pequena_pausa

            else:
                self.estado = "Descanso"
                self.tempo = longa_pausa

        elif self.estado == "Pausa":
            self.estado = "Foco"
            self.tempo = foco_min
            self.volta += 1

        elif self.estado == "Descanso":
            self.estado = "Foco"
            self.tempo = foco_min
            self.ciclo += 1
            self.volta = 1

    def proximo_estado(self):
        if self.estado == "Foco":
            return "Pausa" if self.volta % 4 != 0 else "Descanso"

        elif self.estado in ["Pausa", "Descanso"]:
            return "Foco"

    ## Pulando etapa
    # A função abaixo, é feita para pular certos momentos espeficicos
    # onde é feita para iginorar o periodo de pausa,indo direto para
    # outro momento de foco ou ignnorando momento de descanso e iniciando
    # um novo ciclo

    def pular_etapa(self):
        if self.estado == "Foco":
            self.fases_etapas()
            self.fases_etapas()

        elif self.estado in ("Pausa", "Descanso"):
            self.fases_etapas()

    ## Ativando e desativando o programa
    # Iniciando o cronômetro do pomodoro
    def iniciar_cronometro(self):
        self.rodando = True

    def parar_cronometro(self):
        self.rodando = False

    def reiniciar_cronometro(self):
        self.__init__()
