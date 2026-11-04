
def input_array(name):
    while True:
        text = input(f"Введите элементы массива {name} через пробел: ")

        try:
            array = list(map(int, text.split()))

            if len(array) == 0:
                print("Ошибка: массив не должен быть пустым.")
                continue

            return array

        except ValueError:
            print("Ошибка: вводите только целые числа.")

# элементы массива А, повторяющиеся в массиве В несколько раз
def task_1(a, b):
    result = []

    for x in a:
        if b.count(x) >= 2 and x not in result:
            result.append(x)

    return result

def task_2(a, b):
    result = []

    for x in a:
        if a.count(x) == 1 and b.count(x) >= 2:
            result.append(x)

    return result

def main():
    a = input_array("A")
    b = input_array("B")

    print("Массив A:", a)
    print("Массив B:", b)

if __name__ == "__main__":
    main()
