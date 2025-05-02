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
        i = 0

        # Cria um processo para cada tarefa
        for tarefa in self.tarefas:
            p = Process(target=tarefa.executar)
            processos.append({
                'process': p,
                'nome': tarefa.nome,
                'tempo_restante': tarefa.duracao
            })
            p.start()
            sleep(0.1)  # Evitar problemas de inicialização
            os.kill(p.pid, signal.SIGSTOP)  # Pausa todos os processos inicialmente

        while True:
            # Verifica se todos os processos terminaram
            if all(p['tempo_restante'] <= 0 for p in processos):
                break

            # Pula processos que já terminaram
            while processos[i]['tempo_restante'] <= 0:
                i = (i + 1) % len(processos)

            processo_atual = processos[i]
            p = processo_atual['process']

            # Calcula o tempo de execução (quantum ou tempo restante)
            tempo_execucao = min(self.quantum, processo_atual['tempo_restante'])
            
            print(f"Executando: {processo_atual['nome']} por {tempo_execucao}s")
            
            # Continua o processo
            os.kill(p.pid, signal.SIGCONT)
            
            # Espera pelo tempo de execução
            sleep(tempo_execucao)
            
            # Pausa o processo
            os.kill(p.pid, signal.SIGSTOP)
            
            # Atualiza o tempo restante
            processo_atual['tempo_restante'] -= tempo_execucao
            
            # Move para o próximo processo
            i = (i + 1) % len(processos)

        # Encerra todos os processos
        for p in processos:
            p['process'].terminate()
