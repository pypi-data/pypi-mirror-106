my_pi = 3.1415926

def add_number(num_one, num_two):
    print('this is function add_number')
    result = num_one + num_two
    return result

class Person():
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def print_info(self):
        print(f'name:{self.name},age:{self.age},gender:{self.gender}')