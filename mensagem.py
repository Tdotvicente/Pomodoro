# Mensagem usada para informar o estado atual do pomodoro e exibida ao usuário
estados_ui = {
    "Foco": "Hora de focar",
    "Pausa": "Hora de pausar",
    "Descanso": "Hora de descansar"
}

# Mensagens exibidas, em caixa de dialogos, entre troca de momentos.
# Elas têm a função de ser exibida entre etapas
# A interação será feita para iniciar finalizar ou pular um ciclo
dialogo_mensagem = {
    "ação": {
        "titulo": "Pomodoro",
        "Pausar": "O tempo acabou.\nfazer pequeno descanso?",
        "Focar": "O descanso Acabou.\nDeseja começar a focar?",
        "Descansar": "O ciclo acabou.\nVamos descansar",
        "Novo_ciclo": "Deseja começar\num novo ciclo",
        "opções": ["1.Sim", "2.Não", "3.Pular"]
    }
}
