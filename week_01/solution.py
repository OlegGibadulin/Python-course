"""import sys
import math

if (__name__ == "__main__"):
    try:
        a = sys.argv[1]
        b = sys.argv[2]
        c = sys.argv[3]
    except IndexError:
        print("Err cmd")
        sys.exit()

    if not(a.isdigit() or b.isdigit() or c.isdigit()):
        print("Err input")
        sys.exit()

    a = int (a)
    b = int (b)
    c = int (c)

    D = b * b - 4 * a * c

    if (D <= 0):
        print("Err input")
        sys.exit()

    print(int ((-b - math.sqrt(D)) / (2 * a)))
    print(int ((-b + math.sqrt(D)) / (2 * a)))"""

arr = [12342314213,421,1234,321,432,12,414,23312,234,3214,14,1234]

i = 0
check = 1

while (check):
    check = 0
    for j in range(0, len(arr) - i - 1, 1):
        if (arr[j] > arr[j + 1]):
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            check = 1
    i += 1

print(arr)
