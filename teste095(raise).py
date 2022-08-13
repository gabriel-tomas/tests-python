def func(num1, num2):
    try:
        return num1 / num2
    except Exception as error:
        raise ZeroDivisionError("\033[31mNão pode ter 0\033[m")

try:
    func(2, 0)
except Exception as error:
    print(error)

