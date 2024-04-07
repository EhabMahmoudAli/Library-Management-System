class addBook:
    def addBook(self):
        file = open("my_file.txt", 'a')
        book_name = input(" Enter the book name : ")
        book_ID = input(" Enter the book ID : ")
        with open("my_file.txt", 'r') as f:
            lines = f.readlines()
            for line in lines:
                if "Book ID :" in line and book_ID in line:
                    print(" Book ID already exists. Please enter a different one")
                    return self.addBook()
        author_name = input(" Enter the author name : ")
        number_of_copies = input(" Enter number of copies you want to add : ")
        file.write(" Book name : " + book_name)
        file.write("\n")
        file.write(" Book ID : " + book_ID)
        file.write("\n")
        file.write(" Author name : " + author_name)
        file.write("\n")
        file.write(" number of copies : " + number_of_copies)
        file.write("\n")
        file.write("___________________________________________________________________________________________________________")
        file.write("\n")
        file.close()
