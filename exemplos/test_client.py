import pytest
from datetime import datetime, timedelta
from finances.client import Client
from finances.account import Account
from finances.investment import Investment

def test_client_initialization():

    """
    Testa a inicialização de um objeto Client.

    Verifica se o cliente foi criado corretamente com o nome especificado e se as listas de contas e 
    investimentos estão vazias.
    """

    c = Client("Max Silva")
    assert c.name == "Max Silva"
    assert len(c.accounts) == 0
    assert len(c.investments) == 0

def test_add_account():

    """
    Testa o método add_account de Client.

    Verifica se uma nova conta é adicionada corretamente à lista de contas do cliente.
    """

    c = Client("Max Silva")
    a = c.add_account("Conta Corrente")
    assert len(c.accounts) == 1
    assert c.accounts[0].name == "Conta Corrente"

def test_add_investment():

    """
    Testa o método add_investment de Client.

    Verifica se um novo investimento é adicionado corretamente à lista de investimentos do cliente.
    """

    c = Client("Max Silva")
    inv = Investment("Poupança", 1000.0, 0.01)
    c.add_investment(inv)
    assert len(c.investments) == 1
    assert c.investments[0] == inv

def test_get_net_worth():

    """
    Testa o método get_net_worth de Client.

    Verifica se o patrimônio líquido do cliente é calculado corretamente, somando os saldos das contas
    e os valores atuais dos investimentos.
    """
    
    c = Client("Max Silva")
    a = c.add_account("Conta Corrente")
    a.add_transaction(100.0, "Food", "Lunch")
    inv = Investment("Poupança", 1000.0, 0.01)
    inv.date_purchased = datetime.now() - timedelta(days=30*12)  # 1 ano atrás
    c.add_investment(inv)
    expected_net_worth = 100.0 + 1000.0 * (1 + 0.01)**12
    assert c.get_net_worth() == pytest.approx(expected_net_worth)
