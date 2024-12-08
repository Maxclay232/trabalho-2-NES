from datetime import datetime
from typing import List
from .transaction import Transaction

class Account:

    """
    Classe para representar uma conta bancária ou financeira.

    Atributos:
        name (str): Nome da conta.
        balance (float): Saldo da conta.
        transactions (List[Transaction]): Lista de transações na conta, ordenadas por data.
    """

    def __init__(self, name: str) -> None:

        """
        Inicializa um objeto Account.

        Args:
            name (str): Nome da conta.
        """

        self.name = name
        self.balance = 0.0
        self.transactions = []

    def add_transaction(self, amount: float, category: str, description: str = "") -> Transaction:

        """
        Cria uma nova transação na conta e atualiza o saldo da conta.

        Args:
            amount (float): Valor da transação.
            category (str): Identificador de uma categoria.
            description (str, optional): Descrição da transação. Default é "".

        Returns:
            Transaction: A nova transação criada.
        """

        transaction = Transaction(amount, category, description)
        self.transactions.append(transaction)
        self.balance += amount
        return transaction

    def get_transactions(self, start_date: datetime = None, end_date: datetime = None, category: str = None) -> List[Transaction]:

        """
        Gera uma lista de transações, filtradas por data e/ou categoria.

        Args:
            start_date (datetime, optional): Data inicial para o filtro. Default é None.
            end_date (datetime, optional): Data final para o filtro. Default é None.
            category (str, optional): Categoria para o filtro. Default é None.

        Returns:
            List[Transaction]: Lista de transações que atendem aos critérios de filtro.
        """
        
        transactions = self.transactions
        if start_date:
            transactions = [t for t in transactions if t.date >= start_date]
        if end_date:
            transactions = [t for t in transactions if t.date <= end_date]
        if category:
            transactions = [t for t in transactions if t.category == category]
        return transactions
