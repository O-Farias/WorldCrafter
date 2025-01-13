import pytest
from app.services.city_service import criar_cidade

def test_criar_cidade():
    """Testa a criação de uma cidade com geração automática."""
    cidade = criar_cidade()
    
    assert "nome" in cidade
    assert "populacao" in cidade
    assert "descricao" in cidade
    assert isinstance(cidade["nome"], str)
    assert isinstance(cidade["populacao"], str)  
    assert isinstance(cidade["descricao"], str)
