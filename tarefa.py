class Tarefa:
    
    def __init__(self, nome, duracao):
        self.nome = nome
        self.duracao = duracao
        self.tempo_restante = duracao  

    def executar(self):
        print(f"Executando tarefa: {self.nome}")
