from escalonador import Escalonador
from tarefa import Tarefa

tarefa1 = Tarefa('teste', 12)
tarefa2 = Tarefa('teste1', 15)
Tarefas = [tarefa1, tarefa2]

e = Escalonador(12, Tarefas)
e.roundRobin()
