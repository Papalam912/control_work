from datetime import datetime
import os

idMain = 0
listOfData = []
filePath = "some.csv"
dictMain = {}

clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

def write_list_to_file(st, path):
    with open(path, 'w+') as data:
        try:
            for i in range(0, len(st)):
                data.write(st[i])
                data.write("\n")
        finally:
            data.close()


def write_dict_to_file(path):
    with open(path, 'w+') as data:
        try:
            for key, val in dictMain.items():
                data.write(f"{key};{val[0]};{val[1]};{val[2]}\n")
        finally:
            data.close()


def read_file_to_list(path):
    somelist = []
    with open(path, 'r') as data:
        try:
            somelist = data.readlines()
            return somelist
        finally:
            data.close()


def printlist(somelist):
    for i in range(0, len(somelist)):
        print(f"{somelist[i]}", end="")


def printDict(someDict:dict):
    for key, val in someDict.items():
        print(f"ID:{key}, {val[0]}, {val[1]}, {val[2]}")
    print()


def parcelist(someList):
    temp = []
    for i in range(len(someList)):
        temp.append(str(someList[i]).split(';'))
    return temp


def nextID():
    global idMain
    idMain +=1

def clearID():
    global idMain
    idMain = 0


def listToDict(someList):
    someDict = {}
    for i in range(0, len(someList)):
        someDict[someList[i][0]]=[someList[i][1], someList[i][2], someList[i][3][:-1]]
    return someDict
    

def addNewNote(title = "Заголовок", bodynote = "Lorem ipsum"):
    dictMain[idMain]=(title, str(datetime.now()), bodynote)
    nextID()


def editNote(ID, title, bodynote):
    dictMain[ID][0]=title
    dictMain[ID][2]=bodynote
    # dictMain[ID][3]=datetime.now()


def readFileToDictAndSetLastID(pathToFile):
    someDict:dict = listToDict(parcelist(read_file_to_list(pathToFile)))
    global idMain
    idMain = int(max(someDict.keys()))+1
    return someDict


# addNewNote()
# addNewNote()
# addNewNote()

# write_dict_to_file(filePath)

# dictMain = readFileToDictAndSetLastID(filePath)

while True:
    cmd = input("Всем привет! Это мой консольный блокнот\n"
                "1. Открыть файл с заметками\n"
                "2. Добавить/создать заметку\n"
                "3. Сохранить изменения\n"
                "4. Прочитать список заметок\n"
                "5. Изменить заметку\n"
                "6. Сортировать заметки по времени\n"
                "7. Удалить заметку\n"
                "8. Выход\n\n")
    clear()

    match cmd:

        case "1":
            print("1. Открыть файл с заметками")
            if (os.path.exists(filePath)):
                dictMain = readFileToDictAndSetLastID(filePath)
                print("Файл прочитан\n")
                printDict(dictMain)
            else:
                print("Файл с заметками не создан\n")

        case "2":
            print("2. Добавить/создать заметку\n")
            title = input("Введите заголовок:\n\n")
            body = input("\nВведите текст заметки:\n\n")
            addNewNote(title, body)
            clear()
            print("2. Заметка, добавлена")
            print(f"\nID: {idMain-1}, Заголовок: {title}, Время записи: {datetime.now()}, Текст заметки: {body}\n")

        case "3":
            print("3. Сохранить заметку(ки) в файл\n")
            if len(dictMain) == 0:
                print("Заметки отсутсвуют\n")
            else:
                write_dict_to_file(filePath)
                print("Успешное сохранение\n")
                printDict(dictMain)

        case "4":
            print("4. Прочитать список заметок\n")
            if (len(dictMain)>0):
                printDict(dictMain)
            else:
                print("Нет ни одной заметки или не прочитан файл\n")

        case "5":
            print("5. Изменить заметку\n")
            idForEdit = input("Напишите ID заметки\nID: ")
            if len(dictMain) == 0:
                print("Заметки отсутсвуют\n")
            elif not dictMain.get(idForEdit):
                print(f"Заметки с ID {idForEdit} не существует\n")
            else:
                print(f"Заголовок: {dictMain[idForEdit][0]}\nТекст заметки: {dictMain[idForEdit][2]}")
                titleForEdit = input(f"Заголовок: ")
                bodyForEdit = input(f"Текст заметки: ")
                editNote(idForEdit, titleForEdit,bodyForEdit)
                print()

        case "6":
            print("6. Сортировать заметки по времени\n")
            print("Не успеваю уже сделать, нужно делать второе задание")

        case "7":
            print("7. Удалить заметку\n")
            idForDel = input("напишите ID заметки для удаления\n\nID: ")
            if len(dictMain) == 0:
                print("\nЗаметки отсутсвуют\n")
            elif not dictMain.get(idForDel):
                print(f"\nЗаметки с ID {idForDel} не существует\n")
            else:
                # idForDel = input("напишите ID заметки для удаления\n\nID: ")
                del(dictMain[idForDel])
                print(f"\nЗаметка {idForDel} удалена\n")
                if len(dictMain) == 0:
                    clearID()

        case "8":
            break

        case __:
            print("Выберите пункт меню\n")