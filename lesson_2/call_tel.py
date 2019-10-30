tel=(input("Введите номер телефона: "))
minut=int(input("Введите время разговора(в минутах): " ))
if tel[1:4]== '343' :
    stoim=15*minut
if tel[1:4]== '381':
    stoim=18*minut
if tel [1:4] == '473':
    stoim=13*minut
if tel [1:4] == '485':
    stoim=11*minut 
print("Стоимость разговора: ",stoim," рублей")
    
    
    
