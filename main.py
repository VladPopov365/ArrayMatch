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

# неповторяющиеся элементы массива А, которые присутствуют в массиве В в нескольких экземплярах
def task_2(a, b):
    result = []

    for x in a:
        if a.count(x) == 1 and b.count(x) >= 2:
            result.append(x)

    return result

# элементы, которые присутствуют в обоих массивах А и В в нескольких экземплярах
def task_3(a, b):
    result = []

    for x in a:
        if a.count(x) >= 2 and b.count(x) >= 2:
            if x not in result:
                result.append(x)

    return result

def main():
    while True:
        print("\n=== МЕНЮ ===")
        print("1. Элементы A, повторяющиеся в B")
        print("2. Неповторяющиеся элементы A, повторяющиеся в B")
        print("3. Элементы, повторяющиеся в A и B")
        print("0. Выход")

        choice = input("Выберите пункт меню: ").strip()

        if choice == "0":
            print("Программа завершена.")
            break

        if choice not in ("1", "2", "3"):
            print("Ошибка: выберите пункт от 0 до 3.")
            continue

        a = input_array("A")
        b = input_array("B")

        if choice == "1":
            result = task_1(a, b)
        elif choice == "2":
            result = task_2(a, b)
        else:
            result = task_3(a, b)

        print("Массив A:", a)
        print("Массив B:", b)
        print("Результат:", result)

if __name__ == "__main__":
    main()
