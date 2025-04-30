import os
import signal
from multiprocessing import Process
from time import sleep

class Escalonador:
    
    def __init__(self, quantum, tarefas):
        self.quantum = quantum
        self.tarefas = tarefas

    def roundRobin(self):
        processos = []
        for tarefa in self.tarefas:
            # Criar um processo para cada tarefa
            p = Process(target=tarefa.executar)
            p.start()
            processos.append(p)

        while any(p.is_alive() for p in processos):
            for p in processos:
                if p.is_alive():
                    os.kill(p.pid, signal.SIGSTOP)  # Pausa o processo
                    print(f"Executando processo PID {p.pid} por {self.quantum} segundos.")
                    sleep(self.quantum)
                    os.kill(p.pid, signal.SIGCONT)  # Continua o processo
