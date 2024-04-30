A, B = input().split()

minS = int(A.replace('6', '5')) + int(B.replace('6', '5'))
maxS = int(A.replace('5', '6')) + int(B.replace('5', '6'))

print(minS, maxS)