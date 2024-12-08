from typing import List
from .account import Account
from .investment import Investment

class Client:

    """
    Classe para representar um cliente do sistema financeiro.

    Atributos:
        name (str): Nome do cliente.
        accounts (List[Account]): Lista de contas do cliente.
        investments (List[Investment]): Lista de investimentos do cliente.
    """

    def __init__(self, name: str) -> None:

        """
        Inicializa um objeto Client.

        Args:
            name (str): Nome do cliente.
        """

        self.name = name
        self.accounts = []
        self.investments = []

    def add_account(self, account_name: str) -> Account:

        """
        Cria uma nova conta para o cliente.

        Args:
            account_name (str): Nome da nova conta.

        Returns:
            Account: A nova conta criada.
        """

        account = Account(account_name)
        self.accounts.append(account)
        return account

    def add_investment(self, investment: Investment) -> None:

        """
        Adiciona um novo investimento para o cliente.

        Args:
            investment (Investment): O investimento a ser adicionado.
        """

        self.investments.append(investment)

    def get_net_worth(self) -> float:

        """
        Calcula o patrimônio líquido do cliente, somando os saldos das contas e os valores atuais dos 
        investimentos.

        Returns:
            float: O patrimônio líquido do cliente.
        """

        total = sum(account.balance for account in self.accounts)
        total += sum(investment.calculate_value() for investment in self.investments)
        return total
