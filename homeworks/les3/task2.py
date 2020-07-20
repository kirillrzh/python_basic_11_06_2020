def users_info(name, family, years_old, city_residence, e_mail, phone):
    return f'{name}, {family}, {years_old}, {city_residence}, {e_mail}, {phone}'


print(users_info(family='Rozhkov', name='Kirill', city_residence='Mirny', years_old=1991, e_mail='RK@mail.ru',
                 phone='+79069069006'))