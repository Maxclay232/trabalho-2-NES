import pytest
from datetime import datetime, timedelta
from finances.investment import Investment
from finances.account import Account

def test_investment_initialization():

    """
    Testa a inicialização de um objeto Investment.

    Verifica se o investimento foi criado corretamente com os atributos especificados e se a data de compra é 
    uma instância de datetime.
    """

    inv = Investment("Poupança", 1000.0, 0.01)
    assert inv.type == "Poupança"
    assert inv.initial_amount == 1000.0
    assert inv.rate_of_return == 0.01
    assert isinstance(inv.date_purchased, datetime)

def test_calculate_value():

    """
    Testa o método calculate_value de Investment.

    Verifica se o método calculate_value retorna o valor atual correto do investimento após um ano.
    """

    inv = Investment("Poupança", 1000.0, 0.01)
    inv.date_purchased = datetime.now() - timedelta(days=30*12)  # 1 ano atrás
    assert inv.calculate_value() == pytest.approx(1000.0 * (1 + 0.01)**12)

def test_sell_investment():

    """
    Testa o método sell de Investment.

    Verifica se o método sell atualiza corretamente o saldo da conta após vender o investimento.
    """
    
    inv = Investment("Poupança", 1000.0, 0.01)
    inv.date_purchased = datetime.now() - timedelta(days=30*12)  # 1 ano atrás
    a = Account("Conta Corrente")
    inv.sell(a)
    assert a.balance == pytest.approx(1000.0 * (1 + 0.01)**12)
