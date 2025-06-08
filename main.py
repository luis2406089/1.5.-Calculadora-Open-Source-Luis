from sumar import sumar
from resta import restar
from multiplicacion import multiplicar
from dividir import dividir
from suma_avanzada import suma_avanzada

def mostrar_menu():
    print("\n" + "="*40)
    print("         CALCULADORA PYTHON")
    print("="*40)
    print("1. Sumar dos números")
    print("2. Restar dos números")
    print("3. Multiplicar dos números")
    print("4. Dividir dos números")
    print("5. Suma avanzada (N números)")
    print("6. Salir")
    print("="*40)

def obtener_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor, ingresa un número válido.")

def obtener_numeros_avanzados():
    numeros = []
    print("Ingresa los números (presiona Enter sin escribir nada para terminar):")
    
    while True:
        entrada = input(f"Número {len(numeros) + 1}: ")
        if entrada == "":
            break
        try:
            numeros.append(float(entrada))
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    return numeros

def main():
    print("¡Bienvenido a la Calculadora Python!")
    print("Esta calculadora te permite realizar operaciones básicas y avanzadas.")    
    while True:
        mostrar_menu()
        
        try:
            opcion = int(input("Selecciona una opción (1-6): "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
        
        if opcion == 1:
            print("\n--- SUMA ---")
            a = obtener_numero("Ingresa el primer número: ")
            b = obtener_numero("Ingresa el segundo número: ")
            resultado = sumar(a, b)
            print(f"Resultado: {a} + {b} = {resultado}")
            
        elif opcion == 2:
            print("\n--- RESTA ---")
            a = obtener_numero("Ingresa el primer número: ")
            b = obtener_numero("Ingresa el segundo número: ")
            resultado = restar(a, b)
            print(f"Resultado: {a} - {b} = {resultado}")
            
        elif opcion == 3:
            print("\n--- MULTIPLICACIÓN ---")
            a = obtener_numero("Ingresa el primer número: ")
            b = obtener_numero("Ingresa el segundo número: ")
            resultado = multiplicar(a, b)
            print(f"Resultado: {a} × {b} = {resultado}")
            
        elif opcion == 4:
            print("\n--- DIVISIÓN ---")
            a = obtener_numero("Ingresa el dividendo: ")
            b = obtener_numero("Ingresa el divisor: ")
            resultado = dividir(a, b)
            if resultado is not None:
                print(f"Resultado: {a} ÷ {b} = {resultado}")
            
        elif opcion == 5:
            print("\n--- SUMA AVANZADA ---")
            numeros = obtener_numeros_avanzados()
            if len(numeros) > 0:
                resultado = suma_avanzada(numeros)
                numeros_str = " + ".join(map(str, numeros))
                print(f"Resultado: {numeros_str} = {resultado}")
            else:
                print("No se ingresaron números para sumar.")
                
        elif opcion == 6:
            print("\n¡Gracias por usar la Calculadora Python!")
            print("¡Hasta luego!")
            break
            
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 6.")
        
        # Pausa para que el usuario pueda ver el resultado
        input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main()