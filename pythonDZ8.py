# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

# # 1. Программа должна выводить данные
# def prosmotr():
#   spravka=open('spravochka.txt', 'r')
#   for line in spravka:
#       print(line, end='')
#   spravka.close()


# # 2. Программа должна сохранять данные в текстовом файле
# def save():
#   infa=input("Введите данные: ")
#   spravka=open('spravochka.txt', 'a')
#   spravka.write(infa + '\n')
#   spravka.close()

# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# def poiski(poisk):
#     spravka=open('spravochka.txt', 'r')
#     spisok=spravka.read().split("\n")[:-1]
#     dict = dict()
#     for item in spisok:
#         key = item.split(" ")[0]
#         value = item.split(" ")[-1]
#         dict[key] = value
#     for item in spisok:
#         key = item.split(" ")[1]
#         value = item.split(" ")[-1]
#         dict[key] = value
#     poisk=input("Введите данные для поиска номера: ")
#     if poisk in dict:
#         print(dict[poisk])
#     else:
#         print('Нет таких данных в справочнике.')
#     spravka.close()
# poiski()


#  Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных


# def spravka_change(file_spravka, old_dann, new_dann):
#     with open(file_spravka, 'r') as f:
#         old=f.read()
#     new = old.replace(old_dann, new_dann)
       
#     with open(file_spravka, 'w') as f:
#         f.write(new)


# spravka_change("spravochka.txt", "old_dann", "new_dann")
# old_dann=input("Введите данные для изменения: ")
# new_dann=input("Введите новые данные: ")

# spisok=open('spravochka.txt', 'r')
# print("Данные были изменены")
# print(spisok.read())


def spravka_delite(file_spravka, old_dann):
    with open(file_spravka, 'r+') as f:
        old = f.read()
        new = old.replace(old_dann, "")
    with open(file_spravka, 'w') as f:
        f.write(new)


spravka_delite("spravochka.txt", "old_dann")
old_dann=input("Введите данные для удаления: ")

spisok=open('spravochka.txt', 'r')
print("Данные были удалены")
print(spisok.read())

