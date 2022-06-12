"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход
1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню
2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню
3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню
4. выход
выход из программы
При выполнении задания можно пользоваться любыми средствами
Для реализации основного меню можно использовать пример ниже или написать свой
"""

count=0
spends=[]

def add():
    print("Сколько хотите добавить?")
    while True:
        addition=input()
        if addition.isdigit():
            addition = float(addition)
            break
        else:
            print("Неверный формат. Введите число")
    return addition

def buy():

    print("Сколько хотите потратить?")
    while True:
        spend=input()
        if spend.isdigit():
            spend = float(spend)
            if spend<= count:
                spend_name = input ("Ведите наименование покупки")
                return spend, spend_name
            else:
                print("Сумма слишком велика, вы не можете ее потратить")
                return 0, "0"
            break
        else:
            print("Неверный формат. Введите число")
    


while True:
    print("У вас на счету {} денег. Что хотите сдеделать?".format(count))
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню')
    if choice == '1':
        count += add()
    elif choice == '2':
        spend, spend_name =buy()
        if spend !=0 :
            count -=spend
            spends.append([spend, spend_name])
        
    elif choice == '3':
        for i in spends:
            print(i)
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')
