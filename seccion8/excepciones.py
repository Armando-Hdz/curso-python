def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("\nNo se puede dividir entre 0")
        return "Operacion No Valida\n"

oper1 =  int(input("Ingrese el primer valor: "))
oper2 =  int(input("Ingrese el segundo valor: "))

operacion = input("\nIntroduce la operacion que desea realizar (suma, resta, multiplicacion, division): ")

if  operacion == "suma":
    print(suma(oper1,oper2))
elif operacion == "resta":
    print(resta(oper1,oper2))
elif operacion == "multiplicacion":
    print(multiplicacion(oper1,oper2))
elif operacion == "division":
    print(division(oper1,oper2))
else:
    print("Error: Algo anda mal")
print("\nEjecutando")