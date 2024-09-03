# utils.py

def solicitar_saldo() -> float:
    """
    Solicita el saldo inicial al usuario y lo devuelve como un número flotante.
    """
    while True:
        try:
            saldo_inicial = float(input("Dame saldo actual: "))
            return saldo_inicial
        except ValueError:
            print("Por favor, ingrese un número válido.")
