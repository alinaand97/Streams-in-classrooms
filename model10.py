# Потоки на классах

import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            time.sleep(1)
            self.enemies -= self.power
            self.days += 1

            # Определяем количество врагов
            remaining = max(self.enemies, 0)
            if remaining == 1:
                print(f"{self.name}, сражается {self.days} день..., осталось {remaining} воин.")
            else:
                print(f"{self.name}, сражается {self.days} дней(дня)..., осталось {remaining} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


# Создание классов рыцарей
first_knight = Knight("Sir Lancelot", 10)
second_knight = Knight("Sir Galahad", 20)

# Запуск потоков
first_knight.start()
second_knight.start()

# Ждем завершения сражений
first_knight.join()
second_knight.join()

# Финальное сообщение
print("Все битвы закончились!")
