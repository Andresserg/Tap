import pyautogui
import random
import time

def random_clicks(x1, y1, x2, y2, duration):
    """
    Кликает мышкой в случайной точке в заданной зоне с рандомными интервалами.
    
    :param x1, y1: Верхний левый угол зоны.
    :param x2, y2: Нижний правый угол зоны.
    :param duration: Продолжительность работы кликера (в секундах).
    """
    end_time = time.time() + duration
    while time.time() < end_time:
        # Случайная точка внутри зоны
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)
        
        # Клик по случайной точке
        pyautogui.click(x, y)
        
        # Случайный интервал между кликами
        delay = random.uniform(0.11, 0.24)  # от 140 мс до 300 мс
        time.sleep(delay)

# Пример использования
# Координаты зоны кликов (верхний левый и нижний правый углы)
zone_x1, zone_y1 = 400, 280
zone_x2, zone_y2 = 650, 550

# Продолжительность работы кликера (в секундах)
work_duration = 222

random_clicks(zone_x1, zone_y1, zone_x2, zone_y2, work_duration)
