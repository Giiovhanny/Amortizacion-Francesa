
class Bank:
    def __init__ (self, name, anualRate,comision):
        self.name = name
        self.anualRate = anualRate
        self.monthlyRate = (anualRate/100)/12
        self.comision = comision

    def feeCalculator (self, capital,n):
        return round(capital*((self.monthlyRate*(1+self.monthlyRate)**n)/(((1+self.monthlyRate)**n)-1)),2)

    def fullPayment(self,capital,fixedFee,month,n):
        counter=0  
        interestTotal=0  
        residue = capital
        while(counter<n):
            counter+=1
            interest=residue*self.monthlyRate
            if(month>=counter):
                interestTotal+=interest
            amortization=fixedFee-interest
            residue-=amortization
        return round(capital+interestTotal+(capital*self.comision),2) 
















