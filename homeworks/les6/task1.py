import time
import functools


class TrafficLight:

    __color = None

    def running(self):
        def switching_colors(name_color, time_switch):
            TrafficLight.__color = name_color
            print(TrafficLight.__color)
            time.sleep(time_switch)

        score = 0
        while True:
            score += 1
            switching_colors('Красный', 7)
            switching_colors('Желтый', 2)
            switching_colors('Зеленый', 7)
            if score == 3:
                break
            switching_colors('Желтый', 2)


run = TrafficLight()

run.running()