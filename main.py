from datetime import datetime

from application.salary import calculate_salary
from application.db.people import get_employees


def date():
    return datetime.today()


if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print(date())