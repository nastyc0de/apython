

bill = Bill(amount=120, period='21/3/21')
john = Flatmate(name='John', days_in_house=20)
marry = Flatmate(name='Marry', days_in_house=25)

pdf_report = PdfReport(filename='Report1.pdf')
pdf_report.generate(flatmate1=john, flatmate2=marry, bill=bill)
# print(john.pays(bill=bill, flatmate2=marry))