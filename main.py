# SIMULAÇÃO
from escalonador import Escalonador
from tarefa import Tarefa

# Criando as tarefas
tarefa1 = Tarefa('Google Chrome', 10)
tarefa2 = Tarefa('Pacote Office', 4)
tarefa3 = Tarefa('Steam', 7)
tarefa4 = Tarefa('Skype', 8)

tarefas = [tarefa1, tarefa2, tarefa3, tarefa4]

# Criando o escalonador com quantum 4
escalonador = Escalonador(4, tarefas)


# Iniciando o algoritmo Round Robin
escalonador.roundRobin()
