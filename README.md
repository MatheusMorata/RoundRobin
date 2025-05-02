# Round Robin - Simulador de Escalonamento de Processos

## Resumo
Este projeto simula o algoritmo de escalonamento Round Robin usando Python e POO. Cada processo executa por um quantum de tempo antes de ceder a vez ao próximo, garantindo justiça na alocação de recursos.

## Como Executar
```bash
cd RoundRobin
python main.py
```

## Para criar cenários

# 1. Crie tarefas
tarefa1 = Tarefa("Processo A", 5)
tarefa2 = Tarefa("Processo B", 3)

# 2. Adicione à lista
tarefas = [tarefa1, tarefa2]

# 3. Defina o quantum (unidades de tempo)
escalonador = Escalonador(2, tarefas)  # Quantum = 2
