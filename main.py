
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

def main():
    a = input_array("A")
    b = input_array("B")

    print("Массив A:", a)
    print("Массив B:", b)

if __name__ == "__main__":
    main()
