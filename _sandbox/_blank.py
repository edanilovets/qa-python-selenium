def fibonacci(count):
    first, second = 0, 1
    for _ in range(count):
        yield second
        first, second = second, first + second


count = int(input('How many numbers to print: '))
g = fibonacci(count)
for x in g:
    print(x, end=", ")

