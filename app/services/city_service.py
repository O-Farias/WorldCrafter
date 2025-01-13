import random

def gerar_nome_cidade():
    """Gera um nome aleatório para a cidade."""
    prefixos = ["New", "Port", "San", "Fort", "Lake", "River"]
    sufixos = ["ville", "ton", "burg", "ford", "wood", "field"]
    return random.choice(prefixos) + random.choice(sufixos)

def gerar_populacao_cidade():
    """Gera uma população aleatória para a cidade."""
    return random.randint(5000, 1000000)  # Entre 5 mil e 1 milhão de habitantes

def gerar_descricao_cidade():
    """Gera uma descrição aleatória para a cidade."""
    descricoes = [
        "Uma cidade vibrante cheia de comerciantes e exploradores.",
        "Um refúgio pacífico rodeado por montanhas majestosas.",
        "Uma metrópole movimentada com uma rica vida noturna.",
        "Uma cidade costeira famosa por suas praias paradisíacas.",
        "Um local histórico conhecido por suas ruínas antigas.",
    ]
    return random.choice(descricoes)

def criar_cidade():
    """Cria uma cidade fictícia com propriedades aleatórias."""
    cidade = {
        "nome": gerar_nome_cidade(),
        "populacao": f"{gerar_populacao_cidade():,}".replace(",", "."),
        "descricao": gerar_descricao_cidade(),
    }
    return cidade
