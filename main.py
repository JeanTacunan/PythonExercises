# main.py

from saldo_calculador import SaldoCalculador
from utils import solicitar_saldo

def main():
    """
    Función principal para ejecutar el programa.
    """
    saldo_inicial = solicitar_saldo()  # Solicita el saldo inicial al usuario
    calculador = SaldoCalculador(saldo_inicial)  # Crea una instancia de la clase SaldoCalculador
    calculador.calcular_nuevo_saldo()  # Calcula el nuevo saldo
    calculador.mostrar_saldo()  # Muestra el saldo final


if __name__ == "__main__":
    main()
