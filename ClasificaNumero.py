##Desarrolla un programa que permita ingresar un número y mediante un menú interactivo
##realizar las siguientes verificaciones:
#✓ Determinar si el número es par o impar
#✓ Determinar si es positivo, negativo o cero
#✓ Verificar si es múltiplo de 5
#✓ Verificar si es divisible entre 3 y 4 al mismo tiempo


def clasifica_numero():
    while True:
        try:
            opcion = input("Seleccione una opción:\n1. Numero par o impar\n2.  Numero positivo negativo o cero \n3. Multiplo de 5 \n4. Divisible entre 3 y 4 \n5. Salir\n")
            if opcion == '5':
                print("Saliendo del programa.")
                break
            numero = float(input("Ingrese un número: "))
            
            if opcion == '1':
                clasifica_par_impar(numero) 
            elif opcion == '2':
                clasifica_positivo_negativo_cero(numero)
            elif opcion == '3':
                verifica_multiplo_de_5(numero)
            elif opcion == '4':
                verifica_divisible_entre_3_y_4(numero)
            else:
                print("Opción no válida. Por favor, seleccione una opción del menú.")
        
        except ValueError:
            print("Por favor, ingrese un número válido.")
        
def clasifica_par_impar(numero):
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")
        
def clasifica_positivo_negativo_cero(numero):
    if numero > 0:
        print(f"El número {numero} es positivo.")
    elif numero < 0:
        print(f"El número {numero} es negativo.")
    else:
        print("El número es cero.")

def verifica_multiplo_de_5(numero):
    if numero % 5 == 0:
        print(f"El número {numero} es múltiplo de 5.")
    else:
        print(f"El número {numero} no es múltiplo de 5.")
        
def verifica_divisible_entre_3_y_4(numero):
    if numero % 3 == 0 and numero % 4 == 0:
        print(f"El número {numero} es divisible entre 3 y 4 al mismo tiempo.")
    else:
        print(f"El número {numero} no es divisible entre 3 y 4 al mismo tiempo.")
        
clasifica_numero()
