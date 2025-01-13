import random

def gerar_nome_mundo():
    """Gera um nome aleatório para o mundo."""
    prefixos = ["Zor", "Drak", "Eld", "Aeg", "Thal", "Lor"]
    sufixos = ["athia", "nor", "oria", "dora", "wyn", "ium"]
    return random.choice(prefixos) + random.choice(sufixos)

def gerar_cultura():
    """Gera uma descrição cultural para o mundo."""
    culturas = [
        "Um mundo de comércio e magia, habitado por seres pacíficos.",
        "Um planeta de guerreiros implacáveis que valorizam a força acima de tudo.",
        "Uma terra cheia de mistérios, lar de criaturas mágicas e desconhecidas.",
        "Uma civilização avançada tecnologicamente, mas socialmente instável.",
        "Uma sociedade baseada na harmonia com a natureza e seus espíritos.",
    ]
    return random.choice(culturas)

def gerar_clima():
    """Define o clima predominante do mundo."""
    climas = ["Temperado", "Árido", "Tropical", "Polar", "Montanhoso"]
    return random.choice(climas)

def gerar_populacao():
    """Gera um número aproximado para a população do mundo."""
    return random.randint(100000, 10000000)  # Entre 100 mil e 10 milhões

def criar_mundo():
    """Cria um mundo fictício com propriedades aleatórias."""
    mundo = {
        "nome": gerar_nome_mundo(),
        "cultura": gerar_cultura(),
        "clima": gerar_clima(),
        "populacao": gerar_populacao(),
    }
    return mundo
