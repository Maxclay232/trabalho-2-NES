import pytest
from datetime import datetime
from finances.account import Account

def test_account_initialization():

    """
    Testa a inicialização de um objeto Account.

    Verifica se a conta foi criada corretamente com o nome especificado. o saldo inicial é 0.0 e a lista de 
    transações está vazia.
    """

    a = Account("Conta Corrente")
    assert a.name == "Conta Corrente"
    assert a.balance == 0.0
    assert len(a.transactions) == 0

def test_add_transaction():

    """
    Testa o método add_transaction de Account.

    Verifica se uma nova transação é adicionada corretamente à lista de transações, e se o saldo da conta é 
    atualizado corretamente.
    """

    a = Account("Conta Corrente")
    t = a.add_transaction(100.0, "Food", "Lunch")
    assert a.balance == 100.0
    assert len(a.transactions) == 1
    assert a.transactions[0] == t

def test_get_transactions():

    """
    Testa o método get_transactions de Account.

    Verifica se o método get_transactions retorna corretamente a lista de transações filtradas por categoria.
    """
    
    a = Account("Conta Corrente")
    a.add_transaction(100.0, "Food", "Lunch")
    a.add_transaction(200.0, "Transport", "Bus fare")
    transactions = a.get_transactions(category="Food")
    assert len(transactions) == 1
    assert transactions[0].category == "Food"
