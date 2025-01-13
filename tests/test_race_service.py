import pytest
from app.services.race_service import criar_raca

def test_criar_raca():
    """Testa a criação de uma raça com características geradas."""
    raca = criar_raca()
    
    assert "nome" in raca
    assert "habilidade" in raca
    assert "caracteristica" in raca
    assert isinstance(raca["nome"], str)
    assert isinstance(raca["habilidade"], str)
    assert isinstance(raca["caracteristica"], str)
