from datetime import datetime
import pytest
from finances.transaction import Transaction

def test_transaction_initialization():

    """
    Testa a inicialização de um objeto Transaction.

    Verifica se a transação foi criada corretamente com os atributos especificados e se a data é uma instância 
    de datetime.
    """

    t = Transaction(100.0, "Food", "Lunch")
    assert t.amount == 100.0
    assert t.category == "Food"
    assert t.description == "Lunch"
    assert isinstance(t.date, datetime)

def test_transaction_str():

    """
    Testa o método __str__ de Transaction.

    Verifica se a string retornada pelo método __str__ está no formato correto.
    """

    t = Transaction(100.0, "Food", "Lunch")
    assert str(t) == "Transação: Lunch R$ 100.00 (Food)"

def test_transaction_update():

    """
    Testa o método update de Transaction.

    Verifica se o método update atualiza corretamente os atributos da transação.
    """
    
    t = Transaction(100.0, "Food", "Lunch")
    t.update(amount=150.0, description="Dinner")
    assert t.amount == 150.0
    assert t.description == "Dinner"
