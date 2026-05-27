class Customer:
    def __init__(self, age, income, credit_score, employment):
        self.age = age
        self.income = round(income, 1)
        self.credit_score = credit_score
        self.employment = employment