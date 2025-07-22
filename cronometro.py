import customtkinter 
from config import foco_min, pequena_pausa, longa_pausa

class Cronometro():
    def __init__(self):
        self.tempo = foco_min
        self.estado = "Foco"
        self.volta = 1
        self.ciclo = 1

    # configurando a interface do cronometro
    def formatar_cronometro(self, segundos_restantes):
        return f'{segundos_restantes // 60}:{segundos_restantes % 60}'

    # configurando o processo do pomodoro
    def temporizador(self):
        if self.estado == "Foco":
            if self.volta % 4 != 0:
                self.estado = "Pausa"
                self.tempo = pequena_pausa

            else:
                self.estado = "Decanso"
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