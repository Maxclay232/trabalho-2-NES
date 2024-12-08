from datetime import datetime, timedelta
from .account import Account

class Investment:

    """
    Classe para representar um investimento financeiro.

    Atributos:
        type (str): Identificador de um tipo de investimento.
        initial_amount (float): Valor inicial do investimento.
        date_purchased (datetime): Data da compra do investimento.
        rate_of_return (float): Taxa mensal de retorno.
    """

    def __init__(self, type: str, initial_amount: float, rate_of_return: float):

        """
        Inicializa um objeto Investment.

        Args:
            type (str): Identificador de um tipo de investimento.
            initial_amount (float): Valor inicial do investimento.
            rate_of_return (float): Taxa mensal de retorno.
        """

        self.type = type
        self.initial_amount = initial_amount
        self.date_purchased = datetime.now()
        self.rate_of_return = rate_of_return

    def calculate_value(self):

        """
        Calcula o valor atual do investimento com base na taxa de retorno e no tempo decorrido.

        Returns:
            float: Valor atual do investimento.
        """

        months = (datetime.now() - self.date_purchased).days // 30
        return self.initial_amount * ((1 + self.rate_of_return) ** months)

    def sell(self, account: Account):

        """
        Vende o investimento e deposita o valor em uma conta.

        Args:
            account (Account): Conta onde o valor do investimento será depositado.
        """
        
        account.balance += self.calculate_value()
