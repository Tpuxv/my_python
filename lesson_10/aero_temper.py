stat = open('read_files/temper.stat', 'r')
lst = [float(temp.strip()) for temp in stat]

print('Максимальная температура =', max(lst))
print('Минимальная температура =', min(lst))
print('Средняя температура =', sum(lst) / len(lst))
print('Количество уникальных температур =', len(set(lst)))