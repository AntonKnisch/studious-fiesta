# S= 1
# N=5
# for i in range (1, N+1) :
#     S *= i
#     print (S)
#
# n = 5
# s =4
# for i in range (1, n+1):
#     print( '*' * i)
# S=0
# while True:
#    if N ** 2 >= 1000:
#        print("Последнее число", N - 1)
#        break
#    N += 1
# list_ = [-5, 2, 4, 8, 12, -7, 5]
# index_negative = None
# for i in range (len(list_)):
#     print("Отрицательное число ", list_)
#     index_negative = i
#     print ("Новый индекс отрицательного числа", index_negative)
# else:
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ : индекс последнего отрицательного элемента=", index_negative)
# ist_ = [-5, 2, 4, 8, 12, -7, 5]
# index_negative = None
# for i, value  in enumerate(list_)):
#     if value < 0
#     print("Отрицательное число ", list_)
#     index_negative = i
#     print ("Новый индекс отрицательного числа", index_negative)
# else:
#     print("---")
# print("Конец цикла")
# print()
# print("Ответ : индекс последнего отрицательного элемента=", index_negative)
# text = """
# У лукоморья дуб зелёный;
# Златая цепь на дубе том:
# И днём и ночью кот учёный
# Всё ходит по цепи кругом;
# Идёт направо -- песнь заводит,
# Налево -- сказку говорит.
# Там чудеса: там леший бродит,
# Русалка на ветвях сидит;
# Там на неведомых дорожках
# Следы невиданных зверей;
# Избушка там на курьих ножках
# Стоит без окон, без дверей;
# Там лес и дол видений полны;
# Там о заре прихлынут волны
# На брег песчаный и пустой,
# И тридцать витязей прекрасных
# Чредой из вод выходят ясных,
# И с ними дядька их морской;
# Там королевич мимоходом
# Пленяет грозного царя;
# Там в облаках перед народом
# Через леса, через моря
# Колдун несёт богатыря;
# В темнице там царевна тужит,
# А бурый волк ей верно служит;
# Там ступа с Бабою Ягой
# Идёт, бредёт сама собой,
# Там царь Кащей над златом чахнет;
# Там русский дух... там Русью пахнет!
# И там я был, и мёд я пил;
# У моря видел дуб зелёный;
# Под ним сидел, и кот учёный
# Свои мне сказки говорил.
# """
#
# text = text.lower()
# text = text.replace(" ", "")
# text = text.replace("\n", "")
# print(text)
# heads = 35  # количество голов
# legs = 94  # количество ног
#
# for r in range(heads + 1):  # количество кроликов
#     for ph in range(heads + 1):  # количество фазанов
#         #  если суммарное количество голов превышено или ног превышено, то переходим на следующий шаг цикла
#         if (r + ph) > heads or \
#             (r * 4 + ph * 2) > legs:
#             continue
#         if (r + ph) == heads and (r * 4 + ph * 2) == legs:
#             print("Количество кроликов", r)
#             print("Количество фазанов", ph)
#             print("---")
# if some_var is None:
#     print("NoneType")
# else:
#     print(type(some_var))
#     some_var = (2,)

# a= [1,2,3,4,5,6,7,8,9,]
# L = list (map(int, input("Введите число").split()))
# print( not any (L))

# for a, b in zip(L,M):
#     print('a =', a, 'b =', b

# num = [int(input (  "введите число билетов: " ))]
# age = [int(input (  "введите возраст: " ))]
# if type(age) == int and 0 <= age <= 18 :
#     print("проходите бесплатно")
# # elif :
#  # age in range (18,26 )
#  #    print("Билет 990 рублей")
# #     print("Число удовлетворяет условиям")
# # age  = [int(input())
# #         if 0 <= a <= 18 :  for i in range(1,19)]
# # age.append(a)
# #         print(age)
# if a and b:
#     print("Обе переменные истинные")
#     print(a,b)
# elif a or b:
#     print("Одна из переменных истинная")
#     print(a or b) # печать одной переменной, той, которая является истинной
# else:
#     print("Обе переменные ложные")
# price_all = 0
# while True:
#     try:
#         ticket_number = input('Сколько билетов вы хотите приобрести на мероприятие? ')
#         ticket_number = int(ticket_number)
#         if type(ticket_number) == int:
#             break
#     except ValueError:
#         print('Введите целое число')
# for i in range(ticket_number):
#     i += 1
#     while True:
#         try:
#             age_for_ticket = input(f'Для какого возраста билет №{i}? ')
#             age_for_ticket = int(age_for_ticket)
#             if age_for_ticket < 18:
#                 print('Билет бесплатный')
#             elif 25 > age_for_ticket >= 18:
#                 price_all += 990
#                 print('Стоимость билета: 990 руб.')
#             else:
#                 price_all += 1390
#                 print('Стоимость билета: 1390 руб.')
#             if type(age_for_ticket) == int:
#                 break
#         except ValueError:
#             print('Введите целое число')
# if ticket_number > 5:
#     price_all = price_all - ((price_all / 100) * 20)
#     print(f'Сумма к оплате {price_all} руб. с учетом 20%-ой скидки на полную стоимость заказа за регистрацию больше 5-и человек')
# else:
#     print(f'Сумма к оплате {price_all} руб.')
# ticket = int(input('Введите количество билетов: '))
# cost = 0
# age = int(input('Введите возраст: '))
# while True:
#
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


