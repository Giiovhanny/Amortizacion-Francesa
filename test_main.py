from calculator import Bank

#Verifica que la tasa mensual se este calculando correctamente
def test_calculator():
    BankX=Bank('Banco X',12,0.05)
    assert BankX.monthlyRate == 0.01

#Verifica que la cuota fija se este calculando correctamente

def test2_calculator():
    BankY=Bank('BancoY', 16,0.02)
    BankY.anualRate = 16.0
    capital = 1000
    n = 12
    assert BankY.feeCalculator(capital, n) == 90.73

#Verifica que el total a pagar (sin pre cancelacion ) se este calculando correctamente
def test3_calculator():
    BankZ=Bank('Banco Z', 16 , 0.02)
    capital = 1000
    n = 12
    fixedFee = 90.73
    month = 99
    assert BankZ.fullPayment(capital,fixedFee, month, n ) == 1108.77

#Verifica que el total a pagar (con pre cancelacion ) se este calculando correctamente
def test4_calculator():
    BankW=Bank('Banco W', 16,0.02)
    capital = 1000
    n = 12
    fixedFee = BankW.feeCalculator(capital,n)
    month = 10
    assert BankW.fullPayment(capital,fixedFee, month, n ) == 1105.21



   