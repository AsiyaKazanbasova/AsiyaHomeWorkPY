# Домашнее задание к Семинару №8
# Задача: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал 
# для изменения и удаления данных

# def all_contacts():
#     with open('task19/phone_book.txt', 'r', encoding='utf8') as data:
#         for line in data:
#             print(line)
# all_contacts()

# def find_contact(name):
#     with open('task19/phone_book.txt', 'r', encoding='utf8') as data:
#         for line in data:
#             if name in line:
#                 print(line)
                # break позволяет вывести первое попавшее значение
# find_contact('Иван')

# def add_contact(new_contact):
#     with open('task19/phone_book.txt', 'a', encoding='utf8') as data:
#         data.write('\n'+ new_contact)

# def main_menu(numb):
#     if numb == 1:
#         all_contacts()
#     elif numb == 2:
#         name = input('Введите искомое имя: ')
#         find_contact(name)
#     elif numb == 3:
#         data = input('Введите новый контакт: ')
#         add_contact(data)
# while True:
#     numb = int(input('Введите 1 - для печати всего справочника; 2 - для поиска контакта;' 
#     '3 - для записи контакта; 4 - для выхода из программы: '))
#     if numb == 4:
#         break
#     main_menu(numb)

def change_contact(old_data, new_data) -> str:
    
    with open('task19/phone_book.txt', 'r', encoding='utf8') as data:
        data = data.read()
    with open('task19/phone_book.txt', 'w', encoding='utf8') as data:
        data = data.replace(old_data, new_data)
        data.write(data)
        print('Data replaced')

def delete_contact(del_data):
    with open('task19/phone_book.txt', 'r', encoding='utf8') as data:
        data = data.readlines()
    with open('task19/phone_book.txt', 'w', encoding='utf8') as data:
        for line in data:
            if del_data not in line.strip('\n'):
                data.write(line)

def main_menu(numb):
    if numb == 5:
        old_data = input('Enter data to be replaced: ')
        new_data = input('Enter a new data: ')
        change_contact(old_data, new_data)
    elif numb == 6:
        del_data = input('Enter data to be deleted: ')
        delete_contact(del_data)
while True:
    numb = int(input('Enter 4 - to exit program; 5 - to change data; 6 - to delete data: '))
    if numb == 4:
        break
    main_menu(numb)