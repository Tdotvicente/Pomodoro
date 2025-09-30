import customtkinter as ctk

# Configurações globais
foco_min = 10
pequena_pausa = 5
longa_pausa = 15
volta_numero = 4

def evento_foco(master):
    global foco_min
    def set_foco_min(value):
        global foco_min
        return value * 60

    slider_foco = ctk.CTkSlider(master=master, from_=10, to=60, command=set_foco_min)
    slider_foco.pack(padx=20, pady=20)
    slider_foco.set(25)

def evento_pausa(master):
    global pequena_pausa
    def set_pausa_min(value):
        global pequena_pausa
        return value * 60

    slider_pausa = ctk.CTkSlider(master=master, from_=5, to=20, command=set_pausa_min)
    slider_pausa.pack(padx=40, pady=20)
    slider_pausa.set(5)

def evento_descanso(master):
    global longa_pausa
    def set_descanso_min(value):
        global longa_pausa
        return value * 60

    slider_descanso = ctk.CTkSlider(master=master, from_=10, to=60, command=set_descanso_min)
    slider_descanso.pack(padx=60, pady=20)
    slider_descanso.set(15)

def evento_volta(master):
    global volta_numero
    def set_volta_numero(value):
        global volta_numero
        return value
    
    slider_volta = ctk.CTkSlider(master=master, from_=2, to=10, command=set_volta_numero)
    slider_volta.pack()
    slider_volta.set(4)

# Cores
verde_vibrante = "#25DC71"
