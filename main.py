import calculator
#Creamos una instancia para cada banco
BankA = calculator.Bank('Banco A', 12, 0.05)
BankB = calculator.Bank('Banco B', 16, 0.02)
BankC = calculator.Bank('Banco C', 20, 0.00)

#Numero de cuotas 
n=12

#Se le pide al usuario la cantidad que desea y si desea precancelar.
capital = input("Ingrese la cantidad del credito que desea realizar: $ ")
capital = float(capital)
answer = input("Desea precancelar Si (S) / No (N) : ")
month=99                
if (answer.upper()=='S'):
    month = input("Ingrese el numero del mes en el que desea precancelar (1 - 11): ")
    month = int(month)

#Se imprime los resultados obtenidos
print(f"The full payment in {BankA.name} is: ${BankA.fullPayment(capital,BankA.feeCalculator(capital,n),month,n)}")
print(f"The full payment in {BankB.name} is: ${BankB.fullPayment(capital,BankB.feeCalculator(capital,n),month,n)}")
print(f"The full payment in {BankC.name} is: ${BankC.fullPayment(capital,BankC.feeCalculator(capital,n),month,n)}")


