from fizzBuzz import fizzbuzz
import getpass as gt
from bigO import BigO

def print_hi(name):
    print(f'Hi, {name}')


def fact(n: int) -> int:
    if n <= 1:
        return 1
    print(n)
    return n * fact(n - 1)


if __name__ == '__main__':
    print_hi(gt.getuser())
    exo1 = fizzbuzz(20)
    exo2 = fact(4)
    print(exo2)
    print(exo1)
