import pytest
from app.services.world_service import criar_mundo

def test_criar_mundo():
    """Testa a criação de um mundo fictício."""
    mundo = criar_mundo()
    
    assert "nome" in mundo
    assert "cultura" in mundo
    assert "clima" in mundo
    assert "populacao" in mundo
    assert isinstance(mundo["nome"], str)
    assert isinstance(mundo["cultura"], str)
    assert isinstance(mundo["clima"], str)
    assert isinstance(mundo["populacao"], str)
