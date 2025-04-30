from multiprocessing import Process
from time import sleep
from queue import Queue

class Escalonador:

    def __init__(self,quantum, tarefas):
        self.quantum = quantum
        self.fila = Queue()
        for tarefa in self.tarefas:
            self.fila.put(tarefa)
        
    def roundRobin():
        while not self.fila.empty():
            tarefa = self.fila.get()
            if tarefa.executar(self.quantum):
                self.fila.put(tarefa)
