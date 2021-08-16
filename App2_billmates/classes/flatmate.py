class Flatmate:
    def __init__(self, name, days_in_house):
        self.name = name
        self.day_in_house = days_in_house
    
    def pays(self, bill, flatmate2):
        weight = self.day_in_house / (self.day_in_house + flatmate2.day_in_house)
        return round(bill.amount * weight,2)
