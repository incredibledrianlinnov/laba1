def square(size):
    print(' '.join('*' * size))
    for i in range (0, size - 2):
        print('*' + '  ' * (size - 2)+ ' *')
    print(' '.join('*' * size))

    
a = int(input("Enter the size: "))
square(a)
