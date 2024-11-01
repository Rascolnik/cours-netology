documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
        {"type": "driver license", "number": "5455 028765", "name": "Василий Иванов"},
      ]

directories = {
        '1': ['2207 876234', '11-2', '5455 028765'],
        '2': ['10006'],
        '3': []
      }

def get_name(doc_number):   # вход номер документа, на выход имя из словаря documents
    for set_list in documents:   # перебор словарей из списка
        if set_list["number"] == doc_number:   # ищем совпадение по ключу и входящими данными
            return set_list['name']     # возвращаем имя и словаря в котором было совпадение
            break
    return "Документ не найден"

def get_directory(doc_number):  # вход номер документа, на выход номер полки из словаря directories
    for key in directories:
        if doc_number in directories[key]:  # ищем совпадение по ключу и входящими данными
            return key   # возвращаем ключ как результат
            break
    return "Полки с таким документом не найдено"

def add(document_type, number, name, shelf_number):
    new_doc = {"type": document_type, "number": number, "name": name} # формируем новый словарь
    documents.append(new_doc) # добовляем словарь в documents = []
    if shelf_number in directories: # есть ли в словаре номер полки
        directories[shelf_number].append(number) # добавить номер документа(number) на полку(shelf_number)
    else:
        directories[shelf_number] = [number] # если нет такого списка в словаре создать его




if __name__ == '__main__':
    print(get_name("10006"))
    print(get_directory("11-2"))
    print(get_name("101"))
    add('international passport', '311 020203', 'Александр Пушкин', 3)
    print(get_directory("311 020203"))
    print(get_name("311 020203"))
    print(get_directory("311 020204"))
print(directories)