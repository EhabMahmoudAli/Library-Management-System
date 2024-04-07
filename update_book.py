class UpdateBook:
    @staticmethod
    def update_book():
        book_id = input(" Enter the ID of the book you want to update: ")
        found = False
        updated_data = []
        with open("my_file.txt", 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if "Book ID :" in line and book_id in line:
                    found = True
                    print(" Here are the details of the book you want to update:")
                    print(" " + lines[i - 1].strip())  # Print the line containing book name
                    print(" " + lines[i].strip())  # Print the line containing book ID
                    print(" " + lines[i + 1].strip())  # Print the line containing author name
                    print(" " + lines[i + 2].strip())  # Print the line containing number of copies
                    print("\n")
                    print(" 1) Update book name.")
                    print(" 2) Update book ID.")
                    print(" 3) Update author name.")
                    print(" 4) Update number of book copies.")
                    choice = input(" What would you like to update ? : ")
                    if choice == '1':
                        new_book_name = input(" Enter the updated book name : ")
                        lines[i - 1] = " Book name : " + new_book_name + "\n"
                    elif choice == '2':
                        new_book_id = input(" Enter the updated book ID : ")
                        lines[i] = " Book ID : " + new_book_id + "\n"
                    elif choice == '3':
                        new_author_name = input(" Enter the updated author name : ")
                        lines[i + 1] = " Author name : " + new_author_name + "\n"
                    elif choice == '4':
                        new_number_of_copies = input(" Enter the updated number of copies : ")
                        lines[i + 2] = " number of copies : " + new_number_of_copies + "\n"
                    updated_data = lines
                    break

        if not found:
            print(" Book ID not found.")
        else:
            with open("my_file.txt", 'w') as f:
                f.writelines(updated_data)
            print(" The book data has been updated successfully.")
