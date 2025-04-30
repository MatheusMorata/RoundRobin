# SIMULAÇÃO
from escalonador import Escalonador
from tarefa import Tarefa

# Criando as tarefas
tarefa1 = Tarefa('Tarefa 1', 10)
tarefa2 = Tarefa('Tarefa 2', 4)
tarefa3 = Tarefa('Tarefa 1', 7)
tarefa4 = Tarefa('Tarefa 2', 8)

tarefas = [tarefa1, tarefa2, tarefa3, tarefa4]

# Criando o escalonador com quantum 4
escalonador = Escalonador(4, tarefas)

# Iniciando o algoritmo Round Robin
escalonador.roundRobin()
