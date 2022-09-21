Col_vo = int(input("Кол - во человек"))
number_ages = []
for i in range(0, Col_vo):
    age_value = int(input(f'Введите возраст участника №{i + 1}:\n'))
    number_ages.append(age_value)
    def prise(Age):
        if Age < 18:
            return 0
        elif 18 <= Age < 25:
            return 990
        else:
            return 1390
    full_prise: float = sum(map(prise, number_ages))
    discount_prise = float(full_prise * 0.9)
    if Col_vo> 3:
        print('Стоимость всех билетов со скидкой: ', discount_prise, "руб.")
    else:
        print('Стоимость всех билетов: ', full_prise, "руб.")