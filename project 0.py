nunber_of_tickerts = int(input("Сколько мест вы хотите забронировать? "))
print ("Укажите возраст каждого посетителя")
coast_basic  = 0
for i in range(nunber_of_tickerts):
    age = int(input("Возраст посетителя: "))
    if age < 18 :
        coast_basic+= 0
        print("Стоимость билета = ", coast_basic)
    elif 18 <= age < 25  :
        coast_basic += 990
    else:
        coast_basic += 1390
if nunber_of_tickerts > 3:
    f = 0.9
else:
    f = 1
print("Сумма к оплате c учётом скидки -", coast_basic * f)


