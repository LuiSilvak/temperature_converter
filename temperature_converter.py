# Conversor de Temperaturas

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_para_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_para_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_para_celsius(kelvin):
    return kelvin - 273.15

def kelvin_para_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def conversor_de_temperaturas():
    print("=== Conversor de Temperaturas ===")
    print("Escolha a escala de entrada:")
    print("[1] Celsius")
    print("[2] Fahrenheit")
    print("[3] Kelvin")

    escala_entrada = int(input("Digite o número correspondente à escala de entrada: "))
    temperatura = float(input("Digite a temperatura: "))

    print("\nEscolha a escala de saída: ")
    print("[1] Celsius")
    print("[2] Fahrenheit")
    print("[3] Kelvin")

    escala_saida = int(input("Digite o número correspondente à escala de saída: "))


    if escala_entrada == 1:     # Celsius
        if escala_saida == 1:
            resultado = temperatura
        elif escala_saida == 2:
            resultado = celsius_para_fahrenheit(temperatura)
        elif escala_saida == 3:
            resultado = celsius_para_kelvin(temperatura)
    elif escala_entrada == 2:    # Fahrenheit
        if escala_saida == 1:
            resultado = fahrenheit_para_celsius(temperatura)
        elif escala_saida == 2:
            resultado = temperatura
        elif escala_saida == 3:
            resultado = fahrenheit_para_kelvin(temperatura)
    elif escala_entrada == 3:
        if escala_saida == 1:
            resultado = kelvin_para_celsius(temperatura)
        elif escala_saida == 2:
            resultado = kelvin_para_fahrenheit(temperatura)
        elif escala_saida == 3:
            resultado = temperatura
    else:
        print("Opção inválida.")
        return
    
    print(f"\nTemperatura convertida: {resultado:.2f}°")


if __name__ == "__main__":
    conversor_de_temperaturas()