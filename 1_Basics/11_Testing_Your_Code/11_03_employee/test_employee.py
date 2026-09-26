from employee import Employee

def test_give_default_raise():

    emp = Employee("FName", "LName", 30000)

    emp.give_raise()

    assert emp.annual_salary == 35000


def test_give_custom_raise():
    emp = Employee("FName", "LName", 30000)

    emp.give_raise(25000)

    assert emp.annual_salary == 55000

