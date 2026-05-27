from customer import Customer

class LoanOriginationSystem:
    def __init__(self, customer):
        self.customer = customer
        self.creditworthy = None
        self.loan_offer = None

    def check_valid_input(self):
        """Checks if the customer's input is valid."""
        if not isinstance(self.customer.age, int) or self.customer.age < 18 or self.customer.age > 65:
            return "Invalid Input"
        
        if not isinstance(self.customer.income, (int, float)) or self.customer.income < 5 or self.customer.income > 500:
            return "Invalid Input"
        
        if not isinstance(self.customer.credit_score, int) or self.customer.credit_score < 300 or self.customer.credit_score > 850:
            return "Invalid Input"
        
        if not isinstance(self.customer.employment, str) or self.customer.employment not in ['C', 'F']:
            return "Invalid Input"
        
        return True
    
    def evaluate_creditworthiness(self):
        """Evaluates the customer's creditworthiness based on their input."""
        if self.customer.credit_score <= 500:
            self.creditworthy = "High"
        elif self.customer.credit_score <= 700:
            self.creditworthy = "Medium"
        else:
            self.creditworthy = "Low"

        return self.creditworthy
    
    def generate_loan_offer(self):
        """Generates a loan offer based on the customer's info and creditworthiness."""
        # Gọi check_valid_input trước, nếu không hợp lệ thì trả về lỗi luôn
        is_valid = self.check_valid_input()
        if is_valid == "Invalid Input":
            return "Invalid Input"

        evaluated_creditworthiness = self.evaluate_creditworthiness()
        
        if evaluated_creditworthiness == "High":
            self.loan_offer = "REJECT"
            
        elif evaluated_creditworthiness == "Medium":
            if self.customer.income < 15:
                self.loan_offer = "REJECT"
            else:
                if self.customer.employment == 'C':
                    self.loan_offer = "APPROVE"
                elif self.customer.employment == 'F':
                    self.loan_offer = "MANUAL REVIEW"
                    
        else: # Low Risk
            if self.customer.income < 15:
                if self.customer.employment == 'C':
                    self.loan_offer = "MANUAL REVIEW"
                elif self.customer.employment == 'F':
                    self.loan_offer = "REJECT"
            else:
                if self.customer.employment == 'C':
                    self.loan_offer = "APPROVE"
                elif self.customer.employment == 'F':
                    self.loan_offer = "MANUAL REVIEW"
        
        return self.loan_offer