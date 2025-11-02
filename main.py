# Задача 1

documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

# создал словарь, где ключи это номера полок,а значения это списки номеров документа.
def find_owner(doc_number, docs):
    for doc in docs:
        if doc['number'] == doc_number:
            return doc['name']
    return None

# бесконечный цикл для ввода команд, ищет владельца документа по номеру или выходил по команде 'q'
while True:
    command = input("Введите команду:\n").strip().lower()
    if command == 'p':
        number = input("Введите номер документа:\n").strip()
        owner = find_owner(number, documents)
        if owner:
            print(f"Владелец документа: {owner}")
        else:
            print("Документ не найден.")
    elif command == 'q':
        break

# Незнаю что еще в комментариях написать, но вроде описал что делал)



# Задача 2

documents = [
    {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
    {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
    {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}

def find_document_location(doc_number):
    for shelf, docs in directories.items():
        if doc_number in docs:
            return shelf
    return None

while True:
    command = input("Введите команду (s для поиска, q для выхода): ").strip().lower()
    if command == 'q':
        print("Выход из программы.")
        break
    elif command == 's':
        doc_number = input("Введите номер документа: ").strip()
        shelf = find_document_location(doc_number)
        if shelf:
            print(f"Документ хранится на полке: {shelf}")
        else:
            print("Документ не найден.")
    else:
        print("Неизвестная команда. Попробуйте снова.")

# Досвидания!
