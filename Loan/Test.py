import pytest

from customer import Customer
from CustomerCheck import LoanOriginationSystem

class TestValidInput:
    def test_check_valid_input_valid_cases(self):
        # Valid input
        customer = Customer(age=30, income=50, credit_score=700, employment='C')
        system = LoanOriginationSystem(customer)
        assert system.check_valid_input() == True

        customer = Customer(age=46, income=250.43, credit_score=850, employment='F')
        system = LoanOriginationSystem(customer)
        assert system.check_valid_input() == True

    def test_check_valid_input_invalid_types(self):
        # Invalid types (Chuỗi, List, v.v.)
        customer = Customer(age="30", income=50, credit_score=700, employment='C')
        system = LoanOriginationSystem(customer)
        assert system.check_valid_input() == "Invalid Input"

        customer = Customer(age=30, income=[50], credit_score=700, employment='C')
        system = LoanOriginationSystem(customer)
        assert system.check_valid_input() == "Invalid Input"

        customer = Customer(age=30, income=50, credit_score=700.5, employment='C') # Credit score phải là int
        system = LoanOriginationSystem(customer)
        assert system.check_valid_input() == "Invalid Input"

        customer = Customer(age=30, income=50, credit_score=700, employment=1) # Employment phải là str
        system = LoanOriginationSystem(customer)
        assert system.check_valid_input() == "Invalid Input"

    def test_check_valid_input_invalid_age_cases(self):
        # Invalid age
        customer = Customer(age=17, income=50, credit_score=700, employment='C')
        system = LoanOriginationSystem(customer)
        assert system.check_valid_input() == "Invalid Input"
        
        customer = Customer(age=17.5, income=50, credit_score=700, employment='C')
        system = LoanOriginationSystem(customer)
        assert system.check_valid_input() == "Invalid Input"

        customer = Customer(age=66, income=50, credit_score=700, employment='C')
        system = LoanOriginationSystem(customer)
        assert system.check_valid_input() == "Invalid Input"

        customer = Customer(age=65.5, income=50, credit_score=700, employment='C')
        system = LoanOriginationSystem(customer)
        assert system.check_valid_input() == "Invalid Input"

    def test_check_valid_input_invalid_income_cases(self):
        # Invalid income
        customer = Customer(age=30, income=4, credit_score=700, employment='C')
        system = LoanOriginationSystem(customer)
        assert system.check_valid_input() == "Invalid Input"

        customer = Customer(age=30, income=501, credit_score=700, employment='C')
        system = LoanOriginationSystem(customer)
        assert system.check_valid_input() == "Invalid Input"

        customer = Customer(age=30, income=4.94, credit_score=700, employment='C')
        system = LoanOriginationSystem(customer)
        assert system.check_valid_input() == "Invalid Input"

        customer = Customer(age=30, income=500.05, credit_score=700, employment='C')
        system = LoanOriginationSystem(customer)
        assert system.check_valid_input() == "Invalid Input"

    def test_check_valid_input_invalid_credit_score_cases(self):
        # Invalid credit score
        customer = Customer(age=30, income=250, credit_score=299, employment='C')
        system = LoanOriginationSystem(customer)
        assert system.check_valid_input() == "Invalid Input"

        customer = Customer(age=30, income=250, credit_score=851, employment='C')
        system = LoanOriginationSystem(customer)
        assert system.check_valid_input() == "Invalid Input"

    def test_check_valid_input_invalid_employment_cases(self):
        # Invalid employment status
        customer = Customer(age=30, income=50, credit_score=700, employment='X')
        system = LoanOriginationSystem(customer)
        assert system.check_valid_input() == "Invalid Input"

class TestEvaluateCreditworthiness:
    def test_evaluate_creditworthiness_high(self):
        customer = Customer(age=30, income=250, credit_score=300, employment='C')
        system = LoanOriginationSystem(customer)
        assert system.evaluate_creditworthiness() == "High"

        customer = Customer(age=30, income=250, credit_score=500, employment='F')
        system = LoanOriginationSystem(customer)
        assert system.evaluate_creditworthiness() == "High"

        customer = Customer(age=30, income=250, credit_score=356, employment='C')
        system = LoanOriginationSystem(customer)
        assert system.evaluate_creditworthiness() == "High"

    def test_evaluate_creditworthiness_medium(self):
        customer = Customer(age=30, income=250, credit_score=501, employment='F')
        system = LoanOriginationSystem(customer)
        assert system.evaluate_creditworthiness() == "Medium"

        customer = Customer(age=30, income=250, credit_score=700, employment='C')
        system = LoanOriginationSystem(customer)
        assert system.evaluate_creditworthiness() == "Medium"

        customer = Customer(age=30, income=250, credit_score=653, employment='F')
        system = LoanOriginationSystem(customer)
        assert system.evaluate_creditworthiness() == "Medium"

    def test_evaluate_creditworthiness_low(self):
        customer = Customer(age=30, income=250, credit_score=701, employment='F')
        system = LoanOriginationSystem(customer)
        assert system.evaluate_creditworthiness() == "Low"

        customer = Customer(age=30, income=250, credit_score=850, employment='F')
        system = LoanOriginationSystem(customer)
        assert system.evaluate_creditworthiness() == "Low"

        customer = Customer(age=30, income=250, credit_score=799, employment='C')
        system = LoanOriginationSystem(customer)
        assert system.evaluate_creditworthiness() == "Low"

class TestGenerateLoanOffer:
    def test_generate_loan_offer_reject(self):
        customer = Customer(age=30, income=250, credit_score=300, employment='C')
        system = LoanOriginationSystem(customer)
        assert system.generate_loan_offer() == "REJECT"

        customer = Customer(age=30, income=14.5, credit_score=700, employment='C')
        system = LoanOriginationSystem(customer)
        assert system.generate_loan_offer() == "REJECT"

        customer = Customer(age=30, income=14.5, credit_score=800, employment='F')
        system = LoanOriginationSystem(customer)
        assert system.generate_loan_offer() == "REJECT"

    def test_generate_loan_offer_manual_review(self):
        customer = Customer(age=30, income=15, credit_score=501, employment='F')
        system = LoanOriginationSystem(customer)
        assert system.generate_loan_offer() == "MANUAL REVIEW"
        
        customer = Customer(age=30, income=14.5, credit_score=800, employment='C')
        system = LoanOriginationSystem(customer)
        assert system.generate_loan_offer() == "MANUAL REVIEW"

        customer = Customer(age=30, income=15, credit_score=800, employment='F')
        system = LoanOriginationSystem(customer)
        assert system.generate_loan_offer() == "MANUAL REVIEW"

    def test_generate_loan_offer_approve(self):
        customer = Customer(age=30, income=15, credit_score=501, employment='C')
        system = LoanOriginationSystem(customer)
        assert system.generate_loan_offer() == "APPROVE"

        customer = Customer(age=30, income=15, credit_score=801, employment='C')
        system = LoanOriginationSystem(customer)
        assert system.generate_loan_offer() == "APPROVE"