from datetime import *
import time
from application.salary import *
from application.db.people import *
from tqdm import *

if __name__ == '__main__':
    print(f"Сегодня (dirty): {datetime.now().date()}")

    calculate_salary()
    get_employees()

    print("Загрузка данных:")
    for i in tqdm(range(100)):
        time.sleep(0.01)