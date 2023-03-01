itog = 0
kol_bilet = int(input('Введите цифрами количество билетов: '))
for i in range(kol_bilet):
    i += 1
    vozrast = int(input(f'Введите цифрами количество полных лет посетителя по {i} билету: '))
    if vozrast < 18:
            print('Цена билета - 0 руб.')
    elif 18 <= vozrast < 25:
            itog += 990
            print('Цена билета - 990 руб.')
    else:
            itog += 1390
            print('Цена билета - 1390 руб.')
if kol_bilet > 3:
    total_itog = itog - ((itog / 100) * 10)
    print(f'Сумма к оплате - {total_itog} руб. (учитывая дополнительную скидку 10%, т.к. Вы регистрируете больше трёх человек!)')
else:
    print(f'Сумма к оплате - {itog} руб.')