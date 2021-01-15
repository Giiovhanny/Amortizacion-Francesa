Best Loan

El programa genera la cantidad total a pagar (Capital + Interes + Comision) por un prestamo en diferentes bancos. El usuario tambien tiene la opcion de pre-cancelar la deuda. En este caso el programa quita el interes que se pudo generar de no haber pre-cancelado la deuda.

El programa cuenta con 3 archivos:

main.py : Aqui el programa pide al usuario la cantidad que desea solicitar de prestamo (capital), asi tambien como si desea precancelar y en que mes le gustaria precancelar. Ademas, se inicializan las 3 instancias de la clase bank con los nombres, intereses y comisiones de cada institucion.

calculator.py : Este archivo cuenta con la clase Bank. La clase Bank tiene 3 metodos:
    init: para inicializar su nombre, tasas de interes y comision. 
    feeCalculator: Calcula la cuota mensual fija (amortizacion francesa)
    fullPayment: Calcula el total a pagar en cada institucion. 

test_main.py : Contiene 4 test unitarios donde verifica que bajo ciertos parametros (los del ejercicio) se obtienen los valores esperados.

To run the program:

python3 main.py

to run the tests:

pytest -v
