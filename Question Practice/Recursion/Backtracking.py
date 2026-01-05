# print 1 to n

def func(i,N):
    if i == N:
        return
    print(N)
    func(i,N-1)
    

func(0,4)