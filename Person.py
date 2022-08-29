import random 
import datetime as dt
from dateutil.relativedelta import relativedelta

class PersonNummer: # ALLTID AV FORMEN "YYYYMMDD-####"

    def gen_date():
        infimum = dt.date(1999,1,1) # Förutsätter att ingen född innan år 1900 röstar. 
        supremum = dt.date.today() - relativedelta(years = 18)
        rand_date = infimum + dt.timedelta(days = random.randrange((supremum+dt.timedelta(days = 1 ) - infimum).days))
        return rand_date

    def is_valid_date(date): 
        return True if date <= dt.date.today() - relativedelta(years = 18) else False

    def no_hyphen(PN): 
        return PN[2:8]+ PN[9::]

    def get_kontroll_siffra(PN):
        pn = PersonNummer.no_hyphen(PN)[:-1] if len(PN) == 13 else PersonNummer.no_hyphen(PN)
        y = []; z = 0
        for i in range(len(pn)):
            y.append(2) if i % 2 == 0 else y.append(1)
            z += int(pn[i])*y[i]  if int(pn[i])*y[i]  <= 9 else int(pn[i])*y[i]  - 9 
        return int(str(z)[-1])

    def is_valid(PN):
        if not PersonNummer.is_valid_date(dt.date(int(PN[0:4]), int(PN[4:6]), int(PN[6:8]))): 
            return False
        ks = PersonNummer.get_kontroll_siffra(PN)
        return True if ks == int(PN[-1]) else False
    
    def gen_num():
        pn = []
        for num in str(PersonNummer.gen_date()):
            if num != '-':
                pn.append(num)

        pn.append('-')

        for i in range(3):
            pn.append(str(random.randint(0,9)))
        pn.append(str(PersonNummer.get_kontroll_siffra(''.join(pn))))
        return ''.join(pn)
        

class Person(PersonNummer):
    def __init__(self, pnum = None, val = None, random = False):
        self.pnum = PersonNummer.gen_num() if pnum is None and random else pnum
        if self.pnum is None:
            return 
        self.real = True if PersonNummer.is_valid(self.pnum) else False
        self.val = val if self.real else 'VALFUSK'
        
    def __str__(self):
        return f"PERSONNUMMER: {self.pnum} ||| VAL:{self.val}"


    
    
        



    
