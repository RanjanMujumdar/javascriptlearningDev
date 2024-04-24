L1 = [1,2,3,4,5]
L2 = [2,3,4,5,6]

def addlist(L1, L2):
    result = []
    for num1, num2 in zip(L1, L2):
        result.append(num1 + num2)
    return result

print(addlist(L1,L2));