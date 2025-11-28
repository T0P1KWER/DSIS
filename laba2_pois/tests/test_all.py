# tests/test_all.py
import unittest
from unittest.mock import patch, Mock
import sys
import os

# Добавляем корень проекта в путь
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Импорты — все с учётом snake_case имён файлов и классов
from Human import Human
from Postal_Worker import Postal_Worker
from Post_office import Post_office
from Bilding import Bilding
from Company_info import Company_info
from Car import Car
from Bicycle import Bicycle
from Accountant import Accountant
from Director import Director
from Postman import Postman
from Watchman import Watchman
from Manager import Manager
from Working_place import Working_place  # ← snake_case
from Chair import Chair
from Storage_room import Storage_room
from Cash_register import Cash_register
from Money_check_machine import Money_check_machine

# Исключения
from CompanyNameEmptyError import CompanyNameEmptyError
from InvalidFoundationYearError import InvalidFoundationYearError
from InvalidEmployeesCountError import InvalidEmployeesCountError
from InvalidEmailError import InvalidEmailError
from InvalidTaxIdError import InvalidTaxIdError
from NegativeEmployeesError import NegativeEmployeesError
from CarNotOK import CarNotOK
from PostManError import PostmanError
from NegativeMileageError import NegativeMileageError
from TooBigMileageError import TooBigMileageError
from SoBigWeight import SoBigWeight
from TooManyShelvesError import TooManyShelvesError


class TestHuman(unittest.TestCase):

    def setUp(self):
        self.human = Human("Александр", "Иванов", "Сергеевич", 30, "мужской", 180, 75)

    def test_tell_about_yourself(self):
        with patch('builtins.print') as mock_print:
            self.human.tell_about_yourself()
            printed = '\n'.join(str(call) for call in mock_print.call_args_list)
            self.assertIn("Имя: Александр", printed)

    def test_die(self):
        with patch('builtins.print') as mock_print:
            self.human.die()
            self.assertFalse(self.human.is_alive())
            mock_print.assert_called_with("человек Александр Иванов помер")

    def test_is_alive(self):
        self.assertTrue(self.human.is_alive())
        self.human.die()
        self.assertFalse(self.human.is_alive())


class TestPostalWorker(unittest.TestCase):

    def setUp(self):
        self.worker = Postal_Worker(
            name="Мария", lastname="Петрова", surname="Андреевна",
            age=28, gender="женский", height=165, weight=55,
            worker_id="PW-123", ownskills=["Excel", "Касса"],
            education="Экономист", status="оператор", work_experience=3
        )

    def test_initialization(self):
        self.assertEqual(self.worker.worker_id, "PW-123")
        self.assertEqual(self.worker.age, 28)

    def test_promote(self):
        result = self.worker.promote("старший оператор", 5000)
        self.assertIn("Повышение!", result)
        self.assertIn("старший оператор", result)
        self.assertIn("Зарплата: 6000 руб.", result)

    def test_demote(self):
        self.worker.set_salary(15000)
        result = self.worker.demote("курьер", 10000)
        self.assertIn("Понижение!", result)
        self.assertIn("Зарплата: 5000 руб.", result)

    def test_demote_salary_not_below_1000(self):
        self.worker.set_salary(1500)
        result = self.worker.demote("уборщик", 2000)
        self.assertIn("Зарплата: 1000 руб.", result)

    def test_get_salary_info(self):
        result = self.worker.get_salary_info()
        self.assertIn("Текущая зарплата: 1000 руб.", result)

    def test_tell_about_yourself_like_a_work(self):
        info = self.worker.tell_about_yourself_like_a_work()
        self.assertIn("Мария", info)
        self.assertIn("оператор", info)
        self.assertIn("3 лет", info)


class TestBildingAndPostOffice(unittest.TestCase):

    def test_bilding_initialization(self):
        building = Bilding("ул. Пушкина, 10", "офис", 1990, 500, 5)
        self.assertEqual(building.address, "ул. Пушкина, 10")
        self.assertEqual(building.number_of_storeys, 5)

    def test_post_office_initialization(self):
        office = Post_office("ул. Ленина, 1", "почтовое", 1950, 200, 2, 10000000, "9:00-18:00")
        self.assertEqual(office.address, "ул. Ленина, 1")
        self.assertEqual(office.get_postmen_count(), 0)

    def test_post_office_add_remove_postman(self):
        office = Post_office("ул. Ленина, 1", "почтовое", 1950, 200, 2, 10000000, "9:00-18:00")
        postman = Mock()
        postman.lastname = "Сидоров"

        with patch('builtins.print') as mock_print:
            office.add_postman(postman)
            mock_print.assert_called_with("Почтальон Сидоров добавлен в офис")
            self.assertEqual(office.get_postmen_count(), 1)

            office.remove_postman(postman)
            mock_print.assert_called_with("Почтальон Сидоров удален из офиса")
            self.assertEqual(office.get_postmen_count(), 0)

    def test_post_office_rebuilding(self):
        office = Post_office("ул. Тестовая, 5", "почтовое", 2000, 300, 3, 2000000, "8:00-20:00")
        with patch('builtins.print') as mock_print:
            office.rebuilding()
            mock_print.assert_called_with("rebuilding")

    def test_post_office_sell_office(self):
        office = Post_office("ул. Тестовая, 5", "почтовое", 2000, 300, 3, 2000000, "8:00-20:00")
        with patch('builtins.print') as mock_print:
            office.sell_office()
            mock_print.assert_called_with("office was selled for 2000000")


class TestCompanyInfo(unittest.TestCase):

    def setUp(self):
        self.valid_data = {
            "company_name": "Почта России",
            "legal_form": "АО",
            "foundation_year": 1863,
            "owner_name": "Россия",
            "employees_count": 380000,
            "postal_services": ["Письма", "Посылки"],
            "phone_number": "+78002005888",
            "email": "info@russianpost.ru",
            "address": "г. Москва, Волоколамское ш., д. 13",
            "tax_id": "7704000399"
        }

    def test_valid_company_info(self):
        company = Company_info(**self.valid_data)
        result = company.validate_company_info()
        self.assertEqual(result, "Данные компании корректны")

    def test_empty_company_name(self):
        self.valid_data["company_name"] = ""
        company = Company_info(**self.valid_data)
        result = company.validate_company_info()
        self.assertIn("CompanyNameEmptyError", result)

    def test_invalid_foundation_year(self):
        for year in [1799, 2025]:
            with self.subTest(year=year):
                self.valid_data["foundation_year"] = year
                company = Company_info(**self.valid_data)
                result = company.validate_company_info()
                self.assertIn("InvalidFoundationYearError", result)

    def test_invalid_employees_count(self):
        for count in [0, -5]:
            with self.subTest(count=count):
                self.valid_data["employees_count"] = count
                company = Company_info(**self.valid_data)
                result = company.validate_company_info()
                self.assertIn("InvalidEmployeesCountError", result)

    def test_invalid_email(self):
        self.valid_data["email"] = "bad-email"
        company = Company_info(**self.valid_data)
        result = company.validate_company_info()
        self.assertIn("InvalidEmailError", result)

    def test_invalid_tax_id(self):
        for tax_id in ["123", "12345678901"]:
            with self.subTest(tax_id=tax_id):
                self.valid_data["tax_id"] = tax_id
                company = Company_info(**self.valid_data)
                result = company.validate_company_info()
                self.assertIn("InvalidTaxIdError", result)

    def test_update_employees_count_valid(self):
        company = Company_info(**self.valid_data)
        result = company.update_employees_count(400000)
        self.assertEqual(company.employees_count, 400000)
        self.assertIn("обновлено: 400000", result)

    def test_update_employees_count_negative(self):
        company = Company_info(**self.valid_data)
        result = company.update_employees_count(-10)
        self.assertIn("NegativeEmployeesError", result)
        self.assertEqual(company.employees_count, 380000)


class TestCarAndBicycle(unittest.TestCase):

    def setUp(self):
        self.car = Car(horsepower=150, weight=1200, tipe="легковой", brand="Lada", model="Granta", year=2023, price=800000)
        self.bike = Bicycle(horsepower=0, weight=15, tipe="велосипед", brand="Stels", model="Navigator", year=2022, price=20000)

    def test_car_assign_valid(self):
        postman = Mock()
        postman.lastname = "Иванов"
        result = self.car.assign_to_postman(postman)
        self.assertIn("назначен почтальону Иванов", result)

    def test_car_assign_no_postman(self):
        result = self.car.assign_to_postman(None)
        self.assertIn("PostmanError", result)

    def test_car_broken_assign(self):
        self.car.break_down()
        postman = Mock()
        postman.lastname = "Петров"
        result = self.car.assign_to_postman(postman)
        self.assertIn("CarNotOK", result)

    def test_car_add_mileage_valid(self):
        result = self.car.add_mileage(50)
        self.assertIn("Добавлено 50 км", result)
        self.assertEqual(self.car.get_mileage(), 50)

    def test_car_add_mileage_negative(self):
        result = self.car.add_mileage(-10)
        self.assertIn("NegativeMileageError", result)
        self.assertEqual(self.car.get_mileage(), 0)

    def test_car_add_mileage_too_big(self):
        result = self.car.add_mileage(1500)
        self.assertIn("TooBigMileageError", result)
        self.assertEqual(self.car.get_mileage(), 0)

    def test_bicycle_assign_valid(self):
        postman = Mock()
        postman.lastname = "Сидоров"
        result = self.bike.assign_to_postman(postman)
        self.assertIn("назначен почтальону Сидоров", result)

    def test_bicycle_add_mileage(self):
        self.bike.add_mileage(10)
        self.assertEqual(self.bike.get_mileage(), 10)


class TestAccountant(unittest.TestCase):

    def setUp(self):
        self.accountant = Accountant(
            name="Анна", lastname="Смирнова", surname="Игоревна",
            age=35, gender="женский", height=165, weight=60,
            worker_id="ACC-001", ownskills="1C, Excel", education="Высшее",
            status="ведущий бухгалтер", work_experience=10,
            accounting_software="1С:Бухгалтерия", clients_count=150
        )

    def test_process_payments(self):
        result = self.accountant.process_payments()
        self.assertIn("Обрабатывает платежи для 150 клиентов", result)

    def test_distribute_money_valid(self):
        result = self.accountant.distribute_money(100000, 10)
        self.assertIn("По 10000.00 руб.", result)

    def test_distribute_money_zero_people(self):
        result = self.accountant.distribute_money(50000, 0)
        self.assertEqual(result, "Некому распределять деньги!")


class TestDirector(unittest.TestCase):  # ← исправлено имя класса (было Test_director)

    def setUp(self):
        self.director = Director(
            name="Иван", lastname="Петров", surname="Сергеевич",
            age=50, gender="мужской", height=180, weight=85,
            worker_id="DIR-001", ownskills="управление", education="MBA",
            status="директор", work_experience=20,
            branch="Москва", count_worker=50
        )

    def test_set_budget_valid(self):
        with patch('builtins.print'):
            self.director.set_budget(1000000)
        self.assertEqual(self.director.get_budget(), 1000000)

    def test_set_negative_budget(self):
        with patch('builtins.print') as mock_print:
            self.director.set_budget(-1000)
            printed = '\n'.join(call[0][0] for call in mock_print.call_args_list)
            self.assertIn("бюджет не может быть отрицательным", printed)

    def test_make_decision(self):
        result = self.director.make_decision()
        self.assertIn("принимает стратегические решения", result)

    def test_approve_budget(self):
        self.director.set_budget(750000)
        result = self.director.approve_budget()
        self.assertIn("Утверждает бюджет в размере 750000 руб.", result)

    def test_get_workers_count(self):
        self.assertEqual(self.director.get_workers_count(), 50)

    def test_collaborate_with_accountant(self):
        accountant = Mock()
        accountant.name = "Анна"
        accountant.distribute_money.return_value = "Готово"
        self.director.set_budget(100000)
        with patch('builtins.print'):
            self.director.collaborate_with_accountant(accountant)
        accountant.distribute_money.assert_called_once_with(100000, 50)


class TestPostman(unittest.TestCase):

    def setUp(self):
        self.postman = Postman(
            name="Алексей", lastname="Кузнецов", surname="Дмитриевич",
            age=30, gender="мужской", height=175, weight=70,
            worker_id="PM-001", ownskills="навигация", education="Среднее",
            status="почтальон", work_experience=5,
            delivery_zone="Центр", transport_type="велосипед"
        )
        self.car = Car(100, 1000, "авто", "ВАЗ", "2107", 1990, 50000)
        self.office = Post_office("ул. Ленина, 1", "почтовое", 1950, 200, 2, 10000000, "9:00-18:00")

    def test_assign_vehicle(self):
        with patch('builtins.print'):
            self.postman.assign_vehicle(self.car)
        self.assertEqual(self.postman._Postman__assigned_vehicle, self.car)

    def test_make_delivery(self):
        with patch('builtins.print'):
            self.postman.assign_vehicle(self.car)
        result = self.postman.make_delivery(15)
        self.assertIn("проехал 15 км", result)
        self.assertEqual(self.car.get_mileage(), 15)

    def test_deliver_packages(self):
        self.postman.set_office(self.office)
        result = self.postman.deliver_packages()
        self.assertIn("из офиса ул. Ленина, 1", result)


class TestChairAndStorage(unittest.TestCase):

    @patch('builtins.input', return_value='70')
    def test_chair_normal_weight(self, mock_input):
        chair = Chair("Офисный")
        result = chair.sit_on_chair()
        self.assertEqual(result, "Сижу на  стуле")

    @patch('builtins.input', return_value='150')
    def test_chair_too_heavy(self, mock_input):
        chair = Chair("Офисный")
        result = chair.sit_on_chair()
        self.assertIn("SoBigWeight", result)

    @patch('builtins.input', return_value='10')
    def test_storage_add_shelf_valid(self, mock_input):
        storage = Storage_room(20, 18, 2, 150)
        result = storage.add_shelf()
        self.assertIn("Добавлено 10 полок", result)
        self.assertEqual(storage.shelves_count, 30)

    @patch('builtins.input', return_value='60')
    def test_storage_add_shelf_too_many(self, mock_input):
        storage = Storage_room(20, 18, 2, 150)
        result = storage.add_shelf()
        self.assertIn("TooManyShelvesError", result)


class TestWorkingPlace(unittest.TestCase):

    def test_working_place_initialization(self):
        wp = Working_place()  # ← snake_case, как в файле
        self.assertIsNotNone(wp.chair)
        self.assertIsNotNone(wp.cash_register)

    def test_cash_register(self):
        wp = Working_place()  # ← snake_case
        result = wp.cash_register.process_payment(500)
        self.assertIn("Оплата 500 руб.", result)

    def test_money_check_machine(self):
        wp = Working_place()
        result = wp.money_check_machine.check_bill(1000)
        self.assertIn("Купюра 1000 руб. проверена", result)


if __name__ == '__main__':
    unittest.main()