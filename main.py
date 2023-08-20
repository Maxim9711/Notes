import UI.UIConsole as ui
import API.API as api

while True:
    ui.menu_console()
    user_input = input()
    if user_input == '1':
        api.show("all")
    elif user_input == '2':
        api.show("ID")
    elif user_input == '3':
        api.show("date")
    elif user_input == '4':
        api.show("all")
        api.change_note()
    elif user_input == '5':
        api.add_note()
    elif user_input == '6':
        api.show("all")
        api.del_notes()
    else:
        print("Program completed")
        break
