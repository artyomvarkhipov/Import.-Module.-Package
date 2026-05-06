import time
from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees
from tqdm import tqdm

if __name__ == '__main__':
    print(f"Сегодня: {datetime.now().date()}")

    calculate_salary()
    get_employees()

    print("Загрузка данных:")
    for i in tqdm(range(100)):
        time.sleep(0.01)
