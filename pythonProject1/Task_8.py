import os
from functools import reduce
import re


class Task_8:

    def __init__(self):
        pass

    # 1
    def file_exists(self, path):
        return os.path.exists(path)

    # 2
    def read_file(self, path="UsersName.txt"):
        if self.file_exists(path):
            with open(path, 'r') as f:
                for line in f:
                    yield line
        else:
            with open(path, 'w'):
                pass

    # 3
    def encrypts10(self):
        arr = self.read_file()
        arr_list = list(arr)
        num = int(len(arr_list) * 0.1)
        return arr_list[num:]

    # 4
    def rturn_even_line(self):
        arr = self.read_file()
        return [line for i, line in enumerate(arr) if i % 2 == 0]

    # 5
    def check_email(self):
        data = self.read_file("UsersEmail.txt")
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        for line in data:
            if not re.match(pattern, line):
                print(line)
                return False

        return True

    # 6
    def check_email_com(self):
        r = []
        data = self.read_file("UsersEmail.txt")
        pattern = r'^[a-zA-Z0-9._%+-]+@gmail.com'
        for line in data:
            if re.match(pattern, line):
                r.append(line)
        return r

    # 7//לבדוק
    def check_email_user(self):
        results = {}
        data_users = self.read_file()
        data_email = self.read_file("UsersEmail.txt")
        for u, e in zip(data_users, data_email):
            if u in e:
                results[u] = e
        return results

    # 8
    def check_name_in_users(self, name):
        data = self.read_file()
        name += '\n'
        print(name in data)
        print([ord(char) for char in name])
        print(name.count('A'))

    # 9
    def check_first_letter(self):
        listy = list(self.read_file())
        return all(name[0].isupper() for name in listy)
    # 10
    def sum_pay(self):
        listy = list(self.read_file())
        return len(listy)/8*200+len(listy)%8*50
