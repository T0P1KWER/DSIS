from CompanyNameEmptyError import CompanyNameEmptyError
from InvalidFoundationYearError import InvalidFoundationYearError
from InvalidEmployeesCountError import InvalidEmployeesCountError
from InvalidEmailError import InvalidEmailError
from InvalidTaxIdError import InvalidTaxIdError
from NegativeEmployeesError import NegativeEmployeesError

class Company_info:
    def __init__(self, company_name, legal_form, foundation_year, owner_name, employees_count, postal_services,
                 phone_number, email, address, tax_id):
        self.company_name = company_name
        self.legal_form = legal_form
        self.foundation_year = foundation_year
        self.owner_name = owner_name
        self.employees_count = employees_count
        self.postal_services = postal_services
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.tax_id = tax_id

    def validate_company_info(self):
        try:
            if not self.company_name:
                raise CompanyNameEmptyError("Название компании не может быть пустым!")

            if self.foundation_year < 1800 or self.foundation_year > 2024:
                raise InvalidFoundationYearError("Некорректный год основания!")

            if self.employees_count < 1:
                raise InvalidEmployeesCountError("Количество сотрудников должно быть положительным!")

            if "@" not in self.email:
                raise InvalidEmailError("Некорректный email адрес!")

            if len(self.tax_id) != 10:
                raise InvalidTaxIdError("ИНН должен содержать 10 цифр!")

            return "Данные компании корректны"

        except CompanyNameEmptyError:
            return f"Ошибка валидации: {CompanyNameEmptyError}"
        except InvalidFoundationYearError:
            return f"Ошибка валидации: {InvalidFoundationYearError}"
        except InvalidEmployeesCountError:
            return f"Ошибка валидации: {InvalidEmployeesCountError}"
        except InvalidEmailError:
            return f"Ошибка валидации: {InvalidEmailError}"
        except InvalidTaxIdError:
            return f"Ошибка валидации: {InvalidTaxIdError}"

    def update_employees_count(self, new_count):
        try:
            if new_count < 0:
                raise NegativeEmployeesError("Количество сотрудников не может быть отрицательным!")
            self.employees_count = new_count
            return f"Количество сотрудников обновлено: {new_count}"

        except NegativeEmployeesError:
            return f"Ошибка обновления: {NegativeEmployeesError}"