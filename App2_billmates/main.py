from classes.bill import Bill
from classes.flatmate import Flatmate
from classes.report import PdfReport

amount = float(input('Inserte el monto: '))
period = input('Inserte el periodo: ')

name1 = input('Cual es el nombre: ')
day1 = int(input(f'Cuantos dias estuviste {name1} en casa: '))

name2 = input('Cual es el nombre de tu companero: ')
day2 = int(input(f'Cuantos dias estuvo {name2} en casa: '))

bill = Bill(amount, period)
mate1 = Flatmate(name1, day1)
mate2 = Flatmate(name2, day2)

print(f'{name1} paga: {mate1.pays(bill, mate2)}')
print(f'{name2} paga: {mate2.pays(bill, mate1)}')

pdf_report = PdfReport(filename='Report1.pdf')
pdf_report.generate(mate1, mate2, bill)
print('Reporte generado revise')
# print(john.pays(bill=bill, flatmate2=marry))