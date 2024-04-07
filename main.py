from add_book import addBook
from check_book import checkBook
from delete_book import deleteBook
from display_books import displayBooks
from update_book import UpdateBook


def controlPanel():
    print("\n")
    print(
        "                                                ************************ Welcome to the electronic library ************************")
    print(" 1) Add book ")
    print(" 2) Display books ")
    print(" 3) Update book ")
    print(" 4) Delete book ")
    print(" 5) Check a book ")
    print(" 6) Exit from system ")
    print("\n")
    choice = int(input(" Choose number : "))
    print("\n")
    counter = 1
    if choice == 1:
        obj = addBook()
        numOfBooks = int(input(" How many books you want to add ? : "))
        print("\n")
        while counter <= numOfBooks:
            print(" Enter the data of book number " + str(counter))
            print("\n")
            obj.addBook()
            print(" The data of the book number " + str(counter) + " is saved successfully")
            print("\n")
            counter = counter + 1
        back_To_Control_Panel_Or_Exit = int(input(" Enter 1 to back to the control panel or 0 to exit : "))
        print("\n")
        if back_To_Control_Panel_Or_Exit == 1:
            controlPanel()
        elif back_To_Control_Panel_Or_Exit != 1:
            print(
                "                                                       ************************ Program is ended ************************")
            print("\n")
    elif choice == 2:
        obj = displayBooks()
        obj.view_all()
        back_To_Control_Panel_Or_Exit = int(input(" Enter 1 to back to the control panel or 0 to exit : "))
        print("\n")
        if back_To_Control_Panel_Or_Exit == 1:
            controlPanel()
        elif back_To_Control_Panel_Or_Exit != 1:
            print(
                "                                                       ************************ Program is ended ************************")
            print("\n")
    elif choice == 3:
        obj = UpdateBook()
        obj.update_book()
        back_To_Control_Panel_Or_Exit = int(input(" Enter 1 to back to the control panel or 0 to exit : "))
        print("\n")
        if back_To_Control_Panel_Or_Exit == 1:
            controlPanel()
        elif back_To_Control_Panel_Or_Exit != 1:
            print(
                "                                                       ************************ Program is ended ************************")
            print("\n")
    elif choice == 4:
        obj = deleteBook()
        obj.delete_specific_book()
        back_To_Control_Panel_Or_Exit = int(input(" Enter 1 to back to the control panel or 0 to exit : "))
        print("\n")
        if back_To_Control_Panel_Or_Exit == 1:
            controlPanel()
        elif back_To_Control_Panel_Or_Exit != 1:
            print(
                "                                                       ************************ Program is ended ************************")
            print("\n")
    elif choice == 5:
        obj = checkBook()
        obj.checkSpecificBook()
        back_To_Control_Panel_Or_Exit = int(input(" Enter 1 to back to the control panel or 0 to exit : "))
        print("\n")
        if back_To_Control_Panel_Or_Exit == 1:
            controlPanel()
        elif back_To_Control_Panel_Or_Exit != 1:
            print(
                "                                                       ************************ Program is ended ************************")
            print("\n")
    elif choice == 6:
        print(
            "                                                       ************************ Program is ended ************************")
        print("\n")
    elif choice < 1 or choice > 6:
        print("Invalid choice ( choose number from 1 to 6 )")
        controlPanel()


controlPanel()
