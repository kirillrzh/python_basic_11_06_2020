class Car:
    speed = None
    color = None
    name = None
    is_police = False

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction='лево'):
        print(f'Машина повернула на {direction}')

    def show_speed(self):
        print(f'Скорость автомобился {self.speed}')

    def vertuhai(self):
        if self.is_police:
            print('Вертухаи на дороге')


class TownCar(Car):
    speed = 55
    color = 'blue'
    name = 'TownCar'

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость привышина!')
        else:
            print(f'Скоростной режим соблюдается.')


class WorkCar(Car):
    speed = 40
    color = 'Yellow'
    name = 'WorkCarr'

    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость привышина!')
        else:
            print(f'Скоростной режим соблюдается.')


class SportCar(Car):
    speed = 200
    color = 'black'
    name = 'SportCar'


class PoliceCar(Car):
    speed = 140
    color = 'black and white'
    name = 'PoliceCar'
    is_police = True


town_car = TownCar()

work_car = WorkCar()

sport_car = SportCar()

police_car = PoliceCar()


def info_car(type_car_class, direction='лево'):
    print(f'Автомобиль: {type_car_class.name}, цвет: {type_car_class.color}, скорость: {type_car_class.speed}')
    type_car_class.go()
    type_car_class.show_speed()
    type_car_class.turn(direction)
    type_car_class.stop()
    print()


info_car(town_car)

info_car(work_car, 'право')

info_car(sport_car)

info_car(police_car)

police_car.show_speed()