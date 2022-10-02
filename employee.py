"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract, salary="", totalSalary=""):
        self.name = name
        self.contract = contract
        self.hours = ""
        self.contractT = contract
        self.salary = salary
        self.totalSalary = totalSalary

    def calculateSalary(self):
        tSalary = self.hours * self.salary
        self.totalSalary = tSalary
        #return (tSalary)

    def get_pay(self):
        if self.contract == 'hourly':
            self.calculateSalary()
            return self.totalSalary
        else:
            return self.totalSalary
        #return salary

    def __str__(self):
        if self.contract == 'hourly':
            return(f'{self.name} works on a contract of {self.hours} hours at {self.salary}/hour.  Their total pay is {self.totalSalary}.')
        else:
            return(f'{self.name} works on a {self.contract} salary of {self.salary}.  Their total pay is {self.totalSalary}.')

class CommissionEmployee(Employee):
        def __init__(self, name, contract, type, salary, extraPay, totalSalary):
            super().__init__(name, contract, salary, totalSalary)
            self.commissionType = type
            self.commissionPay = extraPay
            self.amountOfContracts = ""

        def calculateSalary(self, tSalary):


            if self.commissionType == 'Contract':
                self.totalSalary = tSalary + (self.amountOfContracts * self.commissionPay)

            else:
                self.totalSalary = tSalary + self.commissionPay

            #return (tSalary)
        def get_pay(self):
            if self.contract == 'hourly':
                tSalary = self.hours * self.salary
                self.calculateSalary(tSalary)
            else:
                tSalary = self.salary
                self.calculateSalary(tSalary)
            return self.totalSalary
                #return salary


        def __str__(self):
            if self.contract == 'hourly':
                if self.commissionType == 'Contract':
                    return(f'{self.name} works on a contract of {self.hours} hours at {self.salary}/hour and receives a commission for {self.amountOfContracts} contract(s) at {self.commissionPay}/contract.  Their total pay is {self.totalSalary}.')
                else:
                    return(f'{self.name} works on a contract of {self.hours} hours at {self.salary}/hour and receives a bonus commission of {self.commissionPay}.  Their total pay is {self.totalSalary}.')
            else:
                if self.commissionType == 'Contract':
                    return(f'{self.name} works on a {self.contract} salary of {self.salary} and receives a commission for {self.amountOfContracts} contract(s) at {self.commissionPay}/contract.  Their total pay is {self.totalSalary}.')
                else:
                    return(f'{self.name} works on a {self.contract} salary of {self.salary} and receives a bonus commission of {self.commissionPay}.  Their total pay is {self.totalSalary}.')

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 'monthly', 4000,4000)


# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 'hourly', 25, "")
charlie.hours = 100


# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = CommissionEmployee('Renee', 'monthly', 'Contract', 3000, 200, '')
renee.amountOfContracts = 4


# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = CommissionEmployee('Jan', 'hourly', 'Contract', 25, 220, '')
jan.hours = 150
jan.amountOfContracts = 3


# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = CommissionEmployee('Robbie', 'monthly', 'Bonus', 2000, 1500, '')



# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = CommissionEmployee('Ariel', 'hourly', 'Bonus', 30, 600, '')
ariel.hours = 120
