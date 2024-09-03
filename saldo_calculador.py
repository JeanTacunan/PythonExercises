# saldo_calculador.py

class SaldoCalculador:
    """
    Clase para calcular el saldo con una tasa de interés dependiendo del saldo actual.
    """

    def __init__(self, saldo_inicial: float):
        self.saldo = saldo_inicial

    def calcular_nuevo_saldo(self):
        """
        Calcula el nuevo saldo en función de las condiciones de interés.
        """
        if self.saldo < 10000.00:
            self.saldo *= (1 + 0.03)  # Aplica un interés del 3%
        else:
            self.saldo *= (1 + 0.04)  # Aplica un interés del 4%

    def mostrar_saldo(self):
        """
        Muestra el saldo formateado a dos decimales.
        """
        print("Saldo final es %.2f" % self.saldo)
