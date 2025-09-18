# Mensagem usada para guiar as o estado atual do pomodoro e exibida ao usuário
estados_ui = {
    "Foco": "Hora de focar",
    "Pausa": "Hora de pausar",
    "Descanso": "Hora de descansar"
}

# Mensagens exibidas, em caixa de dialogos, entre troca de momentos.
# Elas têm a função de mostrar que uma etapas
# A interação será feita para iniciar ou pular um ciclo
dialogo_mensagem = {
    "ação": {
        "titúlo": "Pomodoro",
        "Pausar": "O tempo acabou.\nfazer pequeno descanso?",
        "Focar": "O descanso Acabou.\nDeseja começar a focar?",
        "Descansar": "O ciclo acabou.\nVamos descansar",
        "Novo_ciclo": "Deseja começar\num novo ciclo",
        "opções": ["[1] Sim", "[2] Não", "[3] Pular"
    }
}
