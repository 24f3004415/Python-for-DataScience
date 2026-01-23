a = 'Sheryians'
b = 'Sheryians'

if len(a) != len(b):
    print('not equal')
else:
    for i in range(len(a)):
        if a[i] != b[i]:
            print('not equal')
            break
    else:
        print('not equal')
