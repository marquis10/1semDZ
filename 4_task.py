# 4 задание
revenue = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))
if revenue > costs:
    profit = revenue - costs
    print(f'Финансовый результат фирмы - прибыль. Её величина = {profit}')
    profitability = round(profit / revenue, 2)
    print(f'Рентабельность выручки = {profitability}')
    employees = int(input('Введите численность сотрудников фирмы: '))
    profit_employees = round(profit / employees, 2)
    print(f'Прибыль фирмы в расчёте на 1 сотрудника = {profit_employees}')
else:
    print('Финансовый результат фирмы - убыток')
