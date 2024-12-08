from datetime import datetime

class Transaction:

    """
    Classe para representar uma transação financeira.

    Atributos:
        amount (float): Valor da transação.
        date (datetime): Data da transação.
        category (str): Identificador de uma categoria.
        description (str): Descrição da transação.
    """

    def __init__(self, amount: float, category: str, description: str = "") -> None:

        """
        Inicializa um objeto Transaction.

        Args:
            amount (float): Valor da transação.
            category (str): Identificador de uma categoria.
            description (str, optional): Descrição da transação. Default é "".
        """

        self.amount = amount
        self.date = datetime.now()
        self.category = category
        self.description = description

    def __str__(self) -> str:

        """
        Retorna uma descrição da transação.

        Returns:
            str: Descrição da transação no formato "Transação: {description} R$ {amount:.2f} ({category})".
        """

        return f"Transação: {self.description} R$ {self.amount:.2f} ({self.category})"

    def update(self, **attributes) -> None:

        """
        Atualiza um ou mais atributos da transação.

        Args:
            **attributes: Atributos para serem atualizados.
        """
        
        for key, value in attributes.items():
            setattr(self, key, value)
