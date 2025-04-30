class Tarefa:
    
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao
        self.tempo_restante = duracao  

    def executar(self):
        print(f"Executando tarefa: {self.nome}")
        while self.tempo_restante > 0:
            print(f"{self.nome}: {self.tempo_restante} unidades de tempo restantes.")
            self.tempo_restante -= 1
