from fizzBuzz import fizzbuzz
import getpass as gt


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':
    print_hi(gt.getuser())
    exo1 = fizzbuzz(20)
    print(exo1)
