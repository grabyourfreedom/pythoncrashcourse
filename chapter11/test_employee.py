import unittest
from employee import Employee


class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        first_name = "Lakshmi"
        last_name = "Narasimhan"
        salary = 85000
        self.employee = Employee(first_name, last_name, salary)

    def test_employee_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 90000)

    def test_employee_default_raise_custom_increment(self):
        self.employee.give_raise(15000)
        self.assertEqual(self.employee.annual_salary, 100000)


unittest.main()
