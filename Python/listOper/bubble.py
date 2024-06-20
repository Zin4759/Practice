List1 = [1, 10, 9, 2, 4, 3, 6, 5, 8, 7]
List2 = [11, 5, 608, 5, 3, 6, 32, 54, 76, 87, 54, 234, 545]


def sort(Array: list):
    n = len(Array)
    for i in range(n):
        for j in range(n - 1 - i):
            # nested loop를 이용하기 때문에 i는 사용하지 않는다.
            if Array[j] > Array[j+1]:
                Array[j], Array[j+1] = Array[j+1], Array[j]

    return Array


print(sort(List1))
print(sort(List2))
