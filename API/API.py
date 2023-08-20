import ClassNote.Note as Note

def write_file(array, mode):
    file = open("notes.csv", mode='w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open("notes.csv", mode=mode, encoding='utf-8')
    for notes in array:
        file.write(Note.Note.to_string(notes))
        file.write('\n')
    file.close

def read_file():
    try:
        array = []
        file = open("notes.csv", "r", encoding='utf-8')
        notes = file.read().strip().split("\n")
        for n in notes:
            split_n = n.split(';')
            note = Note.Note(
                id = split_n[0], title = split_n[1], body = split_n[2], date = split_n[3])
            array.append(note)
    except Exception:
        print('Empty')
    finally:
        return array


def add_note():
    title = input("Enter title:\n")
    body = input("Enter description:\n")
    note = Note.Note(title=title, body=body)
    array_notes = read_file()
    for i in array_notes:
        if Note.Note.get_id(note) == Note.Note.get_id(i):
            Note.Note.set_id(note)
    array_notes.append(note)
    write_file(array_notes, 'a')
    print("Note added")


def show(txt):
    array_notes = read_file()

    if array_notes:
        if txt == "all":
            print("Notes:")
            for i in array_notes:
                print(Note.Note.map_note(i))

        elif txt == "ID":
            for i in array_notes:
                print("ID: ", Note.Note.get_id(i))
            id = input("\nEnter note id:")
            flag = True
            for i in array_notes:
                if id == Note.Note.get_id(i):
                    print(Note.Note.map_note(i))
                    flag = False
            if flag:
                print("ID is not correct")

        elif txt == "date":
            date = input("Enter date (dd.mm.yyyy): ")
            flag = True
            for i in array_notes:
                date_note = str(Note.Note.get_date(i))
                if date == date_note[:10]:
                    print(Note.Note.map_note(i))
                    flag = False
            if flag:
                print("Date is not correct")
        else:
            print("Empty")


def del_notes():
    id = input("Enter the ID of the note to be deleted:")
    array_notes = read_file()
    flag = False

    for i in array_notes:
        if id == Note.Note.get_id(i):
            array_notes.remove(i)
            flag = True

    if flag:
        write_file(array_notes, 'a')
        print("Note deleted")
    else:
        print("ID is not correct")


def change_note():
    id = input("Enter the ID of the note to change:")
    array_notes = read_file()
    flag = True
    array_notes_new = []
    for i in array_notes:
        if id == Note.Note.get_id(i):
            i.title = input("Change title:\n")
            i.body = input("Change description:\n")
            Note.Note.set_date(i)
            logic = False
        array_notes_new.append(i)

    if flag:
        write_file(array_notes_new, 'a')
        print("Note changed")
    else:
        print("ID is not correct")








