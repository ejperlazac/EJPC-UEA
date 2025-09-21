# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Programa principal
if __name__ == "__main__":
    # Caso 1: usando el descuento por defecto (10%)
    monto1 = 100
    descuento1 = calcular_descuento(monto1)
    print(f"Monto de la compra: ${monto1}")
    print(f"Descuento aplicado: ${descuento1}")
    print(f"Monto final a pagar: ${monto1 - descuento1}\n")

    # Caso 2: usando un porcentaje personalizado (20%)
    monto2 = 200
    descuento2 = calcular_descuento(monto2, 20)
    print(f"Monto de la compra: ${monto2}")
    print(f"Descuento aplicado: ${descuento2}")
    print(f"Monto final a pagar: ${monto2 - descuento2}")
