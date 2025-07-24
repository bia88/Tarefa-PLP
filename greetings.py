print("hello word")
site_name = 'PLP'

site_name = 'i love coding'

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operador=input("Digite o operador (+, -, *, /):")
if operador == "+":
    resultado=numero1 + numero2
elif operador == "-":
    resultado=numero1 - numero2   
elif operador == "*":
    resultado=numero1 * numero2  
elif operador == "/":
    if numero2 != 0:
        resultado = numero1 / numero2
    else:
        resultado = "Erro: divisão por zero"
else:
    resultado = "Operador inválido"
        

if isinstance(resultado, float) or isinstance(resultado, int):  
    print(f"{numero1} {operador} {numero2} = {resultado}")
else:
    print(resultado)
