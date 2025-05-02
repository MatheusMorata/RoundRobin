from time import sleep

class Tarefa:
    
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao

    def executar(self):
        # Escreve no log
        with open("log.txt", "a") as f:
            f.write(f"Entrou na fila de pronto: {self.nome} tempo necessario {self.duracao} segundos\n")
        sleep(self.duracao) # Simula duracao da tarefa