class deleteBook:
    @staticmethod
    def delete_specific_book():
        book_id = input(" Enter the ID of the book you want to delete : ")
        found = False
        updated_data = []
        with open("my_file.txt", 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if "Book ID :" in line and book_id in line:
                    found = True
                    print(" Here are the details of the book you want to delete :")
                    print(" " + lines[i - 1].strip())  # Print the line containing book name
                    print(" " + lines[i].strip())  # Print the line containing book ID
                    print(" " + lines[i + 1].strip())  # Print the line containing author name
                    print(" " + lines[i + 2].strip())  # Print the line containing number of copies
                    print("\n")
                    choice = input(" Are you sure ? (y to proceed) : ")
                    if choice.lower() == 'y':
                        # Delete the book data from the list of lines
                        del lines[i-1:i+4]
                        updated_data = lines
                        break
                    else:
                        print(" The process is canceled")
            if not found:
                print(" Book ID not found.")
        with open("my_file.txt", 'w') as f:
            f.writelines(updated_data)
            print(" The book has been deleted successfully.")
