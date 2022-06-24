from random import randint
import time
from colorama import init
from colorama import Fore, Back, Style

print("Шагает первый человек: ")
sosi = input("Готов?( + ): ")
if sosi =="+":
    for i in range(1):
        a = randint(1,6)
        g = randint(1,6)
        print("Кручю...")
        print()
        time.sleep(3)
        print("Первый кубик:")
        print()
        time.sleep(1)
        print(a)
        print()
        time.sleep(2)
        print("Второй кубик:")
        print()
        time.sleep(1)
        print(g)
else:
    print("Не готов")
    print(Fore.BLACK)
    print(a)
    print(Force.WHITE)
# a g
time.sleep(3)
print()
print("Шагает второй человек: ")
x = input("Готов?( + ): ")
if x == "+":
    for i in range(1):
        v = randint(1,6)
        o = randint(1,6)
        print("Кручю...")
        print()
        time.sleep(3)
        print("Первый кубик:")
        print()
        time.sleep(1)
        print(v)
        print()
        time.sleep(2)
        print("Второй кубик:")
        print()
        time.sleep(1)
        print(o)
else:
    print("Не готов")
l = a + g
k = v + o
if l == l > k:
    print()
    print("Победил 1 игрок")
elif l == l < k:
    print()
    print("Победил 2 игрок")
else:
    print("Ничья")
