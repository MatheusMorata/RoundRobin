from time import sleep
class Tarefa:
    
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao

    def executar(self):
        print(f"Entrou na fila de pronto: {self.nome} tempo necessario {self.duracao} segundos")
        sleep(self.duracao)