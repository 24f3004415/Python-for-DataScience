# print 1 to n

def func(i,N):
    if i == N:
        return
    func(i,N-1)
    print(N)

func(0,4)