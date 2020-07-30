class Worker_tab_246000:
    name = 'Андрей'
    surname = 'Петров'
    position = 'Системый администратор'
    wage = 50000
    bonus = 50000
    _income = {'wage': wage, 'bonus': bonus}
    currency = '\u20bd'
    __render_services = ['Установка', 'Поддержка', 'Обновление']


class Position(Worker_tab_246000):

    def get_full_name(self):
        return self.surname + ' ' + self.name

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

    def __get_render_services(self):
        return ((', '.join(self._Worker_tab_246000__render_services)).lower()).capitalize()


villain_woods = Position()

print(f'У сотрудника леса {villain_woods.get_full_name()} доход в месяц составил {villain_woods.get_total_income()} '
      f'{villain_woods.currency}.\n'
      f'Должность в лесу: {villain_woods.position}.\n'
      f'Оказываемые услуги лесу: {villain_woods._Position__get_render_services()}.')