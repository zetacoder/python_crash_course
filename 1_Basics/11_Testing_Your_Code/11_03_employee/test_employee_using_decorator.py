import pytest
from employee import Employee

@pytest.fixture
def declare_employee():

    declare_employee = Employee("FName", "LName", 30000)

    return declare_employee



def test_give_default_raise(declare_employee):

    declare_employee.give_raise()

    assert declare_employee.annual_salary == 35000


def test_give_custom_raise(declare_employee):

    declare_employee.give_raise(25000)

    assert declare_employee.annual_salary == 55000

