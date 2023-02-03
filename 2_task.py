time_sec = int(input('Введите время в секундах: '))
seconds = time_sec
minutes = round(seconds / 60, 2)
hours = round(minutes / 60, 2)
print(f'Время в формате ч:м:с: {hours}:{minutes}:{seconds}')