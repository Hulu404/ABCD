class Patient:
    def __init__(self, name, surname, date):
        self.name = name
        self.surname = surname
        self.date = date

class Doctor:
    def __init__(self, fio, specialists):
        self.fio = fio
        self.specialists = specialists

person1 = Patient("Ivan", "Ivanovich", "1991")
person2 = Patient("Vasy", "Vasychkin", "1997")

doc1 = Doctor("Bnayat Ali Aymanovich", "psychologist")

