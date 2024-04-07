import os


class displayBooks:
    @staticmethod
    def view_all():
        file_path = "my_file.txt"
        file = open("my_file.txt", 'r')
        if os.path.getsize(file_path) == 0:
            print(" There is no books yet.")
            print('\n')
        else:
            read_from_file = file.read()
            print(read_from_file)
            file.close()
