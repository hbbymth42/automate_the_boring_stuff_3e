def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

print('Enter number:')
try:
    input_number = int(input())
    while input_number != 1:
        print(input_number, end=' ')
        input_number = collatz(input_number)
    print(input_number)
except ValueError:
    print('Please enter an integer')
