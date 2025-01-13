import random

def gerar_nome_raca():
    """Gera um nome aleatório para a raça."""
    prefixos = ["Elf", "Orc", "Dwar", "Hum", "Drag", "Fae"]
    sufixos = ["lings", "rons", "ites", "ans", "born", "folk"]
    return random.choice(prefixos) + random.choice(sufixos)

def gerar_habilidade_especial():
    """Gera uma habilidade especial para a raça."""
    habilidades = [
        "Invisibilidade em florestas densas.",
        "Resistência ao fogo.",
        "Capacidade de respirar debaixo d'água.",
        "Velocidade sobre-humana.",
        "Habilidade para manipular magia negra.",
        "Comunicação com animais.",
    ]
    return random.choice(habilidades)

def gerar_caracteristica():
    """Gera uma característica física ou cultural para a raça."""
    caracteristicas = [
        "Altos, com olhos brilhantes e cabelos prateados.",
        "Pequenos, mas extremamente fortes fisicamente.",
        "Pele escamosa e um olhar intimidador.",
        "Orelhas pontudas e uma afinidade com a música.",
        "Grandes asas que brilham sob a luz do sol.",
        "Cultura tribal baseada na força coletiva.",
    ]
    return random.choice(caracteristicas)

def criar_raca():
    """Cria uma raça fictícia com propriedades aleatórias."""
    raca = {
        "nome": gerar_nome_raca(),
        "habilidade": gerar_habilidade_especial(),
        "caracteristica": gerar_caracteristica(),
    }
    return raca
