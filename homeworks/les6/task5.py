class Stationery:
    title = 'Канцелярские принадлжености'

    def draw(self):
        print(F'Запуск отрисовки с помошью "{self.title}".')


class Pen(Stationery):
    title = 'Pen'


class Pencil(Stationery):
    title = 'Pencil'


class Handle(Stationery):
    title = 'Handle'


pen = Pen()

pencil = Pencil()

handle = Handle()

pen.draw()

pencil.draw()

handle.draw()