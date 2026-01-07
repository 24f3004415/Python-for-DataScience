def SumOfNaturalNumbers(N):
    if N == 1:
        return 1
    return N+SumOfNaturalNumbers(N-1)

result = SumOfNaturalNumbers(10)
print(result)