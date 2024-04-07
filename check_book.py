class checkBook:
    @staticmethod
    def checkSpecificBook():
        book_id = input(" Enter the ID of the book you want to check : ")
        found = False
        with open("my_file.txt", 'r') as f:
            lines = f.readlines()
            for i, line in enumerate(lines):
                if "Book ID :" in line and book_id in line:
                    found = True
                    print(" Here are the details of the book you want to check :")
                    print(" " + lines[i - 1].strip())  # Print the line containing book name
                    print(" " + lines[i].strip())  # Print the line containing book ID
                    print(" " + lines[i + 1].strip())  # Print the line containing author name
                    print(" " + lines[i + 2].strip())  # Print the line containing number of copies
                    print("\n")
            if not found:
                print(" Book ID not found.")
