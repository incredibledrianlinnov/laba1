print ('Enter the size:', end = ' ')
a = int(input())
for i in range (0, a):
    print('* ', end = '')
print('\n', end = '')
for i in range (0, a-2):
    print('*', end = '')
    for f in range (0, a-2):
        print('  ', end = '')
    print(' *')
for i in range (0, a):
    print('* ', end = '')
