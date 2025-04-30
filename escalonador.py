from multiprocessing import Process
from time import sleep

class Escalonador:

    def __init__(self,quantum, tarefas):
        self.quantum = quantum
        self.tarefas = tarefas
        
        
    def roundRobin():
        for i in range(0, len(self.tarefas)):
            print(self.tarefas[i].nome)
            print(self.tarefas[i].duracao)
            print("\n")
            
