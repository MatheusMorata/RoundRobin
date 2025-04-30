import os
import singal
from multiprocessing import Process
from time import sleep


class Escalonador:

    def __init__(self,quantum, tarefas):
        self.quantum = quantum
        self.tarefas = tarefas
        
    def roundRobin():
        
