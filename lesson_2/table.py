value = input("Введите номер химического элемента в таблице Менделеева: ")
if value:
    Num = float(value)
    if Num == 3 :
        print("Li - Литий")
    if Num == 80:
        print("Hg - Ртуть")
    if Num == 17 :
        print ("Cl - Хлор")
    if Num == 25:
        print("Mn - Марганец")
    if Num != 25 != 17 !=80 !=3 :
        print("Нет в базе")
